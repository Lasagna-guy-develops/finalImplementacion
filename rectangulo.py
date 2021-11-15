from flask import Blueprint, render_template, abort, session, request, redirect, url_for, flash
import MetodosMath.Rectangulo as rectangulo

rectanguloBP = Blueprint('rectanguloBP', __name__,
                      template_folder='templates')


@rectanguloBP.route('/rectangulo', methods=["GET", "POST"])
def showr():
    error = None
    if request.method == 'POST':
        l1 = request.form['l1']
        l2 = request.form['l2']
        try:
            l1 = float(l1)
            l2 = float(l2)
            if(l1>0 and l2>0):
                return redirect(url_for('rectanguloBP.showir',
                                        area=rectangulo.area(l1, l2),
                                        perimetro=rectangulo.perimetro(l1, l2)))
            else:
                error = 'Valores deben ser mayores a 0'
        except Exception as e:
            error = 'Valores deben ser números mayores a 0'

    return render_template("Rectangulo.html", error=error)


@rectanguloBP.route('/InfoRectangulo//<area>/<perimetro>', methods=["GET"])
def showir(area, perimetro):
    return render_template("FiguraResultado.html", area=area, perimetro=perimetro, type="rectangulo", BP=rectanguloBP)