# SOME LIKE IT HOT MS3 - Testing Details

## **How did I test?**

[W3C Markup Validation Service](https://validator.w3.org/)

-   W3C Markup Validation Service has been used for the testing of the  **HTML**  and  **2 errors**  were found. I could not correct either of them as one was the duplication of the email tag (because on small devices I showed the newsletter signup div in a different place. The other error was caused by the style tag inside the body tag due to me using it to hide the logo on the index page. I tried moving it to the top but that caused several errors. As it is working and I had time constraints I kept it where it is. It would likely be possible to hide the logo on the index page with a function in app.py.
 The result can be seen here  [\[HTML Test\]](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/images/html_test.png)

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

-   W3C CSS Validation service has been used to check the  **CSS**  of the project and  **2 errors**  were found. One of them is in the materialize css and I am unable to access that. The other error tells me the max widht otion in the media queries is deprecated. However, it works perfect for me and removing it had a negative impact so I added it back.
The result can be seen here.  [\[CSS Test\]](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/images/css_test.png) 

[JS HINT](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/images/jshint.png)

- JSHint is a static code analysis tool used in software development for checking if JavaScript source code complies with coding rules. It helped me discover that I had not closed a bracket disabling my dropdown button. 

[Python validator | PEP8](http://pep8online.com/):
 - No errors found, see [here](https://github.com/lisa1Q84/somelikeithot-recipes/blob/master/images/PEP8_test.png)


The Project was tested for Browser compatibility on multiple versions of IE, Chrome and Safari

It was found that "the CSS `transform:` property is not supported by some older browsers" and "The `display: flex` CSS property does not work correctly in some browsers."

Other than that it was suggested to make improvements in the area of Search Engine Optimisation by adding more links and headlines and offering a HTML site map. 


**Client Stories Testing**

Testing client stories from UX part of README.md

1.   Users want to find recipes for spicy food.

		-  Recipes easily accessible on index page (most viewed) and on the recipes page that can always be navigated to on the menu.
    
2.  Users want to easily, intuitively navigate the site.

    -  Site easy to navigate
    -  Forms, buttons and the quote generator are functional. 
    - I have tested the website across multiple screen sizes and have found no issues thus far.
    - Only problem: to get back from the single recipe site to the 'recipes' site, where they may have filtered the results, the user has to use the 'back' button. Otherwise he can click on Recipes on the menu and filter again.

3. Users want to search and filter the recipes if they are looking for something specific.

	- Filter is working well and so does the search bar. In the future I should try to implement more filters or simultaneous filters.
    
4. The users of the website want to make use of CRUD (create, read, update and delete) for their recipes.

	- Users can create, read, edit and delete their recipes and read other users recipes.

5.   Users want the site to be visually appealing and well presented.
    
		- The site is very simply designed in red, black and white. The recipe cards from Materialize look well but sometimes due to the size of the image can be bigger than others. 
    

**Manual Testing of all elements and functionality of every page.**

-   **Navigation Bar**
    
    1.  Check if the  **navbar**  is situated always on top and transforms into a collapsible menu when on m and s screens.

-   **Sections**

    1.   Click The  **MENU LINKS** and check if it brings the user to the next section.
    2.  Fill the  **Login/Register**  forms and check if it works and if the user gets redirected if the username already exists or the login data is wrong.
    3.  Visit the  **Profile **, and check if the user created recipes appear and if they can be edited and deleted.
    4.  Try to  **Add Recipe**, check if the validation works and if recipes are successfully added to the DB.
    5.  Check if the  **Logout** works and if the user gets redirected to the register/login page.
    6.  Click the  **Recipe Cards**,  and see if they direct the user to the recipe site of the correct recipe.
    7.  Try signing up for **Email Newsletter**, check if the form validation works.

  
-   **Content**
    
    1.  Check the alignment of content inside the recipes.
    2.  Check spelling by online spelling and grammar checker  [Grammarly.com](https://app.grammarly.com/). Few spelling mistakes were found, which were corrected.
    

**Project Barrier**

-   At the end of April there was an issue with the Preview function on Gitpod so that I had to add, commit and push changes to Heroku to see if functionalities work. This took quite some time. 

-   I had several problems with my deployment to Heroku. This was caused by the automatic alignment extension preinstalled in my template that put a line within my env.y file containing the URI key on another line, making it dysfunctional. After contacting student support I was able to find and resolve the error. 

- Due to poor time management from my side I was unable to add more filter options and a rating function which would have been a great addition to the page. Also another function I want to add is the possibility for users to make a list with their favorite recipes. I will hopefully be able to add it in the future. 

**Bug report**

-  While testing my site with the Google Developer Tools I came across a strange error I was not able to resolve. Sometimes when checking the site on smaller devices, a horizontal scroll bar appeared on the bottom of the page. When I tried to reload the page and later to reproduce this error, there was suddenly no scrollbar and the pages had no scrollbar problems on smaller devices. 



