# 431 Web Programming Exercise
## Context
This website is for fictional the Nittany University Hospital, where a hospital staff may enter and delete patient names in its database. I've 
created 3 webpages with HTML and use Flask to implement the website functionality. 

## Features
There are five files that make up the website design:
1. app.py: provides functionality to the website using Flask. This includes page redirection, form submission, and database queries. 
Incorporated is SQLite, which was used to set up the database. Important functions:
  a. insert(): directs to the insert.html page along with database information.
  b. delete(): directs to the delete.html page along with database information.
  c. valid_name(): creates a database table if none exists. inserts a generated PID and a given first name/last name into the database and returns
  the database.
  d. name(): directs to the insert.hmtl page with an updated database based on first_name and last_name received from html form.
  e. remove(): deletes an entry from the database based on a first_name and last_name received from html form. returns the delete.html page
  with updated database.

2. homepage.html: html file to create the homepage. Redirects to the other two html pages.
3. style.css: custom css file to enhance homepage visuals.
4. insert.html: html file to create insert page. Here, a user can insert a patient's first and last name. Submitting the form will insert
the name into the users database.

## Organization
app.py is organized by function. the most important functions are:
  a. homepage(): which directs to the homepage html
  b. insert(): which directs to the insert html
  c. delete(): which directs to the delete html
The homepage is organized with a simple title banner, simple description, and a dropdown menu to take the user to one of two html pages.
Insert.html and delete.html are organized with a submit form, which adds (deletes) an entry to (from) the database, which is displayed on the page.

## Instructions
style.css should be placed in the static folder of the Pycharm project.
delete.html, homepage.html, insert.html should be placed in the templates folder of the Pycharm project.
app.py should be placed in the Pycharm project.
To run: run app.py in the Pycharm project. Click on the specified port in the Run environment to open webpage.

