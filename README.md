# **BookMarks** - Book reviews and recommendations

### Code Institute Milestone Project 3 HTML/CSS/JAVASCRIPT/PYTHON+FLASK/MONGODB - Python and Data Centric Development

<p align="center">
    <img src="readme-assets\bookmarks-logo.png" width="200px"/>
</p>

## **About BookMarks**

BookMarks in an online book review site where users can share their opinions on books the have read and search for their next great read. Whether you love pipe smoking detectives and rainy cities, plucky farm animals banding together to save the day or even action packed battles in space; Share the books that you love with BookMarks. Give your marks and share your review with the community to help others to hear about your top reads and find your next all time favorite.

[BookMarks - Live site](https://bookmarks-flask-app.herokuapp.com/home)

<p align="center">
    <img src="readme-assets\responsive1.PNG" width="1200px"/>
</p>

## **Table of contents**

- [UX design](#ux-design)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [](#)
  - [](#)
- [Features](#features)
  - [](#)
- [Testing](#testing)
- [Deployment](#deployment-github-pages)
- [Credits](#credits)

## **UX design**

### Project Goals

The aim of this project is to produce a website that allows book lovers to rate and review books which they have read and share their thoughts with a wider community. With a average rating system of marks out of 5 a user should be able to tell at a glance the general consensus regarding a given book and have the option to dive deeper into people opinions through access to full written reviews.

### User Stories

#### As a regular user of this site I want to be able to -

- Find and learn about new books
- Find a books average rating
- Search for books by parameters such as title, author and genre
- Find the currently highest rated books
- Add books to the site
- Write and post reviews for books
- View all reviews I have posted
- Edit/delete reviews that I have posted
- View reviews other people have written
- Edit/delete books I have added
- Log in to my account
- Log out of my account

#### As a first time visiter to this site I want to be able to -

- Easily understand the purpose of the site
- Learn about specific books
- View reviews other people have written
- Create an account

#### As an admin of this site I want to be able to -

- Login to an admin account
- Log out of an admin account
- Edit the details of a book
- Delete a book
- Delete a user review (potentially offensive content)

### Wireframes

- [Mobile](readme-assets/bookmarks-wireframe-tablet.png)
- [Tablet](readme-assets/bookmarks-wireframe-mobile.png)
- [Desktop](readme-assets/bookmarks-wireframe-desktop.png)

## **Features**

- Navigation

The sites navigation section is located at the top of all pages. This section contains the BookMarks brand name and logo as well as the page navigation controls for larger displays

<p align="center">
    <img src="readme-assets\nav-desktop.PNG" width="1200px"/>
</p>
or an expandable navigation sidebar for these controls for smaller screens. 
<p align="center">
    <img src="readme-assets\nav-mobile.PNG" width="700px"/>
</p>
<p align="center">
    <img src="readme-assets\nav-mobile-sidebar.PNG" width="100px"/>
</p>
Nav controls responsively employ materializes active styling to indicate to the user the current page.

1. When logged in the page links are as follows: Home - Books - Profile - Sign Out.
2. When logged out the page links are as follows: Home - Books - Sign In - Register.

- Footer

The footer section is located at the bottom of all pages and contains a copyright statement and links to facebook, instagram and twitter.

<p align="center">
    <img src="readme-assets\footer.PNG" width="600px"/>
</p>

### Book preview cards/links

Throughout the site book previews are displayed as cards containing the books basic info such as title, author and average rating as well as the books cover art. Preview cards also function as links to that books details page where they can find further details and review for the title. These preview cards are displayed in one or two column grids depending on the users screen size and site section.

<p align="center">
    <img src="readme-assets\book-preview-card.PNG" width="400px"/>
</p>

### Home

- Top rated books

The first section of the sites home page is dedicated to the books with the highest current average ratings. This section displays book previews for the current six highest rated books.

<p align="center">
    <img src="readme-assets\home-top-rated.PNG" width="600px"/>
</p>

- Editors Picks

The editors pick section of the home page contains short write ups on some of the favorite picks of site editors, encouraging users to check out certain titles and engage with the community. Each write up also contains a preview card to direct the user to the books details page.

<p align="center">
    <img src="" width="600px"/>
</p>

### Books

The books page displays book preview cards for all books

- Add a Book

When logged in the books page will display a prompt to the user to add a new book at the top of the page. See - [Add a book](#add-a-book)

<p align="center">
    <img src="readme-assets\add-book-prompt.PNG" width="500px"/>
</p>

- Search

The search bar at the top of the books page allows the user to sort all books by designating a search term. The page will then display any books that contain matches to the designated term in the 'title', 'author', 'summary' or 'genre' fields.

<p align="center">
    <img src="readme-assets\search.PNG" width="450px"/>
</p>

### Add a book

When selecting the add book button from the books page you are directed to a form to input the details of the new title. The form requires the user to input the books title, author, genre, summary and provide an image url before submitting this information to the database. If an invalid image url is given a placeholder image will replace the invalid value.

<p align="center">
    <img src="readme-assets\add-book-form.PNG" width="600px"/>
</p>

### book<book_id> (book details)

Each book has it's own unique page containing all it's information, user reviews and controls.

- Delete/Edit book controls

If there is a user in session and that user is either the one that added the current book or the site admin a card containing edit and delete buttons will be displayed at the top of the page.

<p align="center">
    <img src="readme-assets\book-edit-delete-controls.PNG" width="600px"/>
</p>

Selecting the delete book button will open a modal asking the user to confirm the books deletion.

<p align="center">
    <img src="readme-assets\delete-book-confirmation.PNG" width="500px"/>
</p>

Selecting delete will remove the book and all reviews from the database. Selecting cancel will close the modal.

Selecting Edit book will direct the user to the edit book page. See - [Edit book](#edit-book)

- Book details

The main section of the page contains the books details. This section is similar to the book preview cards but displays the books full description and the name of the user that added the book.

<p align="center">
    <img src="readme-assets\book-details.PNG" width="700px"/>
</p>

If the current user is **not logged in**, a prompt will render under the book details card directing them to login or register to add a review to the book.

<p align="center">
    <img src="readme-assets\login-register-prompt.PNG" width="500px"/>
</p>

If there **is** a user in session and they have **not** previously submitted a review for the current book a prompt will render directing them to add a review. see - [Add a review](#add-a-review)

<p align="center">
    <img src="readme-assets\add-review-prompt.PNG" width="500px"/>
</p>

- Reviews

Reviews are rendered in a series of cards each containing the name of the user that wrote it and the star rating they gave. Clicking on the card causes it to expand and reveal the review in full. Only one card may be open at a time.

<p align="center">
    <img src="readme-assets\review-closed.PNG" width="600px"/>
</p>
<p align="center">
    <img src="readme-assets\review-open.PNG" width="600px"/>
</p>

If the user viewing a review is in session and the one who submitted it they will also be presented with options to either delete or edit their review. If the current user is the site admin they will have access to only the delete review control.

<p align="center">
    <img src="readme-assets\review-open-with-controls.PNG" width="600px"/>
</p>
<p align="center">
    <img src="readme-assets\review-open-admin-controls.PNG" width="600px"/>
</p>

Selecting the delete review button will open a modal asking the user to confirm the books deletion.

<p align="center">
    <img src="readme-assets\delete-review-confirmation.PNG" width="500px"/>
</p>

Selecting delete will remove the review from the database. Selecting cancel will close the modal.

Selecting edit review will direct the user to the edit review page. See - [Edit review](#edit-review)

- Add a review

Clicking the 'Add a review' button from a books details page will open a modal presenting the user with a form to input the details of their review. This form consists of a text box for the body of the review and a 5 star rating selector.

<p align="center">
    <img src="readme-assets\add-review.PNG" width="500px"/>
</p>

The star rating selector was adapted from [This code](https://codepen.io/jexordexan/pen/yyYEJa) written by Jordan-Simonds. It is highly tactile, interactive and pleasant to use.

<p align="center">
    <img src="readme-assets\star-ratings.gif" width="500px"/>
</p>

Submitting the form will update the current book details page and display the new review.

### Edit book

- Selecting to edit a book will direct the user to form identical to the add book form but pre filled with the books current information. The user is free to make any edits they like then re submit the book updating the database.

<p align="center">
    <img src="readme-assets\edit-book.PNG" width="500px"/>
</p>

### Edit review

- Selecting to edit a review will direct the user to form identical to the add review form but pre filled with the review current information. The user is free to make any edits they like then re submit the review updating the database.

<p align="center">
    <img src="readme-assets\edit-review.PNG" width="500px"/>
</p>

### Profile

- Account details

### Entry

## Testing

### Bugs

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

## Deployment

### Heroku

This project was deployed using Heroku

---

## Credits

### Content

### Media

### Help and info

- Code Institute learning material - general knowledge.
  - [Codecademy](https://www.codecademy.com/learn) - general knowledge.
  - [w3schools](https://www.w3schools.com/) - general knowledge.
  - [MND Web Docs](https://developer.mozilla.org/en-US/) - general knowledge.
  - [Stack Overflow](https://stackoverflow.com/) - debugging.
  - Interactive star rating element adapted from [the work of Jordan-Simonds(jexordexan)](https://codepen.io/jexordexan/pen/yyYEJa)
