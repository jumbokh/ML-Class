# ML-Class
#### CSU CSIE 1092 
### Outline
* Python基本功能介紹 [github](https://github.com/joelgrus/data-science-from-scratch)
    * [python基礎](https://docs.google.com/presentation/d/1JCgnwv0qgWh8K117y-hkVyBj1sXzETDLq9mfJ--7sb0/edit#slide=id.p)
    * [數據分析](https://github.com/jumbokh/ML-Class/blob/main/docs/%E5%8D%81%E9%80%B1%E5%85%A5%E9%96%80%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90%E5%AD%B8%E7%BF%92%E8%A8%88%E7%95%AB.pdf)
* Pandas DataFrame介紹
* 資料預處理
* 簡單線性迴歸
    * [kaggle: simple regression](https://www.kaggle.com/kuntahsieh/simple-one-feature-linear-regression)
* 多元線性迴歸
* 羅吉斯迴歸
    * [二元分類 imdb-1](https://github.com/jumbokh/ML-Class/blob/main/notebooks/imdb_ana_v2-1.ipynb)
    * [二元分類 imdb-2](https://github.com/jumbokh/ML-Class/blob/main/notebooks/imdb_sentiment_analysis_keras_and_tensorflow.ipynb)
* CNN
    * [CNN pdf](https://github.com/jumbokh/ML-Class/blob/main/docs/CNN.pdf)
    * [CNN MNIST](https://github.com/jumbokh/ML-Class/blob/main/notebooks/02_1_%E7%94%A8CNN%E5%9C%96%E5%BD%A2%E8%BE%A8%E8%AD%98%EF%BC%88%E9%82%84%E6%98%AFMNIST%EF%BC%89.ipynb)
    * [kaggle: CNN MNIST for Beginners](https://www.kaggle.com/kuntahsieh/mnist-with-keras-for-beginners-99457/edit)
* K最近鄰 [資料說明](https://github.com/jumbokh/ML-Class/blob/main/KNN-Data.md)
    * [KNN Introduction](https://colab.research.google.com/github/jumbokh/ML-Class/blob/main/ML/notebooks/KNN/05_11_K_Means.ipynb)
    * [iris k-means](https://github.com/jumbokh/ML-Class/blob/main/notebooks/iris_kmeans.ipynb)
    * [kaggle: Simple k-means](https://github.com/jumbokh/ML-Class/blob/main/notebooks/simple-k-means-clustering-on-the-iris-dataset.ipynb)
    * [sikit learn](https://scikit-learn.org/stable/modules/neighbors.html)
    * [pima Indian](https://github.com/jumbokh/ML-Class/blob/main/ML/notebooks/KNN/pima-indian/pima-indians-diabetes-beginner.ipynb)
    * [PIMA](https://colab.research.google.com/github/jumbokh/ML-Class/blob/main/ML/notebooks/KNN/pima-indian/pima-indian-diabetes-binary-classification.ipynb)
    * [Dating Web](https://colab.research.google.com/github/jumbokh/ML-Class/blob/main/ML/notebooks/KNN/KNN.ipynb)
    * [Dating Web II](https://colab.research.google.com/github/jumbokh/ML-Class/blob/main/ML/notebooks/KNN/knn_DatingWeb.ipynb)
    * [討論](https://github.com/jumbokh/ML-Class/blob/main/ML/notebooks/KNN/05_11_K_Means.ipynb)
##
<pre>
簡單來說，KNN就是讓你透過一群已經標記好類別的資料，來針對未分類的資料做分類的工具。

那如果只有一群尚未分類的資料，我們要怎麼將他分類呢？這邊就是非監督式學習(Unsupervised learning)中的K-Means
</pre>
* [PCA 降維](https://github.com/jumbokh/ML-Class/tree/main/PCA)
* [iFTTT](https://github.com/jumbokh/ML-Class/blob/main/ML/docs/ESP32-iFTTT.pptx) [Arduino code](https://github.com/jumbokh/ML-Class/blob/main/notebooks/Lab11-4aiFTTT.ino)
    * 參考: [尤老師網站介紹 ESP32 連接 iFTTT](https://youyouyou.pixnet.net/blog/post/119623728)
* [ApacheCN](https://github.com/apachecn/apachecn-ds-zh)
##
#### Tiny Machine Learning
* [Hello World](https://github.com/jumbokh/ML-Class/blob/main/train_hello_world_model.ipynb)
* [住家溫溼度偵測紀錄](https://docs.google.com/spreadsheets/d/1xsixeOMXjxuMVfYnTpc3QVSiCBwI8WdMUyirBemWlJU/edit?usp=sharing)
##
#### RNN
* [李宏毅 教授 pdf](https://github.com/jumbokh/ML-Class/blob/main/RNN/RNN%20(v2).pdf)
* [李宏毅 ML 課程](https://www.youtube.com/watch?v=xCGidAeyS4M&list=RDCMUC2ggjtuuWvxrHHHiaDH1dlQ&start_radio=1&rv=xCGidAeyS4M&t=1)
* [IMDB 使用 RNN](https://github.com/jumbokh/ML-Class/blob/main/RNN/04_1_%E7%94%A8RNN%E5%81%9A%E6%83%85%E6%84%8F%E5%88%86%E6%9E%90.ipynb)
* [Simple RNN & LSTM](https://colab.research.google.com/github/jumbokh/ML-Class/blob/main/RNN/DL_TF2-Ch06-Workshop-RNN_and_LSTM-IMDB_Dataset.ipynb.ipynb)
* [Kaggle: RNN vs LSTM on Bitcoin dataset](https://www.kaggle.com/etatbak/rnn-vs-lstm-on-bitcoin-dataset)
##
### SOM
* [WiKi: 曼哈頓距離](https://zh.wikipedia.org/wiki/%E6%9B%BC%E5%93%88%E9%A0%93%E8%B7%9D%E9%9B%A2)
* [WiKi: 距離](https://zh.wikipedia.org/wiki/%E8%B7%9D%E7%A6%BB#%E6%AD%90%E5%B9%BE%E9%87%8C%E5%BE%97%E8%B7%9D%E9%9B%A2)
* [小羊的研究筆記: Self-organizing map](https://alaric-research.blogspot.com/2011/02/self-organizing-map.html)
* [SOM 簡單範例](https://github.com/jumbokh/intro-computers/blob/master/refers/%E8%81%9A%E9%A1%9E%E7%AF%84%E4%BE%8B6.pdf)
* [Basic uses of SOMPY library](https://github.com/jumbokh/ML-Class/blob/main/notebooks/Basic_Exaples_20160908.ipynb)
* [SOM Notebook](https://nbviewer.jupyter.org/github/jumbokh/DataScience_1082/blob/master/src/immp_sompy_simple.ipynb)
* [SOM 二](https://nbviewer.jupyter.org/github/jumbokh/DataScience_1082/blob/master/src/immp_som.ipynb)
* [以動物特徵分類](https://github.com/jumbokh/ML-Class/blob/main/notebooks/SOM_animal.ipynb) 資料: [features.csv](https://github.com/jumbokh/ML-Class/blob/main/ML/data/features.csv)
##
### 支援向量機
* [ML Lecture 20：Support Vector Machine (SVM)](https://www.cupoy.com/collection/00000168E4E001DA000000016375706F795F72656C656173654355/00000168EA21EFFD0000001E6375706F795F72656C656173654349)
* [李宏毅_ML_Lecture_20](https://hackmd.io/@shaoeChen/B1CoXxvmm/https%3A%2F%2Fhackmd.io%2Fs%2FB1zzzspxE)
* [簡報](http://speech.ee.ntu.edu.tw/~tlkagk/courses/ML_2016/Lecture/SVM%20%28v5%29.pdf)
* [kaggle: Support Vector Machines Classifier Tutorial with Python](https://www.kaggle.com/kuntahsieh/svm-classifier-tutorial/edit)
* [SVM example](https://github.com/HuangYukun/columbia_cs_deep_learning_1) [,notebook](https://github.com/jumbokh/ML-Class/blob/main/notebooks/task1-basic_classifiers.ipynb)
* [Python Data Science Handbook 書本範例](https://github.com/jumbokh/ML-Class/blob/main/notebooks/5_7_Support_Vector_Machines.ipynb)
* [SVM、SVC、SVR三者的區別](https://zhuanlan.zhihu.com/p/37702043)
##
### 決策樹
* [決策樹(Decision Tree)以及隨機森林(Random Forest)介紹](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC3-5%E8%AC%9B-%E6%B1%BA%E7%AD%96%E6%A8%B9-decision-tree-%E4%BB%A5%E5%8F%8A%E9%9A%A8%E6%A9%9F%E6%A3%AE%E6%9E%97-random-forest-%E4%BB%8B%E7%B4%B9-7079b0ddfbda)
* [一文看懂決策樹](https://www.chainnews.com/zh-hant/articles/640320083565.htm)
* [決策樹模型介紹](https://pyecontech.com/2019/07/15/decision_tree/)
#### Youtube:
* [ML Lecture 22: Ensemble](https://www.youtube.com/watch?v=tH9FH1DH5n0)
* [Decision Tree :: Decision Tree Hypothesis @ Machine Learning Techniques](https://www.youtube.com/watch?v=dAqPpAXnMJ4)
* [非監督式學習 (Unsupervised Learning)](https://www.youtube.com/watch?v=wQrghGJvSzs)
#### Kaggle:
* [Titanic](https://www.kaggle.com/c/titanic/notebooks)
* [Kaggle notebooks, most voted](https://github.com/jumbokh/ML-Class/blob/main/notebooks/titanic-data-science-solutions.ipynb)
#### Refers:
* [決策樹](https://github.com/jumbokh/ML-Class/blob/main/docs/%E6%B1%BA%E7%AD%96%E6%A8%B9.pdf) (數據科學入門 第十七章, Joel Grus 著, 高蓉 韓波譯, 歐萊里)
##
### Reference
* ![ML](https://github.com/jumbokh/ML-Class/blob/main/images/ML.PNG)
* ![ML1](https://github.com/jumbokh/ML-Class/blob/main/images/ML.jpg)
* [Over-sampling](https://imbalanced-learn.org/stable/over_sampling.html)
* [imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn)
* https://pub.towardsai.net/machine-learning-algorithms-for-beginners-with-python-code-examples-ml-19c6afd60daa
* https://github.com/jumbokh/python-machine-learning-book-3rd-edition
* https://github.com/jumbokh/python_learn
* https://github.com/jumbokh/PythonDataScienceHandbook
* https://github.com/jumbokh/pyprogbook
* https://github.com/jumbokh/machine-learning-course
* https://github.com/jumbokh/deep-learning-with-python-notebooks
* https://github.com/jumbokh/data-science-with-python
* https://github.com/jumbokh/Python-100-Days
* https://github.com/jumbokh/handson-ml2
* [Machine Learning tutorial of beginner](https://github.com/jumbokh/ML-Class/blob/main/notebooks/machine-learning-tutorial-for-beginners.ipynb)
* [默默地學 Deep Learning (7)-透過Keras進行非監督式分群](https://medium.com/%E7%94%A8%E5%8A%9B%E5%8E%BB%E6%84%9B%E4%B8%80%E5%80%8B%E4%BA%BA%E7%9A%84%E8%A9%B1-%E5%BF%83%E4%B9%9F%E6%9C%83%E7%97%9B%E7%9A%84/%E9%BB%98%E9%BB%98%E5%9C%B0%E5%AD%B8-deep-learning-7-%E9%80%8F%E9%81%8Ekeras%E9%80%B2%E8%A1%8C%E9%9D%9E%E7%9B%A3%E7%9D%A3%E5%BC%8F%E5%88%86%E7%BE%A4-3afb57ea990c)
* [Introduction to Anomaly Detection: Concepts and Techniques](https://iwringer.wordpress.com/2015/11/17/anomaly-detection-concepts-and-techniques/)
* [Unsupervised Anomaly Detection](https://github.com/jumbokh/Unsupervised_Anomaly_Detection)
* [Raspberry pi 3 install pytorch](https://medium.com/hardware-interfacing/how-to-install-pytorch-v4-0-on-raspberry-pi-3b-odroids-and-other-arm-based-devices-91d62f2933c7)
* [輕鬆學習 Python：透過 API 擷取網站資料](https://medium.com/datainpoint/python-essentials-requesting-web-api-edd417a57ba5)
* [Data Science from scratch Links](https://github.com/joelgrus/data-science-from-scratch/blob/master/links.md)
* [Data Science from scratch](https://github.com/joelgrus/data-science-from-scratch)
### Gov Data
* [氣象資料](http://e-service.cwb.gov.tw/HistoryDataQuery/)
* [農產批發市場](https://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx)
* [農業資料](https://drive.google.com/drive/folders/1RQewO9e73hW45cdQR_Q6EQ8Kf5sXxzvx?usp=sharing)
