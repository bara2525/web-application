import flask
import functools
from flask import Flask, render_template, request, redirect, url_for, flash, session,Blueprint
from database import database
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from database.database import get_db
from user import User

bp = Blueprint('homepage', __name__, url_prefix='/')


@bp.route('/')
def home():

    if current_user.is_authenticated:
        if current_user.role == 1:
            show = True
        elif current_user.role == 2:
            show = False
    else:
        show = False

    return render_template("homepage/index.html", showit=show)

