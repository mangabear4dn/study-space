# StudySpace project

<a href="{{ url_for('static' filename='images/wireframes-studyspace.pdf') }}">Wireframes</a>

**Concept:** StudySpace is a website of a (fictional) company that functions in a similar way as coworking spaces but is targeted towards students.

**Target Audience:** Mainly local students looking for a space to come study individually or in a group if necessary.

## Goals

**Site Owners Goal:** Effective way to manage the students and other visitors at their study space location.

**Anonymous User Goal:** Find a potential study location to visit and learn some basic information about it.

**Registered User Goal:** Have a secure option for study locations and have a way to reserve their time there.

## Used Technologies

- Gitpod - the development enviroment
- GitHub - version control
- Heroku - (via GitHub) deployment of the active site with a database
- Django - framework for building the site
- various django-related packages - to improve the already offered features of Django framework
- Bootstrap - for styling of the site templates
- and others.

### Languages used:

- HTML/CSS
- JavaScrip
- Python
- Markdown

## Development process

The development process started with creating a project using GitPod as the the development enviroment via GitHub.

Following that Django framework was instatlled on the project (project: study_space) as the basis for the website along with an number of additional packages to improve the benefit of using a full framework for the project.

At this point the project was deployed on Heroku remote server and linked to the database provided by Heroku already during the development procces.

The main coding activities were started with creating an app for the django project (app: studyspace) and a superuser ('admin' : 'pass123man') and improving the admin side of the site while working on the 2 necessary models for the application:

1. Space - model for the object representing the information about the physical study spaces offered.

2. Reservation - model for the object representing the information about timeslots Space objects are reserved for.

After working out both of these objects an attempt was made to start testing the already with the Unittest (built-in Django) but technichal problems arose due to a couple of unnoticed typos. 

Too much time was spent on fixing them and the testing was left leaving only some basic placeholder code in the test file for the models.

After that the focus was mainly on creating templates and views for the already created models. And gradually the visualstyling was also applied using Boostrap.

During this stage of the development a number of template forms were imported in the project from Django Allauth package since it was already used to manage the site users and login, signup and logout forms were adjusted to work as the templates for the site while the rest of the imported templates were left be fully utilised in the project later on.

# Credits
Most of the information referenced during the project came from the the official documentations for the frameworks and additional packages integrated in the project such as official documentations for Django and Boostrap among others as well as the Code Institute provided walk-throughs un similar projects. 
Also thank you to the advise of Guido Cecilio who mentored me during this project as well.