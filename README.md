# **BookMarks** - Book reviews and recommendations

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

- [**BookMarks** - Book reviews and recommendations](#bookmarks---book-reviews-and-recommendations)
  - [**About BookMarks**](#about-bookmarks)
  - [**Table of contents**](#table-of-contents)
  - [**UX design**](#ux-design)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
      - [As a regular user of this site I want to be able to -](#as-a-regular-user-of-this-site-i-want-to-be-able-to--)
      - [As a first time visiter to this site I want to be able to -](#as-a-first-time-visiter-to-this-site-i-want-to-be-able-to--)
      - [As an admin of this site I want to be able to -](#as-an-admin-of-this-site-i-want-to-be-able-to--)
    - [Wireframes](#wireframes)
    - [Design](#design)
  - [**Features**](#features)
    - [Navigation](#navigation)
    - [Footer](#footer)
    - [Flash messages](#flash-messages)
    - [Book preview cards](#book-preview-cards)
    - [Home](#home)
    - [Books](#books)
    - [Add a book](#add-a-book)
    - [Book details](#book-details)
    - [Edit book](#edit-book)
    - [Edit review](#edit-review)
    - [Profile](#profile)
    - [Entry](#entry)
    - [Error pages](#error-pages)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Help and info](#help-and-info)

## **UX design**

### Project Goals

The aim of this project is to produce a website that allows book lovers to rate and review books which they have read and share their thoughts with a wider community. With a average rating system of marks out of 5 a user should be able to tell at a glance the general consensus regarding a given book and have the option to dive deeper into peoples opinions through access to full written reviews.

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

Wireframes were created for mobile, tablet and desktop screen sizes with [Figma](https://www.figma.com)

- [Mobile](readme-assets/bookmarks-wireframe-tablet.png)
- [Tablet](readme-assets/bookmarks-wireframe-mobile.png)
- [Desktop](readme-assets/bookmarks-wireframe-desktop.png)

### Design

As the focus of this site is the books I chose to use a very simple colour pallet with only one colour. This single action colour makes it easy to identify important aspects of any page and avoids causing visual clutter when placed on a page with multiple book covers of varying colours and styles. The site uses consistent styling of elements throughout to further promote readability. The site uses materializes 12 column grid system to achieve a responsive layout.

## **Features**

### Navigation

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

### Footer

The footer section is located at the bottom of all pages and contains a copyright statement and links to facebook, instagram and twitter.

<p align="center">
    <img src="readme-assets\footer.PNG" width="600px"/>
</p>

### Flash messages

Flash messages are used across the site to give feedback to users in response to their inputs. These responses include confirmation of successful login, logout, register, add new book, add new review as well as informing users or errors such as incorrect username and/or password and username already in user. Flash messages are always rendered at the top of the page.

<p align="center">
    <img src="readme-assets\flash-welcome.PNG" width="600px"/>
</p>
<p align="center">
    <img src="readme-assets\flash-review-added.PNG" width="600px"/>
</p>
<p align="center">
    <img src="readme-assets\flash-logout.PNG" width="600px"/>
</p>

### Book preview cards

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
    <img src="readme-assets\editors-picks.PNG" width="600px"/>
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

### Book details

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

Each users profile page contains three sections. The first section is a full size banner displaying the Username and a count of the total number of reviews the user has added.

<p align="center">
    <img src="readme-assets\user-profile-banner.PNG" width="500px"/>
</p>

The next section contains all of a users submitted reviews. These review cards follow the same format as on the book details pages but displays the name of the book the review is for instead of the review authors username.

<p align="center">
    <img src="readme-assets\profile-user-reviews.PNG" width="500px"/>
</p>

The final section displays book preview card/links for each book that the user has added to the site.

<p align="center">
    <img src="readme-assets\profile-added-books.PNG" width="500px"/>
</p>

### Entry

- Login

This page consists of a login form with fields for username and password, a submit button and a section to direct users to the register page if they do not currently have a registered account. Inputs are checked on submission and if they are valid and match a registered user they will be logged in. If the data is invalid/incorrect either a form prompt or flash message will give feedback to the user and direct them to try again.

<p align="center">
    <img src="readme-assets\login.PNG" width="500px"/>
</p>

- Register

The register page is similar in layout to the login page but the main form is to register a new account and the prompt section directs to the login page for already registered users. On submission details are checked against registered users to determine if the given username is unique. If it is unique a new user account will be registered, if it is not, a flash message will be displayed asking the user to pick a different username.

<p align="center">
    <img src="readme-assets\register.PNG" width="500px"/>
</p>

### Error pages

Site site uses custom error 404 and 500 pages which direct the user back to the site homepage without using browser controls.

<p align="center">
    <img src="readme-assets\error404.PNG" width="150px"/>
</p>
<p align="center">
    <img src="readme-assets\error500.PNG" width="250px"/>
</p>

## Testing

For full testing documentation please see [TESTING.md](TESTING.md)

## Deployment

### Heroku

This project was deployed using Heroku

---

## Credits

### Content

- [Materialize](https://materializecss.com/)
- [Google fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)

### Media

### Help and info

- Code Institute learning material - general knowledge.
  - [Codecademy](https://www.codecademy.com/learn) - general knowledge.
  - [w3schools](https://www.w3schools.com/) - general knowledge.
  - [MND Web Docs](https://developer.mozilla.org/en-US/) - general knowledge.
  - [Stack Overflow](https://stackoverflow.com/) - debugging.
  - Interactive star rating element adapted from [the work of Jordan-Simonds(jexordexan)](https://codepen.io/jexordexan/pen/yyYEJa)
