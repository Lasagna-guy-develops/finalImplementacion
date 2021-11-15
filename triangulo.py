from flask import Blueprint, render_template, abort, session, request, redirect, url_for
import MetodosMath.Triangulo as triangulo

trianguloBP = Blueprint('trianguloBP', __name__,
                        template_folder='templates')


@trianguloBP.route('/triangulo', methods=["GET", "POST"])
def showt():
    error = None
    if request.method == 'POST':
        l1 = request.form['l1']
        l2 = request.form['l2']
        l3 = request.form['l3']
        try:
            l1 = float(l1)
            l2 = float(l2)
            l3 = float(l3)
            if (l1 < (l2 + l3)) and (l2 < (l1 + l3)) and (l3 < (l1 + l2)):
                return redirect(url_for('trianguloBP.showit',
                                        area=triangulo.area(l1, l2, l3),
                                        perimetro=triangulo.perimetro(l1, l2, l3)))
            elif (l1 > 0 and l2 > 0 and l3 > 0):
                error = 'valores deben ser mayores a 0'
            else:
                error = 'Datos equivocados, desigualdad de triangulos'

        except Exception as e:
            error = 'Valores deben ser números mayores a 0'

    return render_template("Triangulo.html", error=error)


@trianguloBP.route('/InfoTriangulo/<area>/<perimetro>', methods=["GET"])
def showit(area, perimetro):
    return render_template("FiguraResultado.html", area=area, perimetro=perimetro, type="triangulo", BP=trianguloBP)
