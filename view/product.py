import functools
from flask import Flask, render_template, request, redirect, url_for, flash, session,Blueprint
from database import database
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from database.database import get_db
from user import User

bp = Blueprint('product', __name__, url_prefix='/product')


@bp.get('/')
def product():
    if current_user.is_authenticated:
        if current_user.role == 1:
            show = True
        elif current_user.role == 2:
            show = False
    else:
        show = False

    statement = "with data as(SELECT produkt.id_produktu, produkt.název, cena, dokdy, id_kategorie FROM produkt LEFT " \
                "OUTER JOIN historie_ceny hc on produkt.id_produktu = hc.id_produktu GROUP BY produkt.id_produktu " \
                "HAVING max(dokdy) or cena is null) SELECT produkt.id_produktu, produkt.název,výrobce," \
                "kategorie.název, cena FROM produkt,kategorie,data WHERE 'data'.id_produktu = produkt.id_produktu and " \
                "('data'.id_kategorie = kategorie.id_kategorie or 'data'.id_kategorie = 0) GROUP BY 'data'.id_produktu "
    db = get_db()
    table = db.execute(statement)
    data = table.fetchall()

    kategorie = db.execute("SELECT název FROM kategorie")
    kategorie = kategorie.fetchall()
    return render_template('/product/product.html', database=data, show_it=show, kategorie=kategorie)


@bp.post('/')
def products():
    data = request.form
    if data.get('delete') is not None:
        db = get_db()
        table = db.execute("SELECT id_produktu FROM produkt")
        table = table.fetchall()
        id_produktu = table[int(data.get('delete'))][0]
        db.execute("DELETE FROM produkt WHERE id_produktu=?", (id_produktu,))
        db.commit()

    elif data.get('one_product') is not None:
        number = int(data['one_product'])
        db = get_db()
        table = db.execute('SELECT * FROM produkt')
        table = table.fetchall()
        id_produktu = table[number][0]

        return redirect(url_for('product.one_product', id=id_produktu))

    else:
        db = get_db()
        cat_index = data['kategorie']
        table = db.execute("SELECT název FROM kategorie")
        cat = table.fetchall()[int(cat_index)]
        cat = cat[0]

        categories = db.execute('SELECT id_kategorie FROM kategorie WHERE název=?', (str(cat),))
        categories = categories.fetchone()[0]
        if data['name'] != None and data['vyrobce']:
            db.execute("INSERT INTO produkt (název, výrobce,id_kategorie) VALUES (?,?,?)",
                       (data['name'], data['vyrobce'], categories))
            db.commit()
    return redirect(url_for('product.product'))


@bp.get('/one_product')
def one_product():
    number = int(request.args.get('id'))
    print(number)
    db = get_db()
    command = f'SELECT * from produkt LEFT JOIN historie_ceny hc on produkt.id_produktu = hc.id_produktu where produkt.id_produktu =?'
    table = db.execute(command, (number,))
    table = table.fetchall()

    command2 = "SELECT kategorie.název from kategorie,produkt where produkt.id_kategorie = kategorie.id_kategorie and produkt.id_produktu=?"
    kategorie = db.execute(command2, (number,))
    kategorie = kategorie.fetchall()[0][0]
    return render_template('product/one_product.html', data=table, kategorie=kategorie)


@bp.post('one_product')
def one_products():
    return redirect(url_for('product.one_product'))
