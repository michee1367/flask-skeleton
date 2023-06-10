from flask import Blueprint
from controllers.authController import login
from hashlib import pbkdf2_hmac

auth = Blueprint('auth', __name__)

auth.route('/login', methods=['POST'])(login)
