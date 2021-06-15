from tkinter import Image

import jieba

from matplotlib import pyplot as plt
from wordcloud import Wordcloud
from PIL import image
import numpy as np
import sqlite3

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select introduction from top250movie'
data = cur.execute(sql)

text=""
for item in data:
    text = text+item[0]

cut = jieba.cut(text)
string = ' '.join(cut)
print(string)

img = Image.open(r'/static/assets/img/hero-img.png')
img_array = np.array(img)
wc = WordCloud(
    background_color='white'
)

cur.close()
con.close()