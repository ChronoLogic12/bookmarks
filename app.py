import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import (ObjectId, InvalidId)
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

def get_average_rating(book):
    if len(book["reviews"]) == 0:
        book["avg_rating"] = 0
    else:
        total = 0
        for review in range(0, len(book["reviews"])-1):
            total += book["reviews"][review]["rating"]
        book["avg_rating"] = round(total / len(book["reviews"]))
    return book


# Home route will return recently added and top rated books
@app.route("/")
@app.route("/home")
def home():
    books = list(mongo.db.books.find())
    return render_template("home.html", books=books)


@app.route("/books")
def get_all_books():
    books = list(mongo.db.books.find())
    books_average_rating = []
    for book in books:
        books_average_rating.append(get_average_rating(book))
    return render_template("all_books.html", books=books_average_rating)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.books.aggregate([
  {
    "$search": {
      "index": 'default',
      "text": {
        "query": query,
        "path": {
          'wildcard': '*'
        }
      }
    }
  }
]))
    return render_template("all_books.html", books=books)


@app.route("/books/<book_id>")
def get_book_by_id(book_id):
    book = mongo.db.books.find_one({ "_id": ObjectId(book_id) })
    book = get_average_rating(book)
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
                "reviews": [],
            }

            _id = mongo.db.books.insert_one(new_book).inserted_id      
            return redirect(f"/books/{_id}")
        except Exception as err:
            print(err)
    return render_template("add_book.html")


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.delete_one({"_id": ObjectId(book_id)})
    flash("Book Successfully Removed")
    return redirect(url_for("get_all_books"))


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        new_values = {
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre"),
            "image_url": request.form.get("image-url"),
            "summary": request.form.get("summary"),
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, new_values)
        flash("Book Updated Successfully")

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_book.html", book=book)


@app.route("/add_review/<book_id>", methods=["GET", "POST"])
def add_review(book_id):
    if request.method == "POST":
        user = request.form.get("user") 
        new_review = {
            "author": user,
            "review": request.form.get("review-body"),
            "rating": int(request.form.get("star"))
        }
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        new_values = { "$addToSet": {"reviews": new_review}}
        mongo.db.books.update_one({"_id": ObjectId(book_id)}, new_values)
    return render_template("book.html", book=book)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "get_all_books", username=session["user"]))
            else:
                # invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # invalid username
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username in use")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("get_all_books", username=session["user"]))

    return render_template("register.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)