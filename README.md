## Table of Contents
1. [**About**](#about)
2. [**UX**](#ux)
3. [**Existing Features**](#existing-features)
4. [**Database Schema**](#database-schema)
5. [**Testing**](#testing)
6. [**Deployment**](#deployment)
7. [**Credits**](#credits)



# About

This is  a fullstack application which allows users too: 
- View and purchase comic books 
- View and purchase graphic novels 
- View and purchase comic merchandise 
- View and purchase comic toys 
As a lifelong comic fan I thought I would do a ecommerce store to refelt my passion for comics 


# UX
### Wireframes 
Please find my wireframes [here](wireframes/daiiycomic.pdf)

### This website is for:

- Fans of all comic related things 
- Children 
- Adults 
- Gift buyers

### What they want to achieve:

- Browse all products on offer 
- See how much they are saving based to RRP
-	Filter through products to find what they are looking for i.e toys merch marvel etc.
-	Filter products based on price high-low 
-	Search for products in a search bar 
-	See the product details 
-	See their products in a shopping cart so they know exactly what they are ordering and spending
-	Be able to make secure online payments 
-	Be able to easily add they delivery address 
-	Save their details for frequent visits
-  Be able to adjust the quantity in the basket
-  Be able to remove items from the basket
-   Add their own reviews on products and also see other reviews to make an informed decision on whether they want to purchase the product
-   Also to be able to filter reviews from date and high/low
-  Have their own profile in which they can see past orders and update delivery information
-	Also administrators will want to add/edit/delete products 

### How will they achieve it:

-	By making the application mobile first the users can easily see the products across all devices 
-	On each product there will be a RRP and then underneath it will be the product price 
-	The navigation will have drop down menus to filter through the products 
-	On each product page there will be a dropdown to filter through price 
-	On the main navigation bar there will be a search bar 
-	Each product will have there own detail page 
-	Each product will have an add to basket button which will automatically update the price 
-	There will be a shopping cart page which will list each product selected as well as quantity eiwhich they can change 
-	The payments will be handled by STRIPE which is a secure online payment system 
-	On check out the user will be prompted to input there delivery information also there will be a chance to sign in and save the delivery information
-   On each item detail page there will be a section to view reviews and a form to add reviews
-   On each product item detail page there will be a dropdown to filter through date-new/old and rating-high/low
-	There will be a administrators section too add products once administrators are signed in 

# Existing features:

-	Navigation bar so the user can jump to the necessary information 
-	Search bar so users can search the site by typing a query
-	A sign in/sign up page and profile page , for users to save there delivery information
-   A drop down box to filter items by price
-	An administration page for administration to add edit and delete products 
-	A payment handler from STRIPE 
-	A shopping cart icon which updates on products added 
-	A quick add to cart button for frequent users 
-	A item detail page for users to see product details 
-	A shopping cart page which lists the items in the cart with a subtotal including/excluding delivery
-   A review section in which users can see reviews on each product and there is also a average review score on each page
-   A drop down box to filter items by date-new/old and rating-high/low

### Features I would like:

- A subscription based payment system to deliver comics on a monthly basis

# Database Schema

Please find the database Schema that I used [here](database_schema/schema.pdf)

# TESTING 


## I Tested each user story as follows:

### "Browse all products on offer" and "See how much they are saving based to RRP"
1. Load webpage
2. click all products
3. see all products and sections for prices 

![browse_products](screenshots/user1.png)

![browse_products](screenshots/user11.png)

### "Filter through products to find what they are looking for i.e toys merch marvel etc." 
1. Load webpage
2. click all products
3. see all products 
4. click navbar links to filter 

![filter_products](screenshots/user2.png)

### "Filter products based on price high-low" 
1. Load webpage
2. click all products 
3. see all products 
4. click dropdown to filter 

![filter_products](screenshots/user3.png)

### "Search for products in a search bar" 
1. Load webpage
2. click search icon
3. type a query into the search bar  

![search_products](screenshots/user4.png)

![search_products](screenshots/user41.png)

![search_products](screenshots/user42.png)

### "See the product details" 
1. Load webpage
2. click on a product
3. see all product details 

![product_details](screenshots/user5.png)

### "See their products in a shopping cart so they know exactly what they are ordering and spending" 
1. Load webpage
2. add a few items to the shopping cart
3. click the basket icon
4. see the basket with a total.

![shopping_cart](screenshots/user6.png)

![shopping_cart](screenshots/user61.png)

### "Be able to make secure online payments"/"Be able to easily add they delivery address"/"Save their details for frequent visits"
1. Load webpage
2. add a few items to the shopping cart
3. click the basket icon
4. see the basket with a total
5. click secure checkout
6. page loads form with delivery details/ payment and a option to create an account to save information

![checkout](screenshots/user7.png)

### "Be able to adjust the quantity in the basket"/"Be able to remove items from the basket"
1. Load webpage
2. add a few items to the shopping cart
3. click the basket icon
4. see the basket with a total
5. chances to update quantity with a selector and button to update
6. chance to delete by clicking the delete button

![shopping_cart](screenshots/user8.png)

![shopping_cart](screenshots/user81.png)

![shopping_cart](screenshots/user82.png)

### "Add their own reviews on products and also see other reviews to make an informed decision on whether they want to purchase the product"
1. Load webpage
2. Click a product to see item details
3. scroll to reviews 
4. see reviews listed and if not a message prompting to write a review
5. if writing a review click add review button
6. see form to write review
7. click add review
8. see message and review added

![review](screenshots/user9.png)

![review](screenshots/user91.png)

![review](screenshots/user92.png)

### "Also to be able to filter reviews from date and high/low"
1. Load webpage
2. Click a product to see item details
3. scroll to reviews 
4. see reviews listed and if not a message prompting to write a review
5. click dropdown to filter reviews


![review](screenshots/user9.png)

### "Have their own profile in which they can see past orders and update delivery information" 
1. Load webpage
2. Click profile navlink 
3. register if not already done so ( go to number 6 )
4. confirm email
5. sign in
6. see profile

![profile](screenshots/user10.png)

![profile](screenshots/user101.png)

![profile](screenshots/user102.png)

![profile](screenshots/user103.png)

![profile](screenshots/user104.png)

![profile](screenshots/user105.png)

### "Also administrators will want to add products " 
1. Load webpage
2. Click profile navlink 
3. login as admin
4. click profile navlink and click product management
5. form will load to add products

![admin](screenshots/user111.png)

### "Also administrators will want to edit products " 
1. Load webpage
2. Click profile navlink 
3. login as admin
4. click edit button on a chosen product
5. form will load to edit product

![admin](screenshots/user12.png)

![admin](screenshots/user121.png)

### "Also administrators will want to delete products " 
1. Load webpage
2. Click profile navlink 
3. login as admin
4. click delete button on a chosen product
5. product will be deleted


## Additional testing 

I have tested this application Accross all devices on google developer tools.  I have also sent this for peer code review on slack,  I also sent it to family and friends to test.  And i recieved alot of positive feedback and fixed any issues highlighted by this.  

I also wrote my own automated tests you will find these in each app in the repository under titles of test-views and test-forms .

I have also passed all HTML and CSS code into the w3c validator and it all passed 

I have also followed the PEP8 guidelines for writing my PYTHON3 code.

I passed my JAVASCRIPT and JQUERY through validators with no isssues also

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


# Deployment

Here is how I deployed my app:

## APP INITIAL SET UP
1.	First I created a Heroku login [here](https://id.heroku.com/login)  
2.	Then I created a new app with a unique name and chose the region I am in 
3.	Now with the app created I clicked the tab RESOURCES and searched for Postgres and Chose the hobby version and now that gives you a secret key in the settings tabs under the reveal config vars. The secret key is under DATABASE_URL
## DATABASE SET UP
4.	Now Back to the Django application. 
5.	Run
``` python
 pip3 install dj_database_url 
 pip3 install psycopg2-binary
 ```
6.	Then freeze the requirements by running
``` python
pip3 freeze > requirements.txt
 ``` 
7.	Next go to settings.py and import dj_database_url at the top 
8.	Then go to databases and comment out the default settings and type
9. 
``` python
DATABASES = { 
    ‘default’: dj_database_url_parse(*add your DATABASE URL HERE*)
    } 
```
10.	Then run the command below in the terminal this will initialise a new database on the Postgres 
``` python 
python3 manage.py migrate
```
11.	With that all set up it is worth adding a superuser to login with by running 
``` python
python3 manage.py createsuperuser 
```
12.	Now uncomment the default database settings and wrap this in a IF ELSE statement 

![database](screenshots/database.png)

## FINAL DEPLOYING STEPS
13.	Now you need to run the code below and freeze that into the requirements as of step 6
``` python
pip3 install gunicorn 
```
14.	Create a Procfile and type  
``` python
web: gunicorn*your app name*.wsgi:application
```
15.	Now if you want to use AWS to collect all static files you need to diable them in heroku under the config vars by adding DISABLE_COLLECT_STATIC = 1
16.	Also go to a django secret key generator and add a secret key to your config vars
17.	Back to settings.py now and in allowedhosts put your app name in there and add localhost so gitpod works too
18.	Now in the command line run 
``` python
Heroku login
```
19.	use “git init “to initialise and new repository 
20.	run the command “git remote add” and the app URL which can be found on the Heroku dashboard
21.	Then git add , git commit -m “your message here”
22.	Then run git push Heroku master
23.	This will now deploy your app without any static files
## Setting up a AWS S3 bucket
1.	First head over to [Amazon Web Services (AWS) - Cloud Computing Services](https://aws.amazon.com/) and create AWS account
2.	Log in and search for s3 and create a new bucket 
3.	Select the region closer to you and uncheck block all public access
4.	Open your new bucket and turn on static website hosting which is under the properties tab
5.	For the index and error document just fill in some default values as you wont be needing them and click save
6.	On the permissions tab paste in your CORS configuration 
7.	Next go the bucket policy tab and select policy generator to create a security policy fo the bucket
8.	The policy type will be the s3 bucket policy
9.	And you will want to allow all principals by using the * 
10.	And the action will be GET object
11.	Now copy and paste your ARN from your bucket policy tab and click add statement then generate policy
12.	Copy and paste this into the bucket policy editor and add /* to the end of the recourse key and click save
13.	Now go to the permissions tab and under public access tick the box that says everyone and tick list objects
## Setting up IAM
1.	Go back to the services menu and search iam
2.	Click groups and create a new group which your own name
3.	Keep clicking next and create a group
4.	Now create a policy by clicking policy and create policy
5.	Go to the JSON tab and select import managed policy
6.	Search for s3 and import the s3 full access policy
7.	And now under resource you want to paste in the ARN from the bucket you created twice as one is for the bucket itself and then the next add /* which adds another rule for all files and folders in the bucket 
8.	Now click review policy give it a name and description and click create policy 
9.	Now attach the policy to the group you created under the tabs permissions
10.	Now to the users page , add a new user
11.	 And give them programmatic access click next
12.	 Now add that user to your newly created group
13.	 Click through to the end and click create user 
14.	 Download and save the CSV file and make sure you keep it as this is the only way you will be able to get your secret access key
## Connect S3 to Django
1.	Install two packages boto3 and django-storages
2.	Freeze them into the requirements file
3.	Add storages to the installed apps in settings
4.	Now add these settings to your settings file
5.	ADD your AWS keys to the Heroku config vars and add USE_AWS=True
6.	Also remove dissabke_collect_static 
7.	Create a file in gitpod called custom_storages
8.	Add add this 

![aws](screenshots/aws.png)

9.	Now git add , git commit , and git push (make sure you have automatic deployment turned on in Heroku)
10.	 Now all Your static files should be hosted to your site
## Adding Images to S3
1.	Go to S3 and create a new folder called media
2.	Inside that click upload , Add files and then select all of your images, Click next
3.	And under manage public permissions select grant public read accesss to these objects 
4.	Click through the rest and then click upload 

# Credits

I would like to thank Code Institue for all the course material to help me create this web application
Also I would like to thank tutor support with the help they gave me when I ran into bugs

I recieved my hero images from [usplash](https://unsplash.com/)
And all the information and pictures for all the products from my favourite comic store [forbidden planet](https://forbiddenplanet.com/)

