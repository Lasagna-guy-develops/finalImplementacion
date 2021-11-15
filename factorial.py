from flask import Blueprint, render_template, abort, session, request, redirect, url_for
import MetodosMath.Factorial as factorial

factorialBP = Blueprint('factorialBP', __name__,
                        template_folder='templates')


@factorialBP.route('/factorial', methods=["GET", "POST"])
def showf():
    error = None
    if request.method == 'POST':
        fact = request.form['fact']
        try:
            fact=int(fact)
            if(fact>0):
                return redirect(url_for('factorialBP.showif',
                                        valor=factorial.factorial(fact)))
            else:
                error = 'El número debe ser mayor a 0'
        except Exception as e:
            error = 'El número debe ser entero'

    return render_template("Factorial.html", error=error)


@factorialBP.route('/InfoFactorial//<valor>', methods=["GET"])
def showif(valor):
    return render_template("FacResultado.html", valor=valor)
