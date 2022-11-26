from flask import Flask;
from flask import render_template, request, redirect;
import pymysql


app = Flask(__name__)


def sql_connector():
    conn = pymysql.connect(user="root", password="root12345", db="webphishingdetection", host="localhost")
    c = conn.cursor()
    return conn, c


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/index")
def index():
   return render_template('index.html')

@app.route("/h1")
def h1():
    return render_template('h1.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method=='POST':
        userdetails = request.form
        fname = userdetails["fname"]
        lname = userdetails["lname"]
        email = userdetails["email"]
        password = userdetails["password"]

        conn, c = sql_connector()
        c.execute("INSERT INTO signup(fname, lname, email, password) VALUES(%s,%s,%s,%s)",(fname, lname,email, password))
        conn.commit()
        conn.close()
        c.close()


    return render_template('signup.html')


if __name__=='__main__':
    app.run(debug=True)
