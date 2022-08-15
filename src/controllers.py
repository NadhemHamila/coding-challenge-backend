from flask import request, Blueprint
import random
from .services import add_number, sample_10

routes = Blueprint('services', __name__)


@routes.route("/add", methods=['POST'])
def add():
    response = add_number()
    return response

@routes.route("/sample10", methods=['GET'])
def sample():
    response = sample_10()
    return response
