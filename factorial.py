from flask import Blueprint, render_template, abort, session, request, redirect, url_for
import MetodosMath.Factorial as factorial

factorialBP = Blueprint('factorialBP', __name__,
                        template_folder='templates')


@factorialBP.route('/factorial', methods=["GET", "POST"])
def showf():
    if request.method == 'POST':
        fact = request.form['fact']
        return redirect(url_for('factorialBP.showif',
                                valor=factorial.factorial(int(fact))))

    return render_template("Factorial.html")


@factorialBP.route('/InfoFactorial//<valor>', methods=["GET"])
def showif(valor):
    return render_template("FacResultado.html", valor=valor)
