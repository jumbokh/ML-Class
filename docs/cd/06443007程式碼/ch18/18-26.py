from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image

alice_mask = np.array(Image.open("cloud_mask7.png"))
wc = WordCloud(background_color="white", max_words=2000, 
               mask=alice_mask, font_path="simsun.ttf")
wc.generate_from_frequencies(df_bow.sum())
wc.to_file("cloud.png")

plt.figure(figsize=(15,15))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")