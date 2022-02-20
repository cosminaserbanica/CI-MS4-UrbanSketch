![UrbanSKetch Mockup Images](/media/mockup.PNG) 

[View Live Site here](https://urbansketch.herokuapp.com) 

------
### Table of contents
- [Project Overview](#project-overview)
  * [Project Description](#project-description)
  * [Project Requirements](#project-requirements)
    + [Main Technologies](#main-technologies)
    + [Mandatory Requirements](#mandatory-requirements)
- [UX](#ux)
  * [Strategy](#strategy)
  * [User Stories](#user-stories)
- [Scope](#scope)
  * [Features](#features)
    + [Implemented Features](#implemented-features)
    + [Future Features](#future-features)
  * [Skeleton](#skeleton)
  * [Surface](#surface)
    + [Color Scheme](#color-scheme)
- [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks, Libraries, Programs & Platforms Used:](#frameworks--libraries--programs---platforms-used-)
- [Bugs & Fixes](#bugs---fixes)
- [Deployment](#deployment)
  * [Deployment Steps](#deployment-steps)
  * [Project and Repository Creation](#project-and-repository-creation)
    + [Deployment Steps](#deployment-steps-1)
    + [Connect Heroku app to Github repository](#connect-heroku-app-to-github-repository)
    + [Add Heroku Postgres Database](#add-heroku-postgres-database)
    + [Setting up environment variables](#setting-up-environment-variables)
    + [Setting up the AWS s3 bucket](#setting-up-the-aws-s3-bucket)
    + [AWS IAM (Identity and Access Management) setup](#aws-iam--identity-and-access-management--setup)
    + [Connecting Heroku to AWS S3](#connecting-heroku-to-aws-s3)
    + [Enable automatic deployment:](#enable-automatic-deployment-)
  * [How to Fork the repository](#how-to-fork-the-repository)
  * [Making a Local Clone](#making-a-local-clone)
- [Testing](#testing)
  * [Code Validity](#code-validity)
  * [User registration tested](#user-registration-tested)
  * [User Profile tested](#user-profile-tested)
  * [Checkout process tested](#checkout-process-tested)
  * [Testing User Stories](#testing-user-stories)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)
------
# Project Overview 
___ 
## Project Description   
**Code Institute: Full Stack Frameworks with Django - Milestone 4 Project**   
   
The Milestone 4 project assignment is to build a full-stack application based around business logic used to control a centrally-owned dataset.  To set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product. I have the option to choose from one of the following two scenarios or to come up with my own idea:   
. Build a ﬁtness subscription application     
. Build a site to sell your graphic design services   
    
I have decided to create an eCommerce application for a fictional business called <strong>UrbanSketch</strong>. The business is a store that sells graffiti related products, such as spray cans, markers, caps and safety equipment.
   
## Project Requirements   
 
### Main Technologies   
. HTML, CSS, JavaScript, Python+Django    
  
. Relational database (recommending MySQL or Postgres)  
  
. Stripe payments    
  
. Additional libraries and APIs

### Mandatory Requirements       
1. Django Full Stack Project: Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain.   
2. Multiple Apps: The project must be a brand new Django project, composed of multiple apps (an app for each potentially reusable component in your project).   
3. Data Modeling: Put some effort into designing a relational database schema well-suited for your domain. Make sure to put some thought into the relationships between entities. Create at least 2 custom django models beyond the examples shown on the course (changing the field names of the miniproject models is not customisation)   
4. User Authentication: The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. e.g., a user would have to register to persist their shopping cart between sessions (otherwise it would be lost).    
5. User Interaction: Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).   
6. Use of Stripe: At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout or single payments, or donations, etc. After paying successfully, the user would then gain access to additional functionality/content on the site. Note that for this project you should use Stripe's test functionality, rather than actual live payments.   
7. Structure and Navigation: Incorporate a main navigation menu and structured layout (you might want to use Bootstrap to accomplish this).   
8. Use of JavaScript: The frontend should contain some JavaScript logic you have written to enhance the user experience.   
9. Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.   
10. Version Control: Use Git & GitHub for version control.   
11. Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.   
12. Deployment: Deploy the final version of your code to a hosting platform such as Heroku.    
13. Security: Make sure to not include any passwords or secret keys in the project repository. Make sure to turn off the Django DEBUG mode, which could expose secrets.   
        
# UX
___
## Strategy

* **Project Goals**
    * To create a fully functioning eCommerce site for UrbanSketch, an online business that sells graffiti supplies.  
    * To allow users to easily view, filter and search for any item available from this shop.  
    * To allow users to make a safe & secure purchase as conveniently as possible.  
    * To allow users to create a user profile to keep track of their order history, add items to their wishlist for a later order and to speed up the purchase process for future purchases.  

* **Business Goals**   
    * To offer their existing customers an alternative to instore shopping as an added convenience.  
    * To have a clean, fresh, modern, professional looking website that can be used as a marketing tool to highlight their range of products to potential new customers.
    * To increase their sales by reaching new customers from outside their immediate physical location.

* **Target audience**
    * The target audience are graffiti artists from the UK and not only.

## User Stories

* **As a first time user I want to be able to:**  

    * Clearly understand the purpose of the website.  
    * Easily navigate around the website. 
    * View all the products the website is selling. 
    * Find products by category. 
    * Filter products by price or alphabetical order.
    * Search for a specific product. 
    * View detailed information about each individual products on a separate page.
    * View my customer reviews of a particular product.  
    * Choose the colour, change the quantity and add a product to a shopping bag.
    * View a full list of items within the shopping bag with a breakdown of the individual costs.
    * View, update & remove products within my shopping bag. 
    * Easily see in the Navbar the current total of any items within the shopping basket.  
    * Securely checkout and purchase the products within my shopping basket. 
    * Receive an order confirmation on-screen and by email upon completion of my purchase.
    * Register and create a user profile.   
    * Contact the stores owners on social media if I have a query.

   
* **As a returning user I want to be able to:**  
    * Login and out of the website with ease. 
    * View my user profile. 
    * Save default delivery details in order to speed up future purchases.   
    * Update my default delivery details.  
    * View my order history.
    * Add products to a wishlist so I can purchase them at a later date.  
    * Write reviews for products I have used for other users to view. 
  
* **As the site owner I want:**
    * Customers to be able to view the full list of products available for purchase.  
    * Customers to be able to filter products by category, price or alphabetical order.  
    * Customers to be able to select and purchase products as quick & easily as possible.  
    * Customers to be able to add, edit, update or delete products within their shopping basket.
    * Customers to be able to read product reviews prior to making a purchase.  
    * Customers to be able to write product reviews after making a purchase. 
    * To be able to maintain & update the website via an Admin panel.  
    * To be able to add, edit, update or delete products from the website.  
    * To be able to add, edit, update or delete blog posts from the website.  
  

[:top:](#UrbanSketch)
