# Luizalabs Employee Manager (Django Coding Test)

[![Build Status](https://travis-ci.com/JoabMendes/luizalabs_test.svg?token=YiXFcShY3q5wCAWymCUr&branch=master)](https://travis-ci.com/JoabMendes/luizalabs_test)

#### Index

- [Introduction](https://github.com/JoabMendes/luizalabs_test#introduction)
  - [Basic Requirements](https://github.com/JoabMendes/luizalabs_test#basic-requirements)
  - [Build](https://github.com/JoabMendes/luizalabs_test#build)
  - [Running on dev](https://github.com/JoabMendes/luizalabs_test#running-on-dev)
  - [Testing](https://github.com/JoabMendes/luizalabs_test#running-tests)
- [Architecture](https://github.com/JoabMendes/luizalabs_test#architecture)
  - [Domain view](https://github.com/JoabMendes/luizalabs_test#domain-view)
  - [Package view](https://github.com/JoabMendes/luizalabs_test#package-view)
- [API](https://github.com/JoabMendes/luizalabs_test#api-endpoints)
  - [Employee Endpoints](https://github.com/JoabMendes/luizalabs_test#employee-endpoints)
  - [Department Endpoints](https://github.com/JoabMendes/luizalabs_test#department-endpoints)
- [Frontend](https://github.com/JoabMendes/luizalabs_test#frontend)
- [Considerations](https://github.com/JoabMendes/luizalabs_test#considerations)


## Introduction

This test project was developed using Python3 + Django 2.0
as framework, with a REST API built with the [DRF](https://www.django-rest-framework.org/) library support. 
Using SQLite for the dev environment and a dynamic database setting.
The frontend uses Vue.js 2 with
the [Bootstrap Vue](https://bootstrap-vue.js.org) as its component
library and it consumes the referenced Django API. 

The project was created from a [Python/Django + Vue.Js skeleton](https://github.com/JoabMendes/vue_django_skeleton) 
application that I use to bootstrap my projects.

### Basic Requirements

- [pip](https://pip.pypa.io/en/stable/installing/) - python package-management system.

- [virtualenv](https://virtualenv.pypa.io/en/latest/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) - tool to create isolated Python environments

- [python3](https://www.python.org/download/releases/3.0/)

- python-dev-tools - os python requirements

- [npm](https://www.npmjs.com/get-npm) / [node.js](https://nodejs.org/en/)

#### Python dependencies

View `requirements.txt` file.

#### Javascript dependencies 

View `package.json` file.


### Build

After creating a python 3 environment and start working on it, you can run these following
commands to to build, populate the database and serve the application
in your machine:

``` bash
# install javascript dependencies
$ npm install

# build javascript frontend instance
$ npm run build

# collect static files
$ ./manage.py collectstatic

# apply migrations
$ ./manage.py migrate

# populate the database for developement
$ ./seed_dev.sh

# run python server
$ ./manage.py runserver

```

The seed command will create a django admin superuser with the following
credentials:

- Login: `admin`
- Password: `admin123`

### Running on dev

There're existing shell scripts in the project root to execute 
the application serving in your local machine (run the building instructions first):

```
# Working on the project python environment, run the django server
$ ./run_django_dev.sh

# In another terminal windown run the npm hot reloader server
$ ./run_npm_dev.sh

# This command  will open the browser automatically on localhost:8080, but
# you should head to http://127.0.0.1:8000 instead.
# To check the django admin head to: http://127.0.0.1:8000/admin

```

### Running tests

There's a shell script to run the style check and the 
django tests all together:

```sh
Working on the project python environment, run:
$ ./test.sh
```

If you want to run them separately:

```sh
# Style test with flake8
$ flake8 domain app api --exclude=*/migrations,*settings

# Django tests
$ ./manage.py test
```

## Architecture

### Domain view

The following diagram describes the designed domain for this challenge:

![Domain Diagram](https://i.imgur.com/YbDje80.png)

This domain is implemented in the `domain.models.py` module, which specifiess
the Django ORM Classes. The employee domain is responsible to manage/store
the Employee entities and despite the problem description showing
the employee department as a field, I decided to normalize it in another
table. Then, the Department domain will be responsible to manage/store the
department entities of the application. 

### Package view

As I'm using Django for this project, by default it proposes the use of a layered MVC architecture
(Models, Views and Controllers - In Django they are called Models, Templates and Views instead). The models provide an
interface for the application domain data in a Object oriented structure. As
I created an API I don't use the Template layer and my Views implement the API logic and
access to the endpoints: Here is a package diagram of this project:

![Package Diagram](https://i.imgur.com/SEcgMWm.png)

Other packages and modules are present in the application but the diagram
represent the main ones that execute the API flow:

The `app` package contains the the django settings and the wsgi module. It also has
the `urls` module, which provides the system urls and loads the main template. It includes the `api.urls` instance loading the 
api package endpoints into the main application. The `api.urls` module provides
the REST API endpoints, loading the views from the `api.views` package.
The `api.views` package has the two modules: `api.department_view` and the `api.employee_view`
and they implement the REST api methods for the models, which are accessed from the `domain.models` module. 


## API Endpoints

The implemented API provides endpoints to manage the two domain entities
 of this project in a REST format through the default HTTP methods and retuning
 json responses. The existing API endpoints are:

### Employee endpoints:

#### Listing employees

Retrieves all existing employees entities in the database.
It supports pagination if the enabled param is specified.

- **endpoint:** `/api/v1/employee/`
- **method:** `GET`
- **params:** These optional parameters can be specified in the endpoint URI
```json
{
  "pagination": 1, 
  "offset:": 0,
  "employees_per_page": 10
}
```
- **200 Response:**
```json
[
    {
        "department": {
            "id": 1,
            "name": "Architecture"
        },
        "email": "arnaldo@luizalabs.com",
        "id": 1,
        "name": "Arnaldo Pereira"
    },
    {
        "department": {
            "id": 2,
            "name": "E-commerce"
        },
        "email": "renato@luizalabs.com",
        "id": 2,
        "name": "Renato Pedigoni"
    },
    {
        "department": {
            "id": 3,
            "name": "Mobile"
        },
        "email": "catoto@luizalabs.com",
        "id": 3,
        "name": "Thiago Catoto"
    }
]
```

or empty:

```js
[]
```

#### Retrieving an employee

Retrieves an employee by its id

- **endpoint:** `/api/v1/employee/<id>`
- **method:** `GET`
- **params:** By URL
- **200 Response:**
```json
{
    "department": {
        "id": 1,
        "name": "Architecture"
    },
    "email": "arnaldo@luizalabs.com",
    "id": 1,
    "name": "Arnaldo Pereira"
}
```
- **400 Response**
```json
{"employee": ["Invalid pk \"10\" - object does not exist."]}
```

#### Creating an employee

Creates a new employee instance based on the specified payload

- **endpoint:** `/api/v1/employee/`
- **method:** `POST`
- **params:**
```json
{
   "name": "Arnaldo Pereira",
   "email": "arnaldo@luizalabs.com",
   "department": 1
}
```
As the department field is a fk, you need to specify the department
id when creating an employee.

- **201 Response:**
```json
{
    "department": {
        "id": 1,
        "name": "Architecture"
    },
    "email": "arnaldo@luizalabs.com",
    "id": 1,
    "name": "Arnaldo Pereira"
}
```
- **400 Responses**
```py
{"department": ["Invalid pk \"10\" - object does not exist."]}
{"name": ["This field is required"]}
{"email": ["This field is required"]}
{"email": ["Enter a valid email address."]}
{"email": ["This field must be unique."]}
```

#### Updating an employee

Updates an employee instanced based on the specified payload

- **endpoint:** `/api/v1/employee/<id>`
- **method:** `PUT`
- **params:**
```json
{
   "name": "Arnaldo Pereira Jr",
   "email": "arnaldo@luizalabs.com",
   "department": 2
}
```
As the department field is a fk, you need to specify the department
id when updating an employee.

- **200 Response:**
```json
{
    "department": {
        "id": 2,
        "name": "E-commerce"
    },
    "email": "arnaldo@luizalabs.com",
    "id": 1,
    "name": "Arnaldo Pereira Jr"
}
```
- **400 Responses**
```py
{"department": ["Invalid pk \"10\" - object does not exist."]}
{"name": ["This field is required"]}
{"email": ["This field is required"]}
{"email": ["Enter a valid email address."]}
{"email": ["This field must be unique."]}
```

#### Deleting an employee

- **endpoint:** `/api/v1/employee/<id>`
- **method:** `DELETE`
- **params:** `None`

- **204 Response**

```No response body```

- **400 Responses**
```py
{"employee": ["Invalid pk \"10\" - object does not exist."]}
```

### Department endpoints:

#### Listing departments

Retrieves all existing department entities in the database.

- **endpoint:** `/api/v1/department/`
- **method:** `GET`
- **params:** `None`
- **200 Response:**
```json
[
    {
        "id": 1,
        "name": "Architecture"
    },
    {
        "id": 2,
        "name": "E-commerce"
    },
    {
        "id": 3,
        "name": "Mobile"
    }
]
```

## Frontend

The frontend of this application is built using Vue.js as Single Page Application (SPA). The `/index.html`
file is served at `/` as a Django TemplateView and it loads the Vue app configuration.
It uses Webpack 4 to minimize the application and convert it to vanilla javascript
in the `static/build.js` map. 

The component library used is the [Bootstrap Vue](https://bootstrap-vue.js.org) which
implements the Twitter Bootstrap directives as Vue components. Which speeds the
frontend development. The Vue components of this project are hosted in the src package:

```
src/
├── App.vue             # The main template of the application which loads the same navbar throug the SPA
├── components          # This folder stores the children components
│   ├── Index.vue       # Index view - Lists/Delete the employees
│   ├── New.vue         # Add emplooye view - Form to create a new employe instance
│   └── Update.vue      # Update employee view - Form to update an employee instance
└── main.js             # The vue app configuration, where the SPA dependencies are loaded and the routes configured.

```

## Considerations

Several improvements can be done this project and here are some of them:

- A login page and allow access to application only by authenticated users.
- Soft delete, currently the when an instance is deleted it will be erased permanently from the database.
  Soft delete makes possible to recover the information from a inactive domain instance.
- With soft delete enable, defining the active scope of de domain entities is also importante,
  so the retrieved information is always de right active one.
- Add pagination to the views when listings are done (Index.vue).
- Add search and filters to the views with listings (Index.vue).

An extra done for this challenge was the ability to edit employees from the
frontend.

For questions email me at `joabe.mdl@gmail.com`.
