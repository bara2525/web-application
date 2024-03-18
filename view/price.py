import functools
from flask import Flask, render_template, request, redirect, url_for, flash, session,Blueprint
from database import database
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from database.database import get_db
from user import User

bp = Blueprint('price', __name__, url_prefix='/price')

@bp.get('/')
def price():
    if current_user.is_authenticated:
        if current_user.role == 1:
            show = True
        elif current_user.role == 2:
            show = False
    else:
        show = False

    db = get_db()
    command = "SELECT id_ceny, název, cena, odkdy, dokdy, komentář FROM historie_ceny, produkt WHERE historie_ceny.id_produktu = produkt.id_produktu"
    table = db.execute(command)
    data = table.fetchall()

    products = db.execute("SELECT název FROM produkt")
    products = products.fetchall()
    return render_template('price/price.html', neco=data, show_it=show, product=products)


@bp.post('/')
def prices():
    data = request.form

    if data.get('delete') is not None:
        db = get_db()
        db = db.execute("SELECT * FROM historie_ceny")
        table = db.fetchall()
        number = int(data.get('delete'))
        id_price = table[int(number)][0]
        db1 = get_db()
        db1.execute("DELETE FROM historie_ceny WHERE id_ceny=?", (id_price,))
        db1.commit()
        return redirect(url_for('price.price'))
    else:
        id_of_product = data.get('produkt')

        db = get_db()
        table = db.execute("SELECT název FROM produkt")
        name = table.fetchall()[int(id_of_product)][0]
        product_id = db.execute("SELECT id_produktu FROM produkt WHERE název=? ", (name,))
        if product_id is not None:
            id = product_id.fetchone()[0]
            db.execute("INSERT INTO historie_ceny (odkdy, dokdy, cena, komentář, id_produktu) VALUES (?,?,?,?,?)",
                       (data.get('datumod'), data.get('datumdo'), data.get('cena'), data.get('komentar'), id,))
            db.commit()
        return redirect(url_for('price.price'))