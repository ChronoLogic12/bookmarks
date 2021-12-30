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
    """
    Takes a book object and returns an updated object
    containing the calculated average review value.

        Parameters:
            book (obj): {}

            Returns (obj): {**book, avg_rating (int)}
    """

    if len(book["reviews"]) == 0:
        book["avg_rating"] = 0
    else:
        total = 0
        for review in range(0, len(book["reviews"])):
            total += book["reviews"][review]["rating"]
        book["avg_rating"] = round(total / len(book["reviews"]), 2)
    return book


def get_all_average_ratings(books):
    """
    Takes a list of book objects and returns an updated
    list with average review values calculated for each book.

        Parameters:
            books (list): A list of book objects

        Returns:
            books_average_rating (list): A list of book objects
            containing calculated average ratings
    """
    books_average_rating = []
    for book in books:
        books_average_rating.append(get_average_rating(book))
    return books_average_rating


# Home route will return recently added and top rated books
@app.route("/")
@app.route("/home")
def home():
    books = get_all_average_ratings(list(mongo.db.books.find()))
    books.sort(key=lambda book: book["avg_rating"], reverse=True)
    return render_template("home.html", books=books[:6])


@app.route("/books")
def get_all_books():
    books = get_all_average_ratings(list(mongo.db.books.find()))
    return render_template("all_books.html", books=books)


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
  }]))
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
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        user = request.form.get("user")
        # check if user has already submitted a review for this book
        for review in range(0, len(book["reviews"])):
            if book["reviews"][review]["author"] == user:
                flash("You have already submitted a review for this book")
                return redirect(url_for("get_book_by_id", book_id=book_id))
        new_review = {
            "author": user,
            "review": request.form.get("review-body"),
            "rating": int(request.form.get("star"))
        }   
        new_values = { "$addToSet": {"reviews": new_review}}
        mongo.db.books.update_one({"_id": ObjectId(book_id)}, new_values)
    return redirect(url_for("get_book_by_id", book_id=book_id))


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


@app.route("/profile/<username>", methods=["POST", "GET"])
def profile(username):
    user = mongo.db.users.find_one({"username": username})
    books = list(mongo.db.books.find({"reviews.author": { "$eq": user["username"] }}))
    user_reviews = []
    for book in books:
        for i in range(len(book["reviews"])):
            if book["reviews"][i]["author"] == username:
                values = book["reviews"][i]
                values["book_title"] = book["title"]
                user_reviews.append(values)
    user["review_count"] = len(user_reviews)
    return render_template("profile.html", user=user, reviews=user_reviews)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)