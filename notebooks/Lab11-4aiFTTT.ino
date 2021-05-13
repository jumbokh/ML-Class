#include <WiFi.h>
#include <WiFiMulti.h>
#include <HTTPClient.h>
//pls use sketch/include library/manage library find simpledht by winlin 
//or you can use another library
#include "DHT.h"
#define DHTPIN 5     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11
// Initialize DHT sensor.
DHT dht(DHTPIN, DHTTYPE);

WiFiMulti wifiMulti;
char* WifiSSID="Tenda_5295A0";
char* WifiPassword="0953313123";
//1.replace https with http 
//2.replace youreventname with your  event name
//3.replace yourkey at the end of url with your key
String IFTTTUrl="http://maker.ifttt.com/trigger/home/with/key/cBVp_iFaovrfRFXjy8P4rn";
void setup() {
    Serial.begin(115200);
    dht.begin();
    Serial.println(F("DHT11 Started!..."));
    wifiMulti.addAP(WifiSSID, WifiPassword);  
    for(uint8_t t = 4; t > 0; t--) {
        Serial.printf("[SETUP] WAIT %d...\n", t);
        Serial.flush();
        delay(1000);
    }
}

void loop() {
    // wait for WiFi connection
    if((wifiMulti.run() == WL_CONNECTED)) {
        //=======Reading dht11 data==============
        Serial.println("reading DHT11...");
        
        //reading data
        float h = dht.readHumidity();
        float t = dht.readTemperature();
        // Check if any reads failed and exit early (to try again).
        if (isnan(h) || isnan(t) ) {
           Serial.println(F("Failed to read from DHT sensor!"));
           return;
        }
        char nmsg[20];
        sprintf(nmsg,"Temperature: %5.2f ,Humidity: %3.0f%s",t,h,"\%");
        Serial.println(nmsg);
        //=======dht11 data read==========
        //regenerate url string with temp and humd
        String url=IFTTTUrl+"?value1="+String(t)+"&value2="+String(h);        

        //Start to send data to IFTTT
        HTTPClient http;
        Serial.print("[HTTP] begin...\n");
        http.begin(url); //HTTP

        Serial.print("[HTTP] GET...\n");
        // start connection and send HTTP header
        int httpCode = http.GET();
        // httpCode will be negative on error
        if(httpCode > 0) {
            // HTTP header has been send and Server response header has been handled
            Serial.printf("[HTTP] GET... code: %d\n", httpCode);
            // file found at server
            if(httpCode == HTTP_CODE_OK) {
                String payload = http.getString();
                Serial.println(payload);
            }
        } else {
            Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
        }
        http.end();
    }
    for(int j=0; j<30; j++){
    delay(30000);//send data every j*30 seconds
    }
}
