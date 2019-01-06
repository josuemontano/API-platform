canopus
=======

[![Build Status](https://travis-ci.org/josuemontano/API-platform.svg?branch=master)](https://travis-ci.org/josuemontano/API-platform)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

## What you get

- Pyramid web framework
- Cornice for REST endpoints
- Database migrations with alembic
- JWT authentication
- Login with Google and Microsoft accounts
- Task queues with Huey
- Pytest
- Webpack 4
- ES2017
- Karma, mocha and expect.js
- Preact
- ESLint
- Dokku deployments

## Getting started

**Important**: Install Python 3.7.x and npm 8.x before proceeding.

```sh
# Change directory into your newly created project.
cd canopus

# Install poetry
pip3 install poetry

# Install the project in editable mode with its testing requirements.
poetry install
npm install

# Run database migrations.
poetry run alembic upgrade head

# Run your project's tests.
poetry run pytest --cov=canopus

# Run your project.
npm start
poetry run pserve development.ini --reload
```

## Deployment

Given you added the remote repository you just need to do `git push production master` to deploy to your production server.

```sh
git remote add production dokku@ip:canopus
```

**Note:** Assets are not compiled at deployment, therefore you need to compile them by yourself with `npm run build`.

## New server instances

```sh
# Install Dokku
wget https://raw.githubusercontent.com/dokku/dokku/v0.12.12/bootstrap.sh
sudo DOKKU_TAG=v0.12.12 bash bootstrap.sh

# Create the dokku app
dokku apps:create canopus

# Install PostgreSQL and PostGIS
sudo dokku plugin:install https://github.com/dokku/dokku-postgres.git postgres
sudo docker pull mdillon/postgis:latest

export POSTGRES_IMAGE="mdillon/postgis"
export POSTGRES_IMAGE_VERSION="latest"
dokku postgres:create canopus
dokku postgres:link canopus canopus

# Install redis
sudo dokku plugin:install https://github.com/dokku/dokku-redis.git redis
dokku redis:create canopus
dokku redis:link canopus canopus

# Configure env variables
dokku config:set canopus JWT_SECRET=
dokku config:set canopus APP_CONFIG_FILE=production.ini
dokku config:set canopus PG_DATABASE_URL=postgres://postgres:@dokku-postgres-canopus:5432/canopus

dokku ps:scale canopus web=1 worker=1

# Setup DNS
dokku domains:add canopus example.com

# Generate an SSL certificate
sudo dokku plugin:install https://github.com/dokku/dokku-letsencrypt.git
dokku config:set --no-restart canopus DOKKU_LETSENCRYPT_EMAIL=
dokku letsencrypt canopus
```

## Console access

```
dokku run canopus bash
poetry run pshell production.ini
```

## TODOS

- [ ] Setup better logging
