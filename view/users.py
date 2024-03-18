import functools
from flask import Flask, render_template, request, redirect, url_for, flash, session,Blueprint
from database import database
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from database.database import get_db
from user import User

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.get('/')
def users():
    if current_user.is_authenticated:
        show = True if current_user.role == 1 else False
    else:
        show = False

    if show is False:
        return redirect(url_for('homepage.home'))

    else:
        db = get_db()
        command = "SELECT * FROM uživatel"
        table = db.execute(command)
        data = table.fetchall()
        return render_template('users/users.html', neco=data)


@bp.post('/')
def users1():
    data = request.form
    if 'admin' in data:
        is_admin = data['admin']
        db = get_db()
        db = db.execute("SELECT * FROM uživatel")
        table = db.fetchall()
        id_user = table[int(is_admin)][0]

        if table[int(is_admin)][5] == 1:
            db1 = get_db()
            db1.execute("UPDATE uživatel SET id_role=2 WHERE id_uživatele=?", (id_user,))
            db1.commit()

        else:
            db1 = get_db()
            db1.execute("UPDATE uživatel SET id_role=1 WHERE id_uživatele=?", (id_user,))
            db1.commit()

        flash(f"Role změněna.", "info")

    if 'delete' in data:

        index_user = int(data['delete'])
        index_user -= 1
        db = get_db()
        table = db.execute('select id_uživatele,username, id_role from uživatel')

        id_user = table.fetchall()[index_user][0]

        table = db.execute('select id_uživatele,username, id_role from uživatel')
        username = table.fetchall()[index_user][1]

        table = db.execute('select id_uživatele,username, id_role from uživatel')
        user_role = table.fetchall()[index_user][2]

        if user_role == 1:
            if current_user.username == 'admin':
                db.execute('delete from uživatel where id_uživatele=?', (id_user,))
                db.commit()
                flash(f"Uživatel {username} byl smazán.", "info")
            else:
                flash("Pouze admin může mazat další administrátory.", "info")
        else:
            db.execute('delete from uživatel where id_uživatele=?', (id_user,))
            db.commit()
            flash(f"Uživatel {username} byl smazán.", "info")

    return redirect(url_for('users.users'))
