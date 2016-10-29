# Canopus
[![Build Status](https://travis-ci.org/josuemontano/API-platform.svg?branch=master)](https://travis-ci.org/josuemontano/API-platform)

**Live Demo:** [https://api-hanovit.rhcloud.com](https://api-hanovit.rhcloud.com)

---

This project was built to provide a starting point for developing a REST applications with Pyramid and AngularJS.

The server is built on top of [Pyramid](http://trypyramid.com) (web development with style, indeed), of course. Pyramid itself exposes and serves the REST resources. It makes use of [PyJWT](https://github.com/jpadilla/pyjwt) in the auth module for JSON Web Token authentication.

The front end is an AngularJS 1 application built with [Satellizer](https://github.com/sahat/satellizer), [AngularUI Router](https://github.com/angular-ui/ui-router) and [Restangular](https://github.com/mgonto/restangular).

## Database

The project has a PostgreSQL connection configured by default. Change the `sqlalchemy.url` property in `development.ini` and `alembic.ini` to match your database settings. Make sure you have PostgreSQL set in your PATH, psycopg2 requires it. If using [PostgresApp](http://postgresapp.com/), as I do, add these lines to your bash profile

```bash
export PATH=/Applications/Postgres.app/Contents/Versions/9.4/bin:$PATH
export DYLD_LIBRARY_PATH=/Applications/Postgres.app/Contents/MacOS/lib
```

It should be straightforward to make it work with the SQL database of your preference.

## Backend

The backend is a Python app built with [Pyramid](http://trypyramid.com). The app is configured to use a PostgreSQL database, so make sure you have one up and running; then configure the settings for SQLAlchemy on `development.ini` and `alembic.ini`. The first time you have to run the migrations:

```bash
cd $VENV/metropolitan
$VENV/bin/alembic upgrade head
```

Then, to run the app do:

```bash
cd $VENV/metropolitan
$VENV/bin/python setup.py develop
$VENV/bin/pserve development.ini --reload
```

You may also want to deploy the app with WSGI locally using [mod_wsgi](https://modwsgi.readthedocs.org/en/master/).

```bash
../bin/pip install mod_wsgi
mod_wsgi-express start-server wsgi.py --port 6543
```

## Frontend

The frontend is served by the same Pyramid app, so you don't have to run it separately on a NodeJS server or whatever. I often find myself in need to deploy this way due to infraestructure limitations.

Grunt tasks are set up, so install [NodeJS](http://nodejs.org) on your development computer. Then install the project dependencies:

```bash
cd $VENV/metropolitan
npm install
grunt build
```

Now you're a `grunt` away!

**Note:** Please note Browsersync is enabled and the proxy port is set to 6543, so make sure the server is running on this port.

## Deploying on OpenShift

You can deploy on [OpenShift](https://openshift.redhat.com) over HTTPS out of the box. When creating your application just fill in the Source Code field with the value: [https://github.com/josuemontano/API-platform](https://github.com/josuemontano/API-platform). All is left to you is the DB configuration, as explained before, and setting the `JWT_SECRET` variable.

```bash
rhc env set JWT_SECRET=secret -a app_name
```
