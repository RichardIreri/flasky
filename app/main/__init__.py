""" Main blueprint creation. """
# Routes are imported at the bottom after blue print creation to avoid circular dependancies.

from flask import Blueprint

main = Blueprint('main', __name__)

# Relative import (current package).
from . import views, errors   # Importing the routes inorder to associate them with blueprint.