# Quickparcel- decentralizing Africa's supply chain system
![header](/images/header.png)
>  At Quickparcel , we create opportunities with all communities with vechiles to participate in making the movement of goods reliable and cheaper for all. 


> [Live demo](https://communitydelivery.herokuapp.com/). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information

COVID-19 has laid bare the vulnerability of the supply chain model that has dominated the way African firms have organised their production. In this model firms rely on multiple suppliers, many of whom are located far away (mostly in China).

With goods stuck at factories and ports around the world and shortages emerging, the pandemic disrupted the supply of most essentials. It also exposed the weakness of global interdependencies. Foremost among these were of course the essential medical devices needed to save people’s lives. Shortages were apparent also in many food items, consumer electronics and other necessities.

With this dependency on centralized  supply chain structures , it has has been hard  for the layman to participate and small business  have contiunued to have challenges estabilishing healthy relationships with their customers. That is what  Quickparcel addresses by decentralizing the suppluy management chain allowing the community  to offer delivery services for different businesses. 

Quickparcel creates jobs while also enabling businesses capture the value from scale.  




## Technologies Used

### 1. Backend Dependencies
Our tech stack includes the following:
- Python3 - version 3.8
- Django - version 3.1.3
- Sqlite (Database)
- Check the [Requirements.txt](./requirements.txt) for other dependencies. You should be careful when changing any  package versions as this  can break the application. 

### 2. Frontend Dependencies
Our tech stack includes the following:
- Bootstrap -version 4.0.0
- Javascript-jquery
- HTML
- CSS
- Jinja2


## Features

Ready features:

#### Customer - Web App
- Authentication with Email/Facebook
- Send welcome emails automatically
- Upload Profile Photo
- Mobile Number Verification (SMS)
- Handle Credit Card with Stripe
- In-app Notification
- Real-time GPS Tracking


#### Courier - Progressive Web App
- List all jobs on Google Map
- Real-time GPS Tracking
- Route with distance and time
- Taking photo from device’s camera
- Total Earnings and Driven miles
- Google Map API libraries
- Push Notification


- Super Admin Dashboard
- Super Admin Authentication
- Backend Dashboard with Django
- Monitor Customers, Couriers, Orders
- Mobile Number Verification (SMS)
- Handle Payout with Paypal API





## Screenshots

![photo](/images/delivery-1.png)
![photo](/images/delivery-2.png)
![photo](/images/delivery-3.png)
![photo](/images/delivery-4.png)
![photo](/images/delivery-5.png)
![photo](/images/delivery-6.png)
![photo](/images/delivery-7.png)



## Setup

* This project is built on python 3.8 and django 3.1.3, if you using Ubuntu, follow the steps below to install setup your project:
``` 
1 - sudo apt update #update system repos
2 - sudo apt-get install python3.8 
3 - sudo apt-get -y install python3-pip
4 - sudo pip3 install virtualenv 
5 - virtualenv -p python3 myenv
6 - source myenv/bin/activate
7 - git clone https://github.com/martin-creator/Communitydeliveryapp.git
8 - cd Communitydeliveryapp.git
7 - pip3 install -r requirements.txt 
8 - Please visit [firebase console](https://console.firebase.google.com/), [google maps console](https://console.cloud.google.com/), your email host to update variable in [settings.py](./quickparcel/settings.py)
9 - python3 manage.py runserver
10 - Visit http://127.0.0.1:8000/ to see your application


```



## Usage

This project is a template for  any delivery business models  that have , gps tracking, booking,  review, payments, and job creation in the functionality.  It is therefore very possible for anyone to use it as a starting point to build a startup  to improve   lives in your community and even your own life!


## Project Status

Project is: _in progress_ 


## Room for Improvement

Room for improvement:
- Refactoring code to follow DRY & KISS principles
- Include documentation in python and html files
- Clean code to remove any comments

To do:
- Integrate mobile money payments
- Seperating customer and courier models




## Acknowledgements

- This project was inspired by [Code4Startup](https://code4startup.com/)
- Many thanks to [Leo Chan](https://hk.linkedin.com/in/leowchan) for giving me a scholarship to hone my software engineering skills. 


## Contact
Created by <martinlubowa@outlook.com> - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->


