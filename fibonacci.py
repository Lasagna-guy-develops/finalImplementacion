from flask import Blueprint, render_template, abort, session, request, redirect, url_for
import MetodosMath.Fibonacci as fibonacci

fibonacciBP = Blueprint('fibonacciBP', __name__,
                        template_folder='templates')


@fibonacciBP.route('/fibonacci', methods=["GET", "POST"])
def showfi():
    error = None
    if request.method == 'POST':
        fibo = request.form['fibo']
        try:
            fibo=int(fibo)
            if(fibo>0):
                return redirect(url_for('fibonacciBP.showifi',
                                        valores=fibonacci.fib(fibo)))
            else:
                error = 'El número debe ser mayor a 0'
        except Exception as e:
            error = 'El número debe ser entero'

    return render_template("Fibonacci.html", error=error)


@fibonacciBP.route('/InfoFibonacci//<valores>', methods=["GET"])
def showifi(valores):
    valores = valores[1:-1]
    valores = valores.split(',')
    return render_template("FibResultado.html", valores=valores)