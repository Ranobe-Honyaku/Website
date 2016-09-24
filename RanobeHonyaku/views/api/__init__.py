from flask import Blueprint, redirect, jsonify

from utils import setup_file

API = Blueprint("api", __name__, url_prefix="/api")


# This is the base for the API; Will redirect to our Github organisation page so it always links to latest documentation
@API.route(rule="")
def root():
    return redirect(setup_file["GITHUB"], 301)


# Our class for API errors to raise so we can catch it with our error_handler function
class APIError(Exception):

    def __init__(self, message: str, status_code: int):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

    def format_to_dict(self):
        return {"message": self.message,
                "error": self.status_code}


# Handles all errors that involve the API; Will return an error message and the response code
@API.errorhandler(APIError)
def api_error_handler(error):
    response = jsonify(error.format_to_dict())
    return response, error.status_code
