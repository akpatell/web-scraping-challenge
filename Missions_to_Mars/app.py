# imports

import pymongo
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo 
import scrape_mars

app = Flask(__name__)
# app.config["MONGO_URI"] = 'mongodb://localhost:27017/myDatabase'
# mongo = PyMongo(app)

@ app.route("/")
def index():
    return "Your reached the index"

@ app.route("/scrape")
def scrape():
    return "Your reached the scrape route"

if __name__ == "__main__":
    app.run()