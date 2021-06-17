from tkinter import Image

import jieba

from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select introduction from top250movie'
data = cur.execute(sql)

text=""
for item in data:
    text = text+item[0]

#结巴分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(string)
cur.close()
con.close()

img = Image.open(r'/static/assets/img/hero-img.png')
img_array = np.array(img) #将图片转换成数组
wc = WordCloud(
    background_color='white',
    mask = img_array,
    font_path='MAIAN.ttf'
).generate_from_text(string)

#准备绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')

plt.show()
