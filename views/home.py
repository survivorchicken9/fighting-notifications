from os import getenv
from dotenv import load_dotenv
from flask import Blueprint, render_template

load_dotenv()  # allows dot env file to be read by os

home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/')
def index():
    return render_template('home.html')
