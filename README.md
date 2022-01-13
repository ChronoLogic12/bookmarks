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
  - [Database schema](#database-schema)
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
    - [**Cloning and running locally**](#cloning-and-running-locally)
    - [**Connecting to Mongodb**](#connecting-to-mongodb)
    - [Deploying to Heroku](#deploying-to-heroku)
  - [Potential Future Features](#potential-future-features)
  - [Credits](#credits)
    - [Services](#services)
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

## Database schema

The data for this project is stored using mongo db and uses two collections for data; One for books and one for users. This is how the data is organized.

1. Books

```
{
    "_id": <Object Id>,
    "author": "Author Name" STRING REQUIRED,
    "genre": "fantasy" STRING REQUIRED,
    "image_url": "https://example-utl.com/image.jpg",
    "summary": "Example book synopsis..." STRING REQUIRED,
    "added_by": "123xyz STRING REQUIRED"
    "reviews": [
        {
            "author": "123xyz" STRING REQUIRED,
            "review": "Example book review..." STRING REQUIRED,
            "rating": INT range(1,5),
        },
        {
            "author": "123xyz" STRING REQUIRED,
            "review": "Example book review..." STRING REQUIRED,
            "rating": INT range(1,5) REQUIRED,
        },
        ...
    ],
    "editors_choice": true BOOLEAN REQUIRED,
    "editors_choice_data": {
        "picked_by": "123xyz" STRING,
        "editors_comments": "editors comments on the book"  STRING
    },
}
```

2. Users

```
{
    "_id": ObjectId("619d4a4c50a386db90b5ad8b"),
    "username": "123xyz" STRING REQUIRED,
    "password": <hashed password> STRING REQUIRED,
}

```

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

The books page displays book preview cards for all books using a one or two column layout depending on user screen size as discussed above.

- Add a Book

When logged in the books page will display a prompt to the user to add a new book at the top of the page. CLicking this will direst the user to the add a book page. See - [Add a book](#add-a-book)

<p align="center">
    <img src="readme-assets\add-book-prompt.PNG" width="500px"/>
</p>

- Search

The search bar at the top of the books page allows the user to sort all books by designating a search term. The page will then display any books that contain matches to the designated term in the 'title', 'author', 'summary' or 'genre' fields.

<p align="center">
    <img src="readme-assets\search.PNG" width="450px"/>
</p>

When a search is submitted a response is given qualifying the number of results and the search term given. The book preview cards for the books matching the search term are displayed bellow this section.

<p align="center">
    <img src="readme-assets\search-results.PNG" width="450px"/>
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

- Selecting to edit a review will direct the user to form identical to the add review form but pre filled with the current review information. The user is free to make any edits they like then re submit the review updating the database.

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

### **Cloning and running locally**

- To clone the repository for this project first navigate to the [Repository main page](https://github.com/ChronoLogic12/bookmarks) and click on the **code** button.

<p align="center">
    <img src="readme-assets\code.PNG" width="500px"/>
</p>

- To clone the repository using HTTPS, select the HTTPS tab under the clone section and click the icon to copy the provided url to the clipboard.

<p align="center">
    <img src="readme-assets\clone-https.png" width="300px"/>
</p>

- Open Git Bash and navigate to the location you would like to store the cloned repository.
- Type `git clone` followed by the url you copied earlier.

```sh
$ git clone https://github.com/ChronoLogic12/bookmarks.git
```

- Press enter to create your cloned repository.
- Open the project in your IDE of choice and install dependencies from the requirements.txt file by running `$ pip3 install -r requirements.txt` in your terminal.
- To run a local development server from Bash:

```sh
    $ pipenv run dev
```

run on http://localhost:5000/home

For more details on cloning repositories click [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

### **Connecting to Mongodb**

To use this application you will need to connect to mongodb (or similar database service).

- Go to [Mongodb](https://www.mongodb.com/) and login/register an account.
- Create a cluster and establish a database for the project.
- Within the database create two clusters; one for 'users' and one for 'books'

For more details on using mongodb click [here](https://docs.atlas.mongodb.com/getting-started/)

Environment variables

- To start create a .gitignore file and add the following filenames to prevent these files from being committed to our repository.

```
env.py
__pycache__/
```

- Create a env.py file in the route directory.
- Import os and set the necessary environment variables as shown bellow.

1. To find your MONGO_URL go to your cluster overview page and select 'Connect'

<p align="center">
    <img src="readme-assets\mongodb-connect.png" width="400px"/>
</p>

2.  Click 'Connect your application'

<p align="center">
    <img src="readme-assets\mongodb-connection-method.png" width="400px"/>
</p>

3. From here copy the connection string provided and update the `<password>` and `<dbname>` sections with the root user password and the name of default database connection respectively.

```py
Import os

os.environ.setdefault("IP", "IP")
os.environ.setdefault("PORT", "PORT")
os.environ.setdefault("SECRET_KEY", "SECRET_KEY")
os.environ.setdefault("MONGO_URI", "MONGO_URI")
os.environ.setdefault("MONGO_DBNAME", "DATABASE NAME")
os.environ.setdefault("FLASK_ENV", "development")
```

### Deploying to Heroku

To deploy this application to heroku first we must make sure to establish a requirements.txt and Procfile as heroku needs these to operate. First type:

```sh
$ pip3 freeze --local > requirements.txt
```

into the terminal to establish your requirements.txt file. Then enter:

```sh
echo web: gunicorn app:app > Procfile
```

to insert the startup commands for heroku into a Procfile.

- Next, go to [Heroku](https://www.heroku.com/) and login/register
- Navigate to your dashboard and select 'New' - 'Create new app'
- Enter a unique application name and select your region then click 'Create app'
- To connect your app and set up automatic deployment, select 'GitHub' under the 'Deployment method' section.
- Select your GitHub profile and the name of the repository containing your code.
- Add your config variables to Heroku by navigating to settings, scrolling down and clicking 'Reveal Config Vars'. Then input the key value pairs from your env.py file
- Return to the deploy tab and select 'Enable Automatic deployment'
- Once the app is deployed you can open the live site by selecting the 'Open app' button at the top right of the page.

---

## Potential Future Features

- Report system: As most of the data displayed on the site is user added (book cover images, book summaries, reviews) a system to allow users to report potentially inappropriate content to admin for review and removal would be an essential addition to future builds.
- User defined book lists: A system to allow users to 'save' books to list such as 'planned to read' or 'favorites' for later viewing could be useful added functionality and encourage more return users.

## Credits

### Services

- [Materialize](https://materializecss.com/) was used throughout site for layout, interactive components, element styling, colours and icons.
- [Google fonts](https://fonts.google.com/) was used to link used fonts.
- [Font Awesome](https://fontawesome.com/) was user for social icons in the site footer.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) micro web framework
- [Heroku](https://www.heroku.com/) application host.
- [Gunicorn](https://gunicorn.org/) wsgi server.
- [Mongodb](https://www.mongodb.com/) non relational database.

### Media

- All brand artwork was created by me with use of Adobe [Photoshop](https://www.adobe.com/uk/products/photoshop.html) and [Illustrator](https://www.adobe.com/uk/products/illustrator.html)
- All images are served to the site [Cloudinary](https://cloudinary.com/console/c-087b7b36d5737750ed37ab5fb60479/getting-started) CDN for improved performance.

### Help and info

- Code Institute learning material - general knowledge.
- [Codecademy](https://www.codecademy.com/learn) - general knowledge.
- [w3schools](https://www.w3schools.com/) - general knowledge.
- [MND Web Docs](https://developer.mozilla.org/en-US/) - general knowledge.
- [Stack Overflow](https://stackoverflow.com/) - debugging.
- Interactive star rating element adapted from [the work of Jordan-Simonds (jexordexan)](https://codepen.io/jexordexan/pen/yyYEJa)
- [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Jinja documentation](https://jinja.palletsprojects.com/en/3.0.x/)
