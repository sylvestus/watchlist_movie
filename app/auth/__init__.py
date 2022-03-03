from flask import Blueprint
#from ..auth import login_manager

auth = Blueprint('auth',__name__)

from . import views,forms