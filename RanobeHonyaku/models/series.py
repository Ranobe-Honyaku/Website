from app import db

"""
A novel series
"""
class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)

    chapters = db.relationship("Chapter", backref="series", lazy="dynamic")

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Series %r>' % self.title