# Introduction 

**first time mom** is an innovative and user friendly application, that offers support, through activities, to new moms trying to navigate their pregnancy journey as they prepare to welcome their little ones. This web-based application allows users to book and/or cancel different activities. Check out the application **here**


# Table of Contents
## UX
## Design
- Colors 
- Typography 
- Images/Icons
- Responsiveness 
## Wireframes 
## Features
- Navigation
- Home page
- Error pages
- Future Developments 
## Testing 
### Validation Testing 
### Lighthouse
### Manual Testing 
## Deoployment and Version control 
## Technologies Used
## Credits
## Acknowledgements 


# User Strories

### As a developer I want:
- New users to create an account
- Returning users to login
- Users to easily navigate through the pages
- Users to reserve a spot
- Users to book classes and activities
- Users to cancel booking
- Users to view location
- Users to view opening and closing hours
### As a user, I want: 
- To create an account
- Login
- Book classes and activities
- Cancel reservations in case of anything
- Search activities
- View location
- View opening hours


## Design


## Wireframes

### Project scope(5-planes)

### Logic Flowchart
- Find the logic flowchart **here**

### ERD Design
- Find the entity relation diagram **here**

# Deoployment and Version control 

## Deployment to Heroku
The following are steps taken when deploying to heroku
- Login to Heroku account or create an account if you don't have one.
- On the main page, click the 'New' button at the top right corner and select 'Create New App'.
- Enter a name 
- Select a region 
- Click 'Create App'
### Prepare the environment and settings.py file:
- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the dafault databse configuration.
- Save all files and make migrations. 
- Add cloudinary URL to env.py.
- Add the Cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR.
- Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost'].
### Create files
- Create a requirements.txt file
- Create directories in the main directory; media, static and templates.
- Create a "Procfile" in the main directory and add the following: web: gunicorn project_name.wsgi
- Make sure the Procfile is capitalized and only has one line.
### Update Heroku Config Vars
Add the following in Heroku:
- SECRET_KEY value
- CLOUDINARY_URL
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1
- HEROKU_POSTGRESQL_OLIVE_URL value
- DATABASE_URL value
### Deployement
- Make sure DEBUG = False in the settings.py
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the GitHub repository is updated.
- Click 'Open App' to view the deployed live site.
## Forking 
To make a copy of the original repository on a GitHub account, ao as to view and/or make changes without affecting the original repository use the following steps:
- Log in to GitHub and locate the repository badware-detective
- At the top of the Repository (not the top of the page) just above the "Settings" Button on the menu, locate the "Fork" Button.
- You should now have a copy of the original repository in your GitHub account.
## Cloning the Github Repository
To clone the original repository:
- Log in to GitHub and locate the repository badware-detective
- Above the list of files(top right of screen), click Code
- Copy the URL using HTTPS, under "HTTPS"
- Type git clone in your terminal, and then paste the URL you copied
- Press Enter to create your local clone.

