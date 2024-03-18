import flask
import functools
from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint
from database import database
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from database.database import get_db
from user import User
from view import categories, auth, homepage, product, price,users
from view.auth import login_manager

app = Flask(__name__)

app.config.from_object('config')
database.init_app(app)


login_manager.init_app(app)

app.register_blueprint(categories.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(homepage.bp)
app.register_blueprint(product.bp)
app.register_blueprint(price.bp)
app.register_blueprint(users.bp)


@app.context_processor
def context_processor():

    if current_user.is_authenticated:
        if current_user.role == 1:
            return dict(key=current_user.username, showit=True)
        return dict(key=current_user.username, showit=False)
    else:
        return dict(key='anonymous')


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('homepage.home'))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

