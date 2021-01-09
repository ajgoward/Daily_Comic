# About

This is  a fullstack application which allows users too: 
- View and purchase comic books 
- View and purchase graphic novels 
- View and purchase comic merchandise 
- View and purchase comic toys 
As a lifelong comic fan I thought I would do a ecommerce store to refelt my passion for comics 

# UX
### Wireframes 
Please find my wireframes here 

### This website is for:

- Fans of all comic related things 
- Children 
- Adults 
- Gift buyers

### What they want to achieve:

- Browse all products on offer 
- See how much they are saving based to RRP
-	Filter through products to find what they are looking for i.e toys merch marvel etc.
-	Filter products based on price high-low rating high-low
-	Search for products in a search bar 
-	Be able to browse the comic subscription 
-	See the product details 
-	See their products in a shopping cart so they know exactly what they are ordering and spending
-	Be able to make secure online payments 
-	Be able to easily add they delivery address 
-	Save their details for frequent visits
-	Also administrators will want to add additional products 

### How will they achieve it:

-	By making the application mobile first the users can easily see the products across all devices 
-	On each product there will be a RRP and then underneath it will be the product price 
-	The navigation will have drop down menus to filter through the products 
-	On each product page there will be a dropdown to filter through price and rating 
-	On the main navigation bar there will be a search bar 
-	Each product will have there own detail page 
-	Each product will have an add to basket button which will automatically update the price 
-	There will be a shopping cart page which will list each product selected as well as quantity eiwhich they can change 
-	The payments will be handled by STRIPE which is a secure online payment system 
-	On check out the user will be prompted to input there delivery information also there will be a chance to sign in and save the delivery information 
-	There will be a administrators section too add products once administrators are signed in 

### Existing features:

-	Navigation bar so the user can jump to the necessary information 
-	Search bar so users can search the site by typing a query
-	A sign in/sign up page and profile page , for users to save there delivery information 
-	An administration page for administration to add edit and delete products 
-	A payment handler from STRIPE 
-	A shopping cart icon which updates on products added 
-	A quick add to cart button for frequent users 
-	A item detail page for users to see product details 
-	A shopping cart page which lists the items in the cart with a subtotal including/excluding delivery

### Features I would like:

- A subscription based payment system to deliver comics on a mothly basis 

# TESTING 
I have tested this application Accross all devices on google developer tools.  I have also sent this for peer code review on slack,  I also sent it to family and friends to test.  And i recieved alot of positive feedback and fixed any issues highlighted by this.  

I also wrote my own automated tests you will find these in each app in the repository under titles of test-views and test-forms . 

## Interesting bugs

During the course of building this app there was a bug which involved GitHub not reading my environment variables and heroku wasn’t reading them either. After contacting code institute tutor support they couldn’t understand the reason why either so I decided to create a new heroku app which fixed the issue on the heroku side but on the github side I couldn’t fix this issue . 
Also Stripe webhooks kept failing on the heroku app as the webhook key was not getting read on the server so I was unable to create subscriptions as Stripe creates these using webhooks.

# Technologies used 
-	HTML5- the standard language of a website 
-	CSS3- used for custom styling 
-	JAVASCRIPT – for making the website more interactive and responsive 
-	JQUERY - for making the website more interactive and responsive 
-	PYTHON3 – backend language To add things to the database, load the pages  and add the main functionality of the application 
-	DJANGO- the framework used 
-	AWS – used as the media and styling files storage when deployed 
-	BOOTSTRAP4- used as a styling 
-	HEROKU – this is where the application is hosted 
