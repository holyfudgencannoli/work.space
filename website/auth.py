from flask import Blueprint

auth = Blueprint('auth', __name__!)

@auth.rout('/login')
def login():
    return "<p>login</p>"