# Canopus
[![Build Status](http://img.shields.io/travis/josuemontano/api-starter.svg?style=flat)](https://travis-ci.org/josuemontano/api-starter)

**Live Demo:** [https://api-hanovit.rhcloud.com](https://api-hanovit.rhcloud.com)

---

This project was built to provide a starting point for developing a REST applications with Pyramid and AngularJS.

The server is built on top of [Pyramid](http://trypyramid.com) (web development with style, indeed), of course. Pyramid itself exposes and serves the REST resources. It makes use of [PyJWT](https://github.com/jpadilla/pyjwt) in the auth module for JSON Web Token authentication.

The front end is an AngularJS 1 application built with [Satellizer](https://github.com/sahat/satellizer), [AngularUI Router](https://github.com/angular-ui/ui-router) and [Restangular](https://github.com/mgonto/restangular).

### Database

By default the project has a PostgreSQL connection configured. Change the `sqlalchemy.url` property in `development.ini` and `alembic.ini` to match your database settings. Make sure you have PostgreSQL set in your PATH, psycopg2 requires it. If using [PostgresApp](http://postgresapp.com/), as I do, add these lines to your bash profile
```bash
export PATH=/Applications/Postgres.app/Contents/Versions/9.4/bin:$PATH
export DYLD_LIBRARY_PATH=/Applications/Postgres.app/Contents/MacOS/lib
```

It should be straightforward to make it work with the SQL database of your preference.

### Running
To run it, and assuming you have a virtual enviroment `$VENV` created, just do:

```bash
export JWT_SECRET='secret'
cd $VENV/api-starter
../bin/python setup.py develop
../bin/alembic upgrade head
../bin/pserve development.ini --reload
```

Migrations are provided by [Alembic](http://alembic.readthedocs.org), you need to run them the first time. The app will look for an env variable called `JWT_SECRET`, make sure it is properly set.

You may also deploy the app with WSGI locally using [mod_wsgi](https://modwsgi.readthedocs.org/en/master/).

```bash
../bin/pip install mod_wsgi
mod_wsgi-express start-server wsgi.py --port 6543
```

### Frontend

The frontend is served by the same Pyramid app, so you don't have to run it separately on a NodeJS server or whatever. I often find myself in need to deploy this way due to infraestructure limitations.

Grunt tasks are set up, so install [NodeJS](http://nodejs.org) on your development computer. Then install the project dependencies:

```bash
cd $VENV/metropolitan
npm install
grunt build
```

Now you're a `grunt` away!

**Note:** Please note Browsersync is enabled and the proxy port is set to 6543, so make sure the server is running on this port.

### OpenShift

You can deploy on [OpenShift](https://openshift.redhat.com) over HTTPS out of the box. When creating your application just fill in the Source Code field with the value: [https://github.com/josuemontano/api-starter](https://github.com/josuemontano/api-starter). All is left to you is the DB configuration, as explained before, and setting the `JWT_SECRET` variable.

```bash
rhc env set JWT_SECRET=secret -a app_name
```
