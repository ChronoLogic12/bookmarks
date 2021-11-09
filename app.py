import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import (ObjectId, InvalidId)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Home route will return recently added and top rated books
@app.route("/")
@app.route("/home")
def home():
    books = list(mongo.db.books.find())
    return render_template("home.html", books=books)


@app.route("/books")
def get_all_books():
    books = list(mongo.db.books.find())
    return render_template("home.html", books=books)
