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

- [Mobile](readme-assets\bookmarks-wireframe-tablet.png)
- [Tablet](readme-assets\bookmarks-wireframe-mobile.png)
- [Desktop](readme-assets\bookmarks-wireframe-desktop.png)

## **Features**

- Navigation

The sites navigation section is located at the top of all pages. This section contains the BookMarks brand name and logo as well as the page navigation controls for larger displays

<p align="center">
    <img src="readme-assets\nav-desktop.PNG" width="1200px"/>
</p>
or an expandable navigation sidebar for these controls for smaller screens. 
<p align="center">
    <img src="readme-assets\nav-mobile.PNG" width="600px"/>
</p>
<p align="center">
    <img src="readme-assets\nav-mobile-sidebar.PNG" width="80px"/>
</p>
Nav controls responsively employ materializes active styling to indicate to the user the current page.

- Footer

The footer section is located at the bottom of all pages and contains a copyright statement and links to facebook, instagram and twitter.

<p align="center">
    <img src="readme-assets\footer.PNG" width="500px"/>
</p>

- Book preview cards/links

Throughout the site book previews are displayed as cards containing the books basic info such as title, author and average rating as well as the books cover art. Preview cards also function as links to that books details page where they can find further details and review for the title. These preview cards are displayed in one or two column grids depending on the users screen size and site section.

<p align="center">
    <img src="readme-assets\book-preview-card.PNG" width="300px"/>
</p>

### Home

- Top rated books

The first section of the sites home page is dedicated to the books with the highest current average ratings. This section displays book previews for the current six highest rated books.

<p align="center">
    <img src="readme-assets\home-top-rated.PNG" width="500px"/>
</p>

- Editors Picks

The editors pick section of the home page contains short write ups on some of the favorite picks of site editors, encouraging users to check out certain titles and engage with the community. Each write up also contains a preview card to direct the user to the books details page.

<p align="center">
    <img src="" width="500px"/>
</p>

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
