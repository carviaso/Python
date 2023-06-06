# [How To Build a Universal Application with Nuxt.js and Django](https://www.digitalocean.com/community/tutorials/how-to-build-a-universal-application-with-nuxt-js-and-django)

``` 
mkdir recipes_app
cd recipes_app

pip install pipenv
pipenv shell
pipenv install django django-rest-framework django-cors-headers

django-admin startproject api
cd api
python manage.py startapp core
```