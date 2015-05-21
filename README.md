# API Starter
[![Build Status](http://img.shields.io/travis/josuemontano/api-starter.svg?style=flat)](https://travis-ci.org/josuemontano/api-starter)

**Live Demo:** [https://api-hanovit.rhcloud.com](https://api-hanovit.rhcloud.com)

---

This project was built to demonstrate (thus the pyramid project is called demonstrare) how to build a simple REST server with Pyramid and how to consume it with AngularJS. One of the key reasons to build this project was to show how to serve the client from Pyramid itself, so you don't have to run the client separately on a NodeJS server or whatever. Some may argue this is not a good practice, however, due to some infraestructure restrictions I often need to do it this way.

I hope the project provides a good starter point for anyone doing some Pyramid and AngularJS magic. Happy coding!

## Cool stuff...
The server is built on top of [Pyramid](http://pylonsproject.org/projects/pyramid/about) (web development with style indeed). [Restless](http://restless.readthedocs.org) is integrated with Pyramid to serve the REST resources. And we make use of [PyJWT](https://github.com/jpadilla/pyjwt) in the auth module for token signing.

The front end is an AngularJS application. The auth module has [Satellizer](https://github.com/sahat/satellizer) at its core, [AngularUI Router](https://github.com/angular-ui/ui-router) provides routing and ngResource for consuming the REST API.

## Database
By default the project has a PostgreSQL connection configured. Change the `sqlalchemy.url` property in `development.ini` and `alembic.ini` to match your database settings. Make sure you have PostgreSQL in your PATH, psycopg2 requires it. If using [PostgresApp](http://postgresapp.com/), as I do, add these lines to your bash profile
```sh
export PATH=/Applications/Postgres.app/Contents/Versions/9.4/bin:$PATH
export DYLD_LIBRARY_PATH=/Applications/Postgres.app/Contents/MacOS/lib
```

It should be straightforward to change to the database of your preference.

## Running
Migrations are provided by Alembic, you need to run them the first time. On the other hand, the app will look for an env variable called `JWT_SECRET`, make sure have set it. The following example assumes you have a python3 virtual enviroment `$VENV`
```sh
export JWT_SECRET='secret'
cd $VENV/api-starter
../bin/python setup.py develop
../bin/alembic upgrade head
../bin/pserve development.ini --reload
```

You may also deploy the app with WSGI locally using [mod_wsgi](https://modwsgi.readthedocs.org/en/master/).
```sh
../bin/pip install mod_wsgi
mod_wsgi-express start-server wsgi.py --port 6543
```

The project has grunt tasks configured, so you need to do:
```sh
npm install
grunt watch
```

Now you're ready to start developing and contributing!

## OpenShift
You can deploy API Starter on [OpenShift](https://openshift.redhat.com) out of the box. When creating your application just fill the Source Code field with [https://github.com/josuemontano/api-starter](https://github.com/josuemontano/api-starter). All is left to you is the DB configuration as explained before.
