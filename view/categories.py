import flask
import functools
from flask import Flask, render_template, request, redirect, url_for, flash, session,Blueprint
from database import database
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from database.database import get_db
from user import User

bp = Blueprint('categories', __name__, url_prefix='/category')


@bp.get('/')
def category():
    if current_user.is_authenticated:
        if current_user.role == 1:
            show = True
        elif current_user.role == 2:
            show = False
    else:
        show = False

    db = get_db()
    table = db.execute("SELECT * FROM kategorie where id_kategorie != 0")
    data = table.fetchall()
    return render_template('/categories/category.html', database=data, show_it=show)


@bp.post('/')
def categories():
    data = request.form

    if data.get('delete') is not None:
        db = get_db()
        table = db.execute("SELECT * FROM kategorie")
        table = table.fetchall()
        number = int(data.get('delete'))
        number += 1
        id_category = table[int(number)][0]
        db.execute("UPDATE produkt set id_kategorie=0 where id_kategorie=?",(id_category,))
        db.commit()
        db1 = get_db()
        db1.execute("DELETE FROM kategorie WHERE id_kategorie=?", (id_category,))
        db1.commit()
        return redirect(url_for('categories.category'))

    elif data.get('one_form') is not None:
        data1 = request.form['one_form']
        number = data1
        return redirect(url_for('categories.one_category', number=number))

    else:
        name = data.get('name')
        popis = data.get('popis')
        db = get_db()

        if current_user.user_id is not None:
            id = current_user.user_id
        else:
            id = 0
        try:
            db.execute("INSERT INTO kategorie (název, popis, id_uživatele)VALUES (?,?,?)", (name, popis, id))
        except:
            flash('Error název kategorie musí být unikátní nebo nastala jiná chyba.', 'error')

        else:
            db.commit()

        return redirect(url_for('categories.category'))

@bp.get("/one_category")
def one_category():
    number = int(request.args.get('number'))
    number += 1
    db = get_db()
    table = db.execute("SELECT * FROM kategorie")
    table = table.fetchall()
    id_category = table[int(number)][0]
    name = table[int(number)][1]

    data = db.execute(
        "SELECT produkt.název, produkt.výrobce from kategorie,produkt where kategorie.id_kategorie = produkt.id_kategorie and produkt.id_kategorie=?",
        (id_category,))
    data = data.fetchall()

    return render_template('categories/one_category.html', data=data, name=name)


@bp.post("/one_category")
def one_categories():
    return (url_for('categories.one_category'))