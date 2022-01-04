import os
import requests
import validators
from random import expovariate
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for,
    abort)
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


def set_average_rating(book):
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


def set_average_rating_for_all_books(books):
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
        books_average_rating.append(set_average_rating(book))
    return books_average_rating


def is_logged_in():
    """Return true if user is in session"""
    if session and session["user"]:
        return True
    return False


def get_reviews_for_user_from_books(books, username):
    """
    Takes a list containing all the books the user 
    has reviews and their username and returns a list 
    containing only the users reviews.

        Parameter:
            books (list of object): [{}, ]
            username (str): user in session

            returns (list): [user reviews]
    """

    user_reviews = []
    for book in books:
        for i in range(len(book["reviews"])):
            if book["reviews"][i]["author"] == username:
                values = book["reviews"][i]
                values["book_title"] = book["title"]
                user_reviews.append(values)
    return user_reviews


def validate_image_url(image_url):
    """
    Takes a string and checks if it is a valid image url.
    Returns the image_url if true and a placeholder image
    if false
    """
    if not validators.url(image_url):
        return "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=640:*"
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(image_url)
    if r.headers["content-type"] in image_formats:
        return image_url
    return "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=640:*"
    

@app.route("/")
@app.route("/home")
def home():
    try:
        books = set_average_rating_for_all_books(list(mongo.db.books.find()))
        books.sort(key=lambda book: book["avg_rating"], reverse=True)
        return render_template("home.html", books=books[:6])
    except:
        abort(500)


@app.route("/books")
def get_all_books():
    try:
        books = set_average_rating_for_all_books(list(mongo.db.books.find()))
        return render_template("all_books.html", books=books)
    except:
        abort(500)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        try:
            query = request.form.get("query")
            if len(query) < 1:
                raise ValueError("Please input a search value")
            books = list(mongo.db.books.aggregate([{
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
        except ValueError:
            flash("Invalid value. Minimum of one character required")
            return redirect(url_for("get_all_books"))
        except:
            abort(500)


@app.route("/book/<book_id>/view")
def get_book_by_id(book_id):
    try:
        book = mongo.db.books.find_one({ "_id": ObjectId(book_id) })
        book = set_average_rating(book)
        return render_template("book.html", book=book)
    except InvalidId:
        abort(404)
    except:
        abort(500)


@app.route("/book/add", methods=["POST", "GET"])
def add_book():

    if not is_logged_in():
        return redirect(url_for("login"))

    if request.method == "POST":
        try:
            new_book = {
                "title": request.form.get("title"),
                "author": request.form.get("author"),
                "genre": request.form.get("genre"),
                "image_url": validate_image_url(request.form.get("image-url")),
                "summary": request.form.get("summary"),
                "reviews": [],
            }
            _id = mongo.db.books.insert_one(new_book).inserted_id      
            return redirect(url_for("get_book_by_id", book_id=_id))
        except:
            abort(500)
    return render_template("add_book.html")


@app.route("/book/<book_id>/delete")
def delete_book(book_id):

    if not is_logged_in():
        return redirect(url_for("login"))

    try:
        mongo.db.books.delete_one({"_id": ObjectId(book_id)})
        flash("Book Successfully Removed")
        return redirect(url_for("get_all_books"))
    except InvalidId:
        abort(404)
    except:
        abort(500)


@app.route("/book/<book_id>/edit", methods=["GET", "POST"])
def edit_book(book_id):

    if not is_logged_in():
        return redirect(url_for("login"))
        
    if request.method == "POST":
        try:
            new_values = {
                "$set": {
                "title": request.form.get("title"),
                "author": request.form.get("author"),
                "genre": request.form.get("genre"),
                "image_url": validate_image_url(request.form.get("image-url")),
                "summary": request.form.get("summary"),
                }
            }
            mongo.db.books.update_one({"_id": ObjectId(book_id)}, new_values)
            flash("Book Updated Successfully")
            book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
            return render_template("book.html", book=book)
            
        except InvalidId:
            abort(404)
        except:
            abort(500)

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_book.html", book=book)


@app.route("/book/<book_id>/review/add", methods=["GET", "POST"])
def add_review(book_id):

    if not is_logged_in():
        return redirect(url_for("login"))

    if request.method == "POST":
        try:
            book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
            user = session["user"]
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
        except InvalidId:
            abort(404)
        except:
            abort(500)

    return redirect(url_for("get_book_by_id", book_id=book_id))


@app.route("/book/<book_id>/review/delete")
def delete_review(book_id):

    if not is_logged_in():
        return redirect(url_for("login"))

    try:
        user = session["user"]
        mongo.db.books.update_one(
                { "_id": ObjectId(book_id) },
                { "$pull": { 'reviews': { "author": user }
            }});
        flash("Review Successfully Removed")
        return redirect(url_for("get_book_by_id", book_id=book_id))
    except InvalidId:
        abort(404)
    except:
        abort(500)


@app.route("/book/<book_id>/review/edit", methods=["GET", "POST"])
def edit_review(book_id):

    if not is_logged_in():
        return redirect(url_for("login"))

    if request.method == "POST":
        try:
            user = session["user"]
            new_values = { 
                "author": user,
                "review": request.form.get("review-body"),
                "rating": int(request.form.get("star"))
            }
            mongo.db.books.update_one(
                { "_id": ObjectId(book_id), "reviews.author": user },
                { "$set": {"reviews.$": new_values }}
            )
            flash("Review Updated Successfully")
            book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
            return redirect(url_for("get_book_by_id", book_id=book_id))
            
        except InvalidId:
            abort(404)
        except:
            abort(500)
    try:
        user = session["user"]
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        review = mongo.db.books.find_one(
                    { "_id": ObjectId(book_id) },
                    { "reviews": {"$elemMatch": {"author": user}}
                })["reviews"][0];
        
        return render_template("edit_review.html", book=book, review=review)

    except InvalidId:
            abort(404)
    except:
        abort(500)


@app.route("/login", methods=["GET", "POST"])
def login():

    if is_logged_in():
        return redirect(url_for("home"))

    if request.method == "POST":
        try:
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
        except:
            abort(500)
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if is_logged_in():
        return redirect(url_for("home"))

    if request.method == "POST":
        try:
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
        except:
            abort(500)

    return render_template("register.html")


@app.route("/logout")
def logout():
    try:
        # remove user from session cookie
        flash("You have been logged out")
        session.pop("user")
        return redirect(url_for("login"))
    except:
        abort(500)


@app.route("/profile", methods=["POST", "GET"])
def profile():

    if not is_logged_in():
        return redirect(url_for("login"))

    try:
        username = session["user"]
        user = mongo.db.users.find_one({"username": username})
        books = list(mongo.db.books.find({"reviews.author": { "$eq": user["username"] }}))
        user_reviews = get_reviews_for_user_from_books(books, username)
        user["review_count"] = len(user_reviews)
        return render_template("profile.html", user=user, reviews=user_reviews)
    except (InvalidId, TypeError):
        abort(404)
    except:
        abort(500)


# error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)