# Website

The Ranobe-Honyaku website source code.

## Installation

### Prerequisites

* python3
* virtualenv
* Flask
* PostgreSQL

### Database Setup

```sql
DROP DATABASE ranobe_dev;
CREATE ROLE ranobe_usr WITH LOGIN PASSWORD 'password';
CREATE DATABASE ranobe_dev OWNER ranobe_usr;
\q
```

### Clone and set up virtualenv

```shell
git clone https://github.com/Ranobe-Honyaku/Website.git
cd Website
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
cp setup_example.json setup.json
```

At this point, open setup.json. You will probably need to change
`SQLALCHEMY_DATABASE_URI` to the path of your local database, provide login
credentials, etc. Try this string format:

```
"postgresql://username:password@host:port/database"
"postgresql://ranobe_usr:password@localhost:5432/ranobe_dev"
```

### Run migrations on the database

```shell
python manage.py db upgrade
```

This applies migrations in the `migrations/` directory to your local database.
Typically you will need to perform this whenever the schema in your database
does not match the schema defined in `models/`.

To make migrations, you can run `manage.py db migrate`, but you won't need to
do this right after `git pull/fetch`. You will need to make migrations when
you change the model yourself though. Please remember to comment the migrations
in `/migrations/versions/`.

### Load database with initial data (superusers, roles, etc)

You will only need to do this if this is your first time setting up the
database (or if you dropped/deleted the database previously).

```shell
python manage.py setup
python manage.py create_user <username> <email>
```

Follow the on-screen instructions. The current roles available are `admin` and `staff`

### Runserver

```shell
python manage.py runserver
```

Note that this set of instructions is for a development configuration only. Debug mode is on.
