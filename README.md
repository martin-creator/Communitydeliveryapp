# Quickparcel- decentralizing Africa's supply chain system
![header](/images/header.png)
>  At Quickparcel , we create opportunities with all communities with vechiles to participate in making the movement of goods reliable and cheaper for all. 


> Live demo [Project will soon be moved to  the cloud](#). <!-- If you have the project hosted somewhere, include the link here. -->

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

* This project is built on ruby 2.6.2 and rails 6.0.6, if you using Ubuntu, follow the steps below to install rails:
``` 
1 - sudo apt update #update system repos
2 - sudo apt install git curl autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm6 libgdbm-dev libdb-dev #ruby libraries and compilers
3- curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash # install rbenv2
    #Bash commands to update .bashrc file
4 - echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc
    source ~/.bashrc

5 - rbenv -v # check rbenv version
6 - rbenv install -l # check versions of ruby on the systme
7 - rbenv install [version number] # install a specific ruby version
8 - rbenv global [version number] # make installed ruby version as the global version
9 - ruby --version # check ruby version
10 - gem install bundler # install bundler 
10 - gem install rails -v @version number # install rails
11 - rails -version  # check the rails version
12 - git clone @africalancer git repo
13 - cd @africalancer directory
14 - bundle # install gem dependences
15 - rails start # start your rails application


```
Incase you get any errors during installation, you can delete the **Gemfile.lock** and then run **bundle** again. 


## Usage

This project is a template for  any marketplace business models  that have booking,  review, payments, and job creation in the functionality.  It is therefore very possible for anyone to use it as a starting point to build a startup  to improve   lives in your community and even your own life!


## Project Status

Project is: _in progress_ 


## Room for Improvement

Room for improvement:
- Refactoring code to follow DRY & KISS principles
- Upgrading codebase to  newer ruby and rails  versions
- Include documentation in ruby and html files
- Clean code to remove any comments

To do:
- Prepare app for deployment
- Integrate mobile money payments
- Include online status messaging functionality


## Acknowledgements

- This project was inspired by [Code4Startup](https://code4startup.com/)
- Many thanks to [Leo Chan](https://hk.linkedin.com/in/leowchan) for giving me a scholarship to hone my software engineering skills. 
- <https://www.vultr.com/docs/installing-ruby-on-rails-on-ubuntu-20-04/>
- <https://phoenixnap.com/kb/install-ruby-ubuntu>


## Contact
Created by <martinlubowa@outlook.com> - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->


