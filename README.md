# Recipebook

## Data Centric Development Milestone Project-3

## Description

The Recipebook is an online cookbook, where a user can find recipes or share his/her own recipes. User can create an account 
and has the possibility of add, update or delete his/her own recipes.

# UX

 The target audience of this web-application are food lovers who are either in search of good cooking recipes or they want to store 
 their favourite recipes online and want to share with the rest of the world. The purpose of this web-application 
 is to provide a platform to food lovers so they can share their cooking recipes with other. Besides this the web-application
 owner's goal is to create a cooking recipes database.

 ### User Stories

 1. As a user, I want to see a list / catalogue of recipes.
 2. As a user, I want to search for recipes so that I can find easily and quickly.
 3. As a user, I want to be able to create an account.
 4. As a user, I want to be able to login to my account.
 5. AS a user, I want to store/add  and share my recipes online with others.
 6. As a user, I want to see a list of my own recipes.
 7. As a user, I want to see the details of the recipe.
 8. As a user, I want to update my existing recipes. 
 9. As a user, I want to delete my existing recipes.
 10. As a user, I want to end the session.

 ## Design

 The website design is simple and responsive which allows the user to perform easily theCRUD functionality. The design 
 inspiration is taken from the **Code Institute's Task Manager Mini Project**.

#### Fonts

1. Google fonts **Krona One** is used in navbar and footer. 
2. Where as **Balsamiq Sans** is used in the body. 

#### Attribute

1. The target_blank value is given to the social links in the footer so that they will open in a new tab / window on click.
2. The required attribute is used in the search field, login form, sign up form, add recipe form and edit recipe form so that user 
fill in all the fiels before performing the respective action.

#### Hover Effect

1. Slight change in background color and default cursor changes to hand pointer happens when a user hover over a button.
2. Default cursor changes to hand pointer when a user hover over logo and social links.

## Wireframes

I used [Balsamiq](https://balsamiq.com/) to create wireframes which will provide an overview of how the website will look 
like on different mobile screen size.

- [Link to Wireframes](https://balsamiq.cloud/sfyoi6/p2i2t4h/r2278) 
- [Wireframes in PDF](static/wireframes/recipebook.pdf)

## Database Schema

NoSql MONGODB is used to store data at the backend. Database schema is designed for various collections before buiding the project. 
- [Collections Schema in PDF](static/collections/collections.pdf)

## Features
### Existing Features

- **Navbar/Side** navbar - Navbar and side navbar links vary, if user is logged in or not. If user is not logged in then Home,
All Recipes and Log In buttons are shown. Where as after login user can see Home, All Recipes, Add Recipes, My Recipes and Logout.
At login and signup pages all navbar/sidenavbar links will disappear except the logo Recipebook. 
- **All recipes** - When a user land on the home page and user has not logged in yet, user can see the list of all recipes in the database. User can also 
see the list of all recipes once the user has logged in.
- **Search** - User can search for any recipe in the database for being login or without login in the website.
- **Register** - User can easily register if does not have an account as signup form is very simple. Signup form
form has two fields username and password. It is required that a username must be minimum three character long and password 
should be minimum 6 character long. It is not possible to have two accounts with the same
name as I have included this feature to check whether the user name already exist or not. If username already exist then user will 
be notified that username already exist with a flash message.
- **Login** - If username password does not match user will get a message that invalid username/password.
- **Flash Messages** - Flash Messages are shown to the user to keep user inform of user interactivity. Flash messages for 
login and signup will stay untill pages is refreshed. Where as flash messages on recipe addition, deletion and update will 
disappear after 4 sec.
- **Logout** - Logout allows a user to end the session and return to the home page.
- **View** - It allows a user in session to see the details of a recipe.
- **Add Recipe** - It allows a user to add a new recipe in the database. All the fields are required in add recipe form. After 
adding the recipe user will get a flash message that recipe is added successfully and will disappear after 3 sec. After this 
user will be redirected to the all recipes page.
- **Edit/Delete Recipe** - When user is logged in user can edit or delete a recipe which he owns.
- **Edit/Delete Buttons**- Edit/Delete buttons will appear only if the user is the owner of that particular recipe.
- **Cancel Button** - Cancel button is provied in edit recipe page for user's convenience to cancel the operation which will 
redirect user back to that particular recipe that user was viewing.
- **Deletion Confirmation**- If a user click on delete button, then a modal will pop up to confirm if user is sure to delete the recipe or not.
- **My Recipe** - If user want to see his own added recipes then **My Recipe** function will  display the list of user's own recipe.

### Features Left to Implement

- **Pagination** - At the moment **All Recipes** and **My Recipes** pages just list all the recipes on the same page. But in 
in future I would like to add pagination so that a few number of recipes can be shown on the page and remain on page 2 or 
page 3 etc.
- **Graphs** - I would like add graphs in future to give a statistical overview of the recipes.
- **Reset Password** - A reset password feature will be added in the future.
- **Recover Password** - Password recovery feature if forgotten will also be added in future.
- **Recipe Image** - To make recipe visually appealing, recipe image addition option will also be added.
- **Sort** - Sorting recipes accending or decending order feature will also be added in future.

## Technologies Used

- **HTML5**
- **CSS3** - CSS3 is used for custome styling the elements. 
- **JavaScript** - JavaScript function is used to overcome the bug in the datepicker.
- **JQuery** - Jquery is used to initialize the Materialize components.
- **[Materialize Framework](https://materializecss.com/)** - Materialize front-end framework is used to make website responsive.
- **[Python](https://www.python.org/)** - Python is used as the back-end programming language.
- **[Flask](https://flask.palletsprojects.com/en/1.1.x/)** - Python microframework Flask is used to create this project.
- **[Jinja](https://jinja.palletsprojects.com/en/2.11.x/)** - Jinja templating language is used with Flask in the HTML code.
- **[Balsamiq](https://balsamiq.com/)** - Balsamiq is used to create wireframes for the project.
- **[PyMongo](https://pymongo.readthedocs.io/en/stable/)** -  It is a Python distribution that contains tools to work with MongoDB.
- **[MongoDB](https://www.mongodb.com/)** - It is a NoSql database that is use to store data at the backend.
- **[Google Fonts](https://fonts.google.com/)** - Google fonts *Balsamiq Sans* and *Krona One* are used in the project.
- **[Git & Github](https://github.com/)** - Used for version control.
- **[Git & Github](https://www.heroku.com/#)** - It is used as hosting platform to deploy the project.

## Testing

### User Stories
User stories from the UX section were tested to see if they all work as intended. 
- *As a user, I want to see a list / catalogue of recipes.*
1. Go to the **Home** Page.
2. Click on **All Recipes** button in the navbar or on **All Recipes** beside image slider.
3. A list of recipes will be displayed.
- *As a user, I want to search for recipes so that I can find easily and quickly.*
1. Go to the **Home** Page
2. Go to the search bar beside the image slider and write any key word to search for the recipe.
3. Click on the **Search** button.
4. A list of recipes will be displayed.
5. If no recipe found then a **No Recipe Found** will be displayed.
- *As a user, I want to be able to create an account.*
1. Go to the **Home** Page.
2. Click on **log In** button AND then **Sign Up** button.
3. Fill in username, password and click on **Sign Up** button.
4. If username does not exist already then a user account will be created and user will be redirected to **Home** page.
5. If user already exist then user will get a message that **User already exists.**
- *As a user, I want to be able to login to my account.*
1. Go to the **Home** Page.
2. Click on **log In** button.
3. Fill in username, password and click on **Log In** button.
4. If username and password are correct then user will be redirected to the **Home** Page.
5. If username and password does not match then **Invalid username/password** message will be displayed.
- *AS a user, I want to store/add  and share my recipes online with others.*
1. Go to the **Home** Page.
2. Click on **log In** button.
3. Fill in username, password and **Log In**.
4. Click on **Add Recipe** and fill out the **Add Recipe** form. All fields are required to fill in.
5.  Click on **Add Recipe** button. A confirmation message **Recipe successfully Added** will be displayed and user will 
be redirected to the list of all recipes.
- *As a user, I want to see a list of my own recipes.*
1. Go to the **Home** Page.
2. Click on **log In** button.
3. Fill in username, password and **Log In**.
4. Click on **My Recipes** button.
5. User will be redirected to list of user's own recipes. 
- *As a user, I want to see the details of the recipe.*
1. Find the recipe either by using **Search bar** or from list **All Recipes** or from list of **My Recipes**.
2. Click on the **View** button.
3. Recipe details will be shown.
- *As a user, I want to update my existing recipes.*
1. Go to the **Home** Page.
2. Click on **log In** button.
3. Fill in username, password and **Log In**.
4. Click on **My Recipes** button and choose the recipe form the list to update.(**User can only update or delete his own recipes**)
5. Click on the **View** button and the recipe details will be displayed.
6. Click on the **Edit** button and recipe details will open in a editable form.
7. Edit the required field and click on update. A conformation message **Recipe successfully updated** will be displayed.
8. If user want to cancel the update and return to the previous page then click on **Cancel** button.
- *As a user, I want to delete my existing recipes.*
1. Go to the **Home** Page.
2. Click on **log In** button.
3. Fill in username, password and **Log In**.
4. Click on **My Recipes** button and choose the recipe form the list to update.(**User can only update or delete his own recipes**)
5. Click on the **View** button and the recipe details will be displayed.
6. Click on the **Delete** button and a pop up window will appear to confirm the deletion.
7. Click **yes** to confirm and a confirmation message **Recipe successfully deleted** will be displayed.
8. Click **No** to get back to same page agian.
- *As a user, I want to end the session.*
1. Click on the **Logout** button to end the session.









