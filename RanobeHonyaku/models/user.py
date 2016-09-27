from flask_security import UserMixin, RoleMixin

from RanobeHonyaku.database import db

# Helper table for multiple-to-multiple relationship
roles_users = db.Table("roles__users",
        db.Column("user_id", db.Integer(), db.ForeignKey("user.id")),
        db.Column("role_id", db.Integer(), db.ForeignKey("role.id")))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    roles = db.relationship("Role", secondary=roles_users, backref=db.backref("users", lazy="dynamic"))

    def __str__(self):
        return "<User {} ({})>".format(self.email, self.name)

    __repr__ = __str__


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    def __str__(self):
        return "<Role {}>".format(self.name)

    __repr__ = __str__

