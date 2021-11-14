from flask import Blueprint, render_template, abort, session, request, redirect, url_for
import MetodosMath.Triangulo as triangulo

trianguloBP = Blueprint('trianguloBP', __name__,
                      template_folder='templates')


@trianguloBP.route('/triangulo', methods=["GET", "POST"])
def showt():
    if request.method == 'POST':
        l1 = request.form['l1']
        l2 = request.form['l2']
        l3 = request.form['l3']
        print(triangulo.area(float(l1), float(l2), float(l3)))
        print(triangulo.perimetro(float(l1), float(l2), float(l3)))
        return redirect(url_for('trianguloBP.showit',
                                area=triangulo.area(float(l1), float(l2), float(l3)),
                                perimetro=triangulo.perimetro(float(l1), float(l2), float(l3))))

    return render_template("Triangulo.html")


@trianguloBP.route('/InfoTriangulo/<area>/<perimetro>', methods=["GET"])
def showit(area, perimetro):
    return render_template("FiguraResultado.html", area=area, perimetro=perimetro, type="triangulo", BP=trianguloBP)