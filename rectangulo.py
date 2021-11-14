from flask import Blueprint, render_template, abort, session, request, redirect, url_for, flash
import MetodosMath.Rectangulo as rectangulo

rectanguloBP = Blueprint('rectanguloBP', __name__,
                      template_folder='templates')


@rectanguloBP.route('/rectangulo', methods=["GET", "POST"])
def showr():
    if request.method == 'POST':
        l1 = request.form['l1']
        l2 = request.form['l2']
        print(rectangulo.area(float(l1), float(l2)))
        print(rectangulo.perimetro(float(l1), float(l2)))
        return redirect(url_for('rectanguloBP.showir',
                                area=rectangulo.area(float(l1), float(l2)),
                                perimetro=rectangulo.perimetro(float(l1), float(l2))))

    return render_template("Rectangulo.html")


@rectanguloBP.route('/InfoRectangulo//<area>/<perimetro>', methods=["GET"])
def showir(area, perimetro):
    return render_template("FiguraResultado.html", area=area, perimetro=perimetro, type="rectangulo", BP=rectanguloBP)