from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from RanobeHonyaku.database import db
from RanobeHonyaku.models import Series
from .chapter import chapter_list_fields

# Fields to serialize when a single series is requested
series_detail_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "chapters": fields.List(fields.Nested(chapter_list_fields))
}

# Fields to serialize when a list of series is requested
series_list_fields = {
    "id": fields.Integer,
    "title": fields.String,
}


# Shows or mutates a single series item
class SeriesDetail(Resource):

    @marshal_with(series_detail_fields)
    def get(self, series_id):
        series = Series.query.get(series_id)

        # Abort if it returns None
        if not series:
            abort(404)

        return series

    @marshal_with(series_detail_fields)
    def put(self, series_id):

        # Try to get the series
        series = Series.query.get(series_id)

        # Abort if it returns None
        if not series:
            abort(404)

        # Try to get the series title abort if it's not there
        try:
            series.title = request.json['title']
        except KeyError:
            abort(400)

        # Update the database
        db.session.commit()

        return series

    @marshal_with(series_detail_fields)
    def delete(self, series_id):

        # Try get the series
        series = Series.query.get(series_id)

        # Abort if it returns None
        if not series:
            abort(404)

        # TODO Protect this against cascading deletes

        # Delete the item from the database
        db.session.delete(series)
        # Confirm the delete
        db.session.commit()

        return series


# Shows a list of all series, or POST to add new series
class SeriesList(Resource):

    @marshal_with(series_list_fields)
    def get(self):
        return Series.query.all()

    @marshal_with(series_detail_fields)
    def post(self):

        # Try to get the title, if it's not there abort
        try:
            title = request.json['title']
        except KeyError:
            abort(400)

        # need to check if series already exists before adding

        # Make a series object to add to the database
        series = Series(title=title)
        # Add the series to the database
        db.session.add(series)
        # Confirm the addition
        db.session.commit()

        # Return the response code for creation + the series created
        return series, 201
