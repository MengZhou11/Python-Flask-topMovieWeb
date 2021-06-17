from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    return home()

@app.route('/movie')
def top250():
    datalist = []
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    sql = "select * from top250movie"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template("index2.html", movies=datalist)

@app.route('/rating')
def rating():
    score = []
    count = []
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    sql = "select score,count(rating) from top250movie group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        count.append(item[1])
    cur.close()
    conn.close()

    return render_template("index3.html", score=score, count=count)


@app.route('/WordCloud')
def WordCloud():
    return render_template("index4.html")

if __name__ == '__main__':
    app.run()
