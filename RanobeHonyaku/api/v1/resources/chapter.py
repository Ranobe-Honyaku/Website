from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from RanobeHonyaku.database import db
from RanobeHonyaku.models import Chapter

# Fields to serialize when a single chapter is requested
chapter_detail_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "body": fields.String
}

# Fields to serialize when a list of chapters is requested
chapter_list_fields = {
    "id": fields.Integer,
    "title": fields.String,
}
