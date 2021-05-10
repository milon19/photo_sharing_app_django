# Photo Sharing Web App Usign Django

## Setup

It is best to use the python `virtualenv` tool to build locally:
- Clone the repository

```shell script
$ git clone https://github.com/milon19/photo_sharing_app_django
$ cd photo_sharing_app_django
```
- Create Virtual environment and Install dependencies

```diff
$ virtualenv env
$ source ./env/bin/activate
$ pip install -r requirements.txt
```

- Make `.env` file to the root directory of the project. `.env` file should contains following variables.
```
SECRET_KEY=
ALLOWED_HOSTS=
DEBUG=
SQLITE_URL=
CORS_ALLOWED_ORIGINS=
```

## Run
```shell script
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
Then visit [http://localhost:8000](http://localhost:8000) to view backend of the app.
Here is the frontend part of this app [FRONTEND](https://github.com/milon19/photo_sharing_app_react).

## Deploy to Heroku

This application is currently deployed in Heroku. 

To Visit follow this link: [Heroku App URL.]()