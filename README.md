## Luizalabs Employer Manager (Django Coding Test)

## Basic Requirements


- pip

- python3

- python-dev-tools

- npm / node.js


#### npm default dependencies 

View `package.json` file.

#### python dependencies

View `requirements.txt` file.


## Build

``` bash
# install dependencies
npm install

# build for production with minification
npm run build

# collect static files
./manage.py collectstatic

# apply migrations
./manage.py

# seed
./seed_dev.sh

# run python server
./manage.py runserver

```

## Running on dev

```
# Working on the project python environment, run the django server
./run_django_dev.sh

# In another terminal windown run the npm hot reloader serve
./run_npm_dev.sh

```

## Running tests

```sh
Working on the project python environment, run:
./manage test
```
