#!/usr/bin/env python3
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, prompt_pass, prompt_bool
from flask_security.utils import encrypt_password

from RanobeHonyaku import app
from RanobeHonyaku.database import db
from RanobeHonyaku.models import User, Role

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)


@manager.command
def runserver():
    app.run(host="127.0.0.1", port=5000, debug=True)


# Adopted from https://github.com/KanColleTool/kcsrv/blob/master/commands/user.py
@manager.command
def create_user(name, email):
    print("Username: " + name)
    print("Email: " + email)

    while True:
        password = prompt_pass("Password")
        if password == prompt_pass("Again"):
            break

    roles_list = input("Roles (separated by space): ").split(" ")
    roles = [Role.query.filter_by(name=role).first_or_404() for role in roles_list if role != '']

    if prompt_bool("Create this user?"):
        user = User(name=name, email=email, password=encrypt_password(password), roles=roles)
        db.session.add(user)
        db.session.commit()


@manager.command
def setup():
    print("Installing default roles...")
    db.session.add(Role(name="admin"))
    db.session.add(Role(name="staff"))
    db.session.commit()


if __name__ == "__main__":
    manager.run()
