# Canopus
[![Build Status](https://travis-ci.org/josuemontano/API-platform.svg?branch=master)](https://travis-ci.org/josuemontano/API-platform)

**Live Demo:** [https://api-hanovit.rhcloud.com](https://api-hanovit.rhcloud.com)

---

This project was built to provide a starting point to develop RESTful applications with Pyramid and AngularJS.

The backend is built on top of [Pyramid](http://trypyramid.com). The app implements JSON Web Token authentication. The frontend is an AngularJS 1 application.

## Database

The project has a PostgreSQL connection configured by default. Change the `sqlalchemy.url` property in `development.ini` and `alembic.ini` to match your database settings. Make sure you have PostgreSQL set in your PATH, psycopg2 requires it.

For [PostgresApp](http://postgresapp.com/) you have to add these lines to your bash profile:

```bash
export PATH=/Applications/Postgres.app/Contents/Versions/9.4/bin:$PATH
export DYLD_LIBRARY_PATH=/Applications/Postgres.app/Contents/MacOS/lib
```

It should be straightforward to configure the SQL database of your preference.

## Backend

The app is configured to use a PostgreSQL database, so make sure you have one up and running; then configure the settings for SQLAlchemy on `development.ini` and `alembic.ini`. The first time you have to run the migrations:

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

The frontend is served by the same Pyramid app. Grunt tasks for AngularJS minification and Sass compiling are set up, so install [NodeJS](http://nodejs.org) on your development conputer. Then install the project dependencies:

```bash
cd $VENV/metropolitan
npm install
```

#### Grunt tasks

`Gruntfile.js` defines two tasks: default and build. Use the default task for development, for deployment run `grunt build`.

**Note:** Please note Browsersync is enabled and the proxy port is set to 6543, so make sure the server is running on this port or change it to the desired one.

## Deploying on OpenShift

You can deploy on [OpenShift](https://openshift.redhat.com) over HTTPS out of the box. When creating your application just fill in the Source Code field with the value: [https://github.com/josuemontano/API-platform](https://github.com/josuemontano/API-platform). Then update the DB settings, as explained before.

Finally, do not forget to set the `JWT_SECRET` variable:

```bash
rhc env set JWT_SECRET=secret -a app_name
```
