# **BookMarks** - Testing

<p align="center">
    <img src="readme-assets\bookmarks-logo.png" width="200px"/>
</p>

[README.md](README.md)

[Live Site](https://bookmarks-flask-app.herokuapp.com/home)

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
  - [**Manual Testing**](#manual-testing)
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

These changes along with several small styling tweaks have helped make this a more complete and user friendly product.

## **User Stories Testing**

1. As a regular user of this site I want to be able to -

- Find and learn about books
  - The site homepage displays a live update on the highest rated books on the site allowing the user to see what books are currently popular. In addition to this the books page shows all added books and allows the user to search for specific terms within a books title, author, genre and summary fields. Book details pages show full descriptions and details for all titles.

<p align="center">
    <img src="readme-assets\book-details.PNG" width="400px"/>
</p>

- Find a books average rating
  - All book preview cards and book details pages display the books average rating out of 5 to two decimal places along with a graphical representation of this rating.

<p align="center">
    <img src="readme-assets\book-preview-card.PNG" width="400px"/>
</p>

- Search for books by parameters such as title, author and genre
  - The books page allows the user to search for specific terms within a books title, author, genre and summary fields.

<p align="center">
    <img src="readme-assets\search-results.PNG" width="400px"/>
</p>

- Find the currently highest rated books
  - The site home page shows the current top six titles sorted by average user rating.

<p align="center">
    <img src="readme-assets\home-top-rated.PNG" width="400px"/>
</p>

- Add books to the site
  - User can add books to the site by clicking on the prompt from the books page which takes them to a form to add details to the new entry.

<p align="center">
    <img src="readme-assets\add-book-form.PNG" width="400px"/>
</p>
<p align="center">
    <img src="readme-assets\add-book-prompt.PNG" width="400px"/>
</p>

- Write and post reviews for books
  - logged in users that have not already added a review to the current book are prompted to add a review via a card below the books details. Clicking this prompt opens a modal where the user can add the details of their review and select a star rating.

<p align="center">
    <img src="readme-assets\add-review-prompt.PNG" width="400px"/>
</p>

<p align="center">
    <img src="readme-assets\add-review.PNG" width="400px"/>
</p>

- View all reviews I have posted
  -All review written buy a user are displayed on the users profile page.

<p align="center">
    <img src="readme-assets\profile-user-reviews.PNG" width="400px"/>
</p>

- Edit/delete reviews that I have posted
  - User reviews can be edited or deleted by the review author from the reviews section of the pertaining book.

<p align="center">
    <img src="readme-assets/review-open-with-controls.PNG" width="400px"/>
</p>

- View reviews other people have written
  - Any/All reviews for a book are displayed on the books details page.

<p align="center">
    <img src="readme-assets/review-closed.PNG" width="400px"/>
</p>

- Edit/delete books I have added
  - Controls to delete/edit books can be located at the top of a books details page for the user who added the book and site admin.

<p align="center">
    <img src="readme-assets\book-edit-delete-controls.PNG" width="400px"/>
</p>

- Log in to my account
  - Users can navigate to the login page from the navbar or from a prompt on any book details page or the registration page. There they will need to enter their account details into a login form to access their account.

<p align="center">
    <img src="readme-assets\login.PNG" width="400px"/>
</p>
<p align="center">
    <img src="readme-assets\login-register-prompt.PNG" width="400px"/>
</p>

- Log out of my account
  - User can select to log out from the navigation bar located at the top of any page, or the expandable sidenav for mobile users.

<p align="center">
    <img src="readme-assets\nav-desktop.PNG" width="500px"/>
</p>
<p align="center">
    <img src="readme-assets\nav-mobile-sidebar.PNG" width="100px"/>
</p>

2. As a first time visiter to this site I want to be able to -

- Easily understand the purpose of the site
  - The site homepage predominantly displays book preview cards which show book cover art, titles, authors and truncated summaries. This combines with the title and 'Top Rated Books' banner should make the sites intentions clear and obvious.

<p align="center">
    <img src="readme-assets\home-top-rated.PNG" width="400px"/>
</p>

- Learn about specific books
  - The books page allows the user to search for specific terms within a books title, author, genre and summary fields. This would allow a user ot find any currently added book by Title or author with ease.

<p align="center">
    <img src="readme-assets\search-results.PNG" width="400px"/>
</p>

- View reviews other people have written
  - Any/All reviews for a book are displayed on the books details page.

<p align="center">
    <img src="readme-assets/review-closed.PNG" width="400px"/>
</p>

- Create an account
  - Users can navigate to the register page from the navbar or from a prompt on any book details page or the login page. There they will be prompted to complete a registration form to register an account.

<p align="center">
    <img src="readme-assets\register.PNG" width="400px"/>
</p>
<p align="center">
    <img src="readme-assets\login-register-prompt.PNG" width="400px"/>
</p>

3. As an admin of this site I want to be able to -

- Login to an admin account
  - Users can navigate to the login page from the navbar or from a prompt on any book details page or the registration page. There they will need to enter the admin account details into a login form to access their account.

<p align="center">
    <img src="readme-assets\login.PNG" width="400px"/>
</p>
<p align="center">
    <img src="readme-assets\login-register-prompt.PNG" width="400px"/>
</p>

- Log out of an admin account
  - User can select to log out from the navigation bar located at the top of any page, or the expandable sidenav for mobile users.

<p align="center">
    <img src="readme-assets\nav-desktop.PNG" width="500px"/>
</p>
<p align="center">
    <img src="readme-assets\nav-mobile-sidebar.PNG" width="100px"/>
</p>

- Edit the details of a book
- Delete a book
  - The site admin account has access to the delete/edit controls for all books. These controls can be located at the top of any books details page.

<p align="center">
    <img src="readme-assets\book-edit-delete-controls.PNG" width="400px"/>
</p>

- Delete a user review (potentially offensive content)
  - The site admin account has access to delete controls for all user reviews. These controls are located at the bottom of the expandable section of any user review and should be used to remove any offensive content.

<p align="center">
    <img src="readme-assets\review-open-admin-controls.PNG" width="400px"/>
</p>

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
    <img src="readme-assets/html-validation.PNG" width="500px"/>
</p>

### CSS validation

All custom CSS code was tested using the [Jigsaw css validator](https://jigsaw.w3.org/css-validator/) and showed no errors.

<p align="center">
    <img src="readme-assets/css-validation.PNG" width="500px"/>
</p>

### JS validation

All Javascript code was tested using [Beautify Tool Javascript validator](https://beautifytools.com/javascript-validator.php) and returned no errors.

### Python validation

All Python was tested and checked against pep8 standards using pylint in vscode and returned no errors.

## **Manual Testing**

## **Responsive Design**

To test the responsive design of my site I checked each page in various sizes using Google Chromes Dev tools. Chrome dev tools allow you to virtually scale your site to a variety of common device types and also allows you to input specific, custom display dimensions to test any screen size. Using this tool I was able to render each page in a variety of screen sizes and check the results. For each resolution I checked for:

- Clearly legible text
- Consistent styling
- No blocked or hidden elements

Here are some screen shots demonstrating this for the site homepage

- Mobile (375-667px)
<p align="center">
    <img src="readme-assets\mobile-375-667.PNG" width="150px"/>
</p>
- Tablet (768-1024px)
<p align="center">
    <img src="readme-assets\tablet-768-1024.PNG" width="200px"/>
</p>
- Desktop (1920-1080px)
<p align="center">
    <img src="readme-assets\desktop-1920-1080.PNG" width="500px"/>
</p>

## **Bugs**

- The intention of this code was to take a list of all books and return an array containing only reviews from those books written by a specific user. In my first iteration of the code some user profiles were producing an 'IndexError: list index out of range'. To test this error I printed the results at each stage and found the cause. This error was due to the assumption in my code that the index I would be referencing to add the books title to the 'user_reviews' array would be the same as the current index of the for reviews loop. This would only be true under very specific conditions and would not produce the desired, consistent effect. To resolve this issue I created a separate value to allow me to store, update, then append the data to the 'user_reviews' array before the end of the loop without relying on the loop index.

original code

```py
user_reviews = []
for book in books:
    for i in range(len(book["reviews"])):
        if book["reviews"][i]["author"] == username:
            user_reviews.append(book["reviews"][i])
            user_reviews[i]["book_title"] = book["title"]
```

updated code

```py
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
  ```py
  def is_logged_in():
  """Return true if user is in session"""
  try:
      if session and session["user"]:
          return True
      return False
  except:
      return False
  ```
