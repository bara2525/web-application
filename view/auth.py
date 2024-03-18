import flask
import functools
from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint
from database import database
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from database.database import get_db
from user import User

bp = Blueprint('auth', __name__, url_prefix='')
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    db = get_db()
    try:
        user_data = db.execute("SELECT * FROM uživatel WHERE id_uživatele = ?", (user_id,)).fetchone()
        if user_data is None:
            return None
        else:
            return User(user_data['id_uživatele'], user_data['username'], user_data['password'], user_data['id_role'])

    except db.Error as e:
        flash('Omlouváme se, nastal problém s databází.', 'error')
        print('DB Error: ' + str(e))
        return None


@bp.get('/registration')
def registration():
    return render_template('auth/registration.html')


@bp.post('/registration')
def register():
    data = request.form
    db = get_db()

    try:
        db.execute("INSERT INTO uživatel (jméno,příjmení,username,password,id_role) VALUES (?,?,?,?,?)",
                   (data['fname'], data['lname'], data['username'], data['password'], 2))
    except:
        flash('Error username musí být unikátní, nebo nastala jiná chyba. Zkuste to znovu.', 'error')
        return redirect(url_for('auth.registration'))

    else:
        db.commit()

    flash('Registrace proběhla úspěšně. Nyní se můžete přihlásit.', 'info')
    return redirect(url_for('auth.registration'))


@bp.get('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for("homepage.home"))
    return render_template('auth/login.html')


@bp.post('/login')
def logins():
    logout_user()

    data = request.form
    db = get_db()
    result = db.execute("SELECT count(*) FROM uživatel WHERE username=? AND password=?",
                        (data['username'], data['password']))
    result = result.fetchone()[0]

    username = data['username']
    password = data['password']

    if result == 1:
        id_user = db.execute("SELECT id_uživatele FROM uživatel WHERE username=? AND password=?", (username, password))
        id_user = id_user.fetchone()[0]

        role = db.execute("SELECT role.název FROM uživatel,role WHERE username=? and role.id_role = uživatel.id_role",
                          (username,))
        role = role.fetchone()[0]

        user = User(id_user, username, password, role)
        login_user(user)
        flask.flash(f'Login úspěšný! Vítej {user.username}.')
        return redirect(url_for('auth.login'))

    flash('Zadali jste nesprávné přihlašovací údaje.', 'error')
    return redirect(url_for('auth.login'))


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

