from gettext import npgettext
from flask import Flask;
from flask import render_template, request, redirect;
import pymysql
import pickle
import numpy as np
import streamlit as st

app = Flask(__name__)

model = pickle.load(open("ml.pkl","rb"))


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

@app.route("/predict",methods=["Post","GET"])
def predict():
    features=[int(x) for x in request.form.values()]
    final = (np.array(features).reshape(1,-1))
    prediction = model.predict(final)
    output = '{0:.{1}f}'.format(prediction[0][1],2)

    if output==1:
       return render_template("h1.html",pred="This website is a genuine website".format(output))

    if output==(-1):
        return render_template("h1.html",pred="Malicious website, alert!".format(output))
    

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
