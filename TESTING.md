# **BookMarks** - Testing

<p align="center">
    <img src="readme-assets\bookmarks-logo.png" width="200px"/>
</p>

## **Table of contents**

- [**BookMarks** - Testing](#bookmarks---testing)
  - [**Table of contents**](#table-of-contents)
  - [**User Testing**](#user-testing)
  - [**User Stories Testing**](#user-stories-testing)
  - [**Performance**](#performance)
  - [**Code Validation**](#code-validation)
    - [HTML validation](#html-validation)
    - [CSS validation](#css-validation)
    - [JS validation](#js-validation)
    - [Python validation](#python-validation)
  - [**Responsive Design**](#responsive-design)
  - [**Bugs**](#bugs)

## **User Testing**

Throughout this project I conducted 'over the shoulder' user tests to asses the usability, readability and functionality of the site and it's features. These tests involved allowing test users to freely use the site while observing to gage how they were engaging with elements to determine if everything was functioning as intended. I also gathered feedback as to how users felt about certain aspects in order to improve the UX. I was able to improve the useability of the site inv various ways thanks to their feedback, such as -

- Removing the prompt to add a review if a user has already submitted one.
- Maintain consistency of hover effects on interactive elements.
- Buttons to move to register from login and vice versa without accessing the navbar to improve mobile useability.
- Star rating values should always be displayed out of their total potential value to improve readability.
- Give feedback of search term and number of results after entering a search so as not to leave a user on a empty page with no explanation.
- More friendly exit message after logging out.
- Books added by a user should appear on their profile page.

These changes along with several small styling tweaks have helped make this a

## **User Stories Testing**

## **Performance**

Site performance was tested using Google Chrome's Lighthouse tool. All pages scored high across all parameters though performance for mobile devices was slightly lower on pages with images as images are user added and not optimized or size adjusted. These are the lighthouse results -

_Each image shows the results for a page for both desktop (left) and mobile (right)_

1. /home

<p align="center">
    <img src="readme-assets/performance/home.png" width="500px"/>
</p>

2. /books

<p align="center">
    <img src="readme-assets/performance/books.png" width="500px"/>
</p>

3. /book/<book_id>/view

<p align="center">
    <img src="readme-assets/performance/book-details.png" width="500px"/>
</p>

4. /book/add

<p align="center">
    <img src="readme-assets/performance/add-book.png" width="500px"/>
</p>

5. /book/<book_id>/edit

<p align="center">
    <img src="readme-assets/performance/edit-book.png" width="500px"/>
</p>

6. /book/<book_id>/review/edit

<p align="center">
    <img src="readme-assets/performance/edit-review.png" width="500px"/>
</p>

7. /profile

<p align="center">
    <img src="readme-assets/performance/profile.png" width="500px"/>
</p>

8. /login

<p align="center">
    <img src="readme-assets/performance/login.png" width="500px"/>
</p>

9. /register

<p align="center">
    <img src="readme-assets/performance/register.png" width="500px"/>
</p>

## **Code Validation**

### HTML validation

All HTML was tested using [Nu HTML Checker](https://validator.w3.org/nu/) and returned no errors.

<p align="center">
    <img src="readme-assets/html-validation.png" width="500px"/>
</p>

### CSS validation

All custom CSS code was tested using the [Jigsaw css validator](https://jigsaw.w3.org/css-validator/) and showed no errors.

<p align="center">
    <img src="readme-assets/css-validation.png" width="500px"/>
</p>

### JS validation

All Javascript was tested using [Beautify Tool Javascript validator](https://beautifytools.com/javascript-validator.php) and returned no errors.

### Python validation

Python was tested and check against pep8 standards with pylint in vscode and returned no errors.

## **Responsive Design**

## **Bugs**

- The intention of this code was to take a list of all books and return an array containing only reviews from those books written by a specific user. In my first iteration of the code some user profiles were producing an 'IndexError: list index out of range'. To test this error I printed the results at each stage and found the cause. This error was due to the assumption in my code that the index I would be referencing to add the books title to the 'user_reviews' array would be the same as the current index of the for reviews loop. This would only be true under very specific conditions and would not produce the desired, consistent effect. To resolve this issue I created a separate value to allow me to store, update, then append the data to the 'user_reviews' array before the end of the loop without relying on the loop index.

original code

```
user_reviews = []
for book in books:
    for i in range(len(book["reviews"])):
        if book["reviews"][i]["author"] == username:
            user_reviews.append(book["reviews"][i])
            user_reviews[i]["book_title"] = book["title"]
```

updated code

```
user_reviews = []
for book in books:
    for i in range(len(book["reviews"])):
        print(book["reviews"][i]["author"])
        if book["reviews"][i]["author"] == username:
            values = book["reviews"][i]
            values["book_title"] = book["title"]
            user_reviews.append(values)
```

- During testing I discovered that logging out was causing a KeyError. Reading the error message I discovered this was due to the server checking for a 'user' key in session directly after removing this key. The logout route was directing to the login page which was checking for a user in session. Searching for a key that did not exist was causing the error. I instead decided to direct a user back to the homepage instead after logging out as it is unlikely for a user to want to log back in directly after having logged out.
  - The function I created to test if a user was logged in or not was also causing a key error when the login route was called with either an incorrect username or password. By placing the session check inside a try except block I was able to return 'False' for any state other than a logged in user resolving the error.
  ```
  def is_logged_in():
  """Return true if user is in session"""
  try:
      if session and session["user"]:
          return True
      return False
  except:
      return False
  ```
