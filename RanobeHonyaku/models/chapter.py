from RanobeHonyaku.database import db


class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    body = db.Column(db.String(1000000))

    # Need a compound index on series_id and title... maybe?

    series_id = db.Column(db.Integer, db.ForeignKey("series.id"))

    def __init__(self, title, body, series):
        self.title = title
        self.body = body
        self.series = series

    def __str__(self):
        return "<Chapter {}:{}>".format(self.series.title, self.title)

    __repr__ = __str__
