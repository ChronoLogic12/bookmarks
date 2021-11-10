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
    return render_template("all_books.html", books=books)

@app.route("/books/<book_id>")
def get_book_by_id(book_id):
    book = mongo.db.books.find_one({ "_id": ObjectId(book_id) })
    
    return render_template("book.html", book=book)

@app.route("/book/add", methods=["POST", "GET"])
def add_book():
    if request.method == "POST":
        try:
            new_book = {
                "title": request.form.get("title"),
                "author": request.form.get("author"),
                "genre": request.form.get("genre"),
                "image_url": request.form.get("image-url"),
                "summary": request.form.get("summary"),
            }

            _id = mongo.db.books.insert_one(new_book).inserted_id      
            return redirect(f"/books/{_id}")
        except Exception as err:
            print(err)
    return render_template("add_book.html")
