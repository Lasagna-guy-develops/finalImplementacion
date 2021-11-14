from flask import Blueprint, render_template, abort, session, request, redirect, url_for
import MetodosMath.Fibonacci as fibonacci

fibonacciBP = Blueprint('fibonacciBP', __name__,
                        template_folder='templates')


@fibonacciBP.route('/fibonacci', methods=["GET", "POST"])
def showfi():
    if request.method == 'POST':
        fibo = request.form['fibo']
        return redirect(url_for('fibonacciBP.showifi',
                                valores=fibonacci.fib(int(fibo))))

    return render_template("Fibonacci.html")


@fibonacciBP.route('/InfoFibonacci//<valores>', methods=["GET"])
def showifi(valores):
    valores = valores[1:-1]
    valores = valores.split(',')
    return render_template("FibResultado.html", valores=valores)