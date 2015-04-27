# API Starter

## Requirements
Most requirements are defined in `setup.py`. Besides them, you need to have a PostgreSQL dabatase up and running, then configure the `sqlalchemy.url` property in `development.ini` and `alembic.ini`.

Make sure you have PostgreSQL in your PATH, psycopg2 requires it. If using [PostgreApp](http://postgresapp.com/), as I do, add these lines to your bash profile
```
export PATH=/Applications/Postgres.app/Contents/Versions/9.4/bin:$PATH
export DYLD_LIBRARY_PATH=/Applications/Postgres.app/Contents/MacOS/lib
```

## Running
Run as any other Pyramid app, in case you have a virtual enviroment configured (`$VENV` in the following example) just do
- `$VENV/bin/python setup.py develop`
- `$VENV/bin/pserve development.ini --reload`

If you have installed [mod_wsgi](https://modwsgi.readthedocs.org/en/master/) in your virtual enviroment you may start the app doing
`mod_wsgi-express start-server wsgi.py --port 6543`
