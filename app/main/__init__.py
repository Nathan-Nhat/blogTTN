from flask import Blueprint

main = Blueprint('main', __name__, template_folder="templates")

from .views import views, errors
