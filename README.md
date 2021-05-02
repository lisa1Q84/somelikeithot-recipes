# **Readme: MS3 - SOME LIKE IT HOT (Recipe Sharing Website)**



# Table of content:

   [Description](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#description)
-   [User Experience](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#user-experience)
    -   User Stories
    -   Strategy
    -   Scope
    -   Structure
    -   Look
    -   Surface
-   [Technologies](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#technologies)
-   [Testing](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#testing)
-   [Bugs](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#bugs)
-   [Deployment](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#deployment)
-   [Credits](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#credits)

## [](https://github.com/lisa1Q84/somelikeithot-recipes/master/README.md#description)Description

SOME LIKE IT HOT 

This recipe sharing website is intended for spice lovers to explore new recipes and to collect their own recipes.

The newly created live site can be viewed  [here](https://flask-recipe-app-ms3.herokuapp.com/). This site was designed as a project to be submitted for grading in the third milestone project in Full Stack Software Development with the Code Institute.

## [](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#user-experience) User Experience

----------

**USER STORIES & PROJECT GOALS**

----------

	External User Goal: 

1.   Users want to find recipes for spicy food.
    
2.  Users want to easily, intuitively navigate the site.
    
3.  Users want to search and filter the recipes if they are looking for something specific.
    
4.   The users of the website want to make use of CRUD (create, read, update and delete) for their recipes.
    
5.    Users want the site to be visually appealing and well presented.
    

	Project Goals:

1. To build a full-stack site that allows users to manage a common dataset about a particular domain, in this case recipes.
    
2. To create a site that uses HTML, CSS, JavaScript, Python+Flask and MongoDB.
    
3. Creating a website that serves as a platform where people can get inspired for breakfast ideas and where they can share their breakfast recipes.
    
4. To create a site that serves as a platform where people who love spicy food can get inspired for recipe ideas and where they are able to share their own recipes.
    
5. To create an easy to navigate site that makes registering/login easy and that makes use of CRUD (create, read, update and delete) for the users own recipes.
----------

**SCOPE**

----------

Features:

-   Navigation menu – a basic and easily visible navigation menu from materialize that folds on mobile . The name and logo on top on the left is only hidden on the Index page as the banner would repeat the title.

The sections will be:
    
-   Home/Index
	The user will see the banner and the welcome section on the left to learn immediately what this page is about. On the index page the top 9 recipes (with the most views) are displayed.
    
-   All Recipes
	The user can see all recipes entered and filter according to category, spice level and use a search bar to find recipes. 

-   Register/Login
	The user is first lead to a page where he can choose to either register or to login. When clicking register he is lead to the registration page.
    
-  Profile
	After logging in, the user is redirected to his profile page where he can look at all the recipes he has ever added. On the recipe card he can choose to delete the recipe (a modal pops up for confirmation) or to edit it.

- Add recipe / Edit Recipe

	The user can add a recipe in a form with each input field describing below what input is needed. If the user misses something, due to the validation, the input field lights red and asks the user to enter the required text/number/url.
I added a value to the url field so that a user, if they don't have an image, can use the default url.
Clicking the submit button adds the recipe to the database and redirects the user to his profile.
The edit page works the same with the difference that the input fields are already pre-filled.

- Logout
If the user clicks logout on the menu they will  	be redirected to the index page.

----------

**STRUCTURE** 

----------

I am not a very talented designer, therefore I decided to keep the site as simple as possible. 

There is no previous buttons because the user is meant to only move in one direction. If the user is curious what happens if they answers questions differently, they can press start and go back to the beginning. 

The structure of my database is as follows:

RECIPES
**_id**  
**recipe_name**  
**recipe_spicy_scale**  
**category_name**  
**img_url**  
**recipe_serves**  
**prep_time**  
**recipe_ingredients**  
**recipe_method**  
**recipe_inventor**  
**is_vegetarian**  
**is_vegan**  
**views**

CATEGORIES
**_id**
**category_name**

SPICELEVEL
**_id**
**spiciness**

SUBSCRIBERS
**_id**
**email_address**

USERS
**_id**
**username**
**password**




----------

**LOOK**

----------

The website is meant to look friendly and fun, inviting users to browse recipes.

Colours:

-   Red to match the chilli peppers as well as black and white

Typography:

-   Oswald is used on the menu and the headings and Railway is the font for the paragraphs. 

I found the two of them to pair nicely together when trying them together on Google-Fonts.

Effects:

I used the  dropdown-effect buttons and modals from Materialize as well as the reveal cards that "turn around" when clicked on. 

Imagery:

-  For the main site, I created a banner on Canva 
- The recipe images are added by the user. The default image if they don't enter anything has been taken from [here](https://www.pennmedicine.org/updates/blogs/health-and-wellness/2019/april/spicy-foods)


## [](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#technologies)Technologies

-   HTML – Used to create the websites main structures
-   CSS5 – Used to style the components created with HTML 
-   GitPod – Used for writing the code
-   GitHub – Used for hosting the files used for the website.
-   Flask – Used as web framework  to provide libraries, tools and technologies
-   Materialize is used for the design framework.
 -   MongoDB is the fully managed cloud database service used for the project.
-   Heroku is the cloud platform to deploying the app.
-   Jinja is used for templating Python
-   Werkzeug is used for password hashing and authentication and authorisation.
-   Google Fonts – Used for the fonts Oswald and Railway
-   Git – Version control used to track changes, commit and push code to Github.
- Javascript - Was used in order to create interactive elements.
-  Jquery - JavaScript Library used

**Testing Tools**

-   [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/open) 
	-  Used to detect problems and test responsiveness.
-   [Autoprefixer](https://autoprefixer.github.io/)
    -   Autoprefixer is used to parse the CSS and to add vendor prefixes to CSS rules.
-   [W3C Markup Validation Service](https://validator.w3.org/)
    -   The W3C Markup Validation Service is used to check whether there were any errors in the HTML5 code.
-   [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
    -   The W3C CSS validator is used to check whether there were any errors in the CSS3 code.
-   [JShint](https://jshint.com/)
    -   JShint is a JavaScript validator that is used to check whether there were any errors in the JavaScript code.
-   [PEP8](http://pep8online.com/)
    -   The PEP8 validator is used to check whether there were any errors in the Python code.
	
-   [W3 HTML ](https://validator.w3.org/)
	- Validation of HTML
-   [W3 CSS](https://jigsaw.w3.org/css-validator/)
	- Validation of CSS
	
- [Canva](https://www.canva.com/)
	-  Creation of the Banner and Logo 


## [](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#testing)Testing

All testing was documented in a separate filed that can be accessed [here.](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md/master/TESTING.md)

## [](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#bugs)Bugs

Bug: I was unable to find a way to create a uniform size for the images entered by users so that some cards have a different size than others. 

Bug: The validation of the form fields only changes to green when the user clicks on the next input field. 

Bug: 


## [](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#deployment)Deployment

The following steps were taken to deploy the website:

#### Requirements

-   Python3
-   Github account
-   MongoDB account
-   Heroku account

#### [](https://github.com/juanstelling/MS3_breaktasty/blob/master/README.md#clone-the-project)Clone the project

To make a local clone, follow the following steps.

1.  Log in to GitHub and go to the repository.
2.  Click on the green button with the text  **“Code”.**
3.  Click on  **“Open with GitHub Desktop”**  and follow the prompts in the GitHub Desktop Application or follow the instructions from  **[this link](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)**  to see how to clone the repository in other ways.

#### [](https://github.com/juanstelling/MS3_breaktasty/blob/master/README.md#working-with-the-local-copy)Working with the local copy

1.  Install all the requirements: Go to the workspace of your local copy. In the terminal window of your IDE type:  **pip3 install -r requirements.txt**.
2.  Create a database in MongoDB
    -   Signup or login to your MongoDB account.
    -   Create a cluster and a database.
    -   Create five collections in the db:  **categories, recipes, spicelevel, users, subscribers**
    -   Add values for the collection 
3.  Create the environment variables
    
    -   Create a .gitignore file in the root directory of the project.
    -   Add the env.py file in the .gitignore.
    -   Create the file env.py. This will contain all the envornment variables.
    
    ```
    Import os
    os.environ.setdefault("IP", "Added by developer")
    os.environ.setdefault("PORT", "Added by developer")
    os.environ.setdefault("SECRET_KEY", "Added by developer")
    os.environ.setdefault("MONGO_URI", "Added by developer")
    os.environ.setdefault("MONGO_DBNAME", "Added by developer")
    
    ```
    
4.  Run the app: Open your terminal window in your IDE. Type python3 app.py and run the app.

#### [](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#heroku-deployment)Heroku Deployment

1.  Set up local workspace for Heroku
    -   In terminal window of your IDE type:  **pip3 freeze -- local > requirements.txt.**  (The file is needed for Heroku to know which filed to install.)
    -   In termial window of your IDE type:  **python app.py > Procfile**  (The file is needed for Heroku to know which file is needed as entry point.)
2.  Set up Heroku: create a Heroku account and create a new app and select your region.
3.  Deployment method 'Github'
    -   Click on the  **Connect to GitHub**  section in the deploy tab in Heroku.
        -   Search your repository to connect with it.
        -   When your repository appears click on  **connect**  to connect your repository with the Heroku.
    -   Go to the settings app in Heroku and go to  **Config Vars**. Click on  **Reveal Config Vars**.
        -   Enter the variables contained in your env.py file. it is about:  **IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME**
4.  Push the requirements.txt and Procfile to repository.
    
    ```
    $ git add requirements.txt
    $ git commit -m "Add requirements.txt"
    
    $ git add Procfile 
    $ git commit -m "Add Procfile"
    
    ```
    
5.  Automatic deployment: Go to the deploy tab in Heroku and scroll down to  **Automatic deployments**. Click on  **Enable Automatic Deploys**. By  **Manual deploy**  click on  **Deploy Branch**.

Heroku will receive the code from Github and host the app using the required packages. Click on  **Open app**  in the right corner of your Heroku account. The app will open and the live link is available from the address bar.

6.  Happy Coding!


## [](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/README.md#credits)Credits

**Code used**

Parts of the app.py, mainly 
- Register/ Login
- The CRUD functionality 
file were created with the code from Mini Project at the end of the Backend Module from Code Institute.

I learned how to code the view counter through this thread on a python forum:
https://python-forum.io/Thread-How-Do-I-Increment-My-View-Counter-in-Flask

The Error Handlers Code has been taken from the Flask Documentation: https://flask.palletsprojects.com/en/1.1.x/errorhandling/

Navbar, Buttons, Cards, Searchbar and Modals have been taken from https://materializecss.com/


**Content**

Content has been either created by me or by the users entering recipes.

The default recipe image has been taken from 
https://www.pennmedicine.org/updates/blogs/health-and-wellness/2019/april/spicy-foods)



**Acknowledgements**

I would like to thank:

-   Code institute for giving me the chance to learn something entirely new

- Tim from Tutor support for always being friendly

- My new tutor Spencer for taking the time to mentor me and for giving me valuable advice.

- All the amazing people that put tutorials out there, answer questions on forums as well as Slack.


> Written with [StackEdit](https://stackedit.io/).
