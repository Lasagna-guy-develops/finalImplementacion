from flask import Blueprint, render_template, abort, session, request, redirect, url_for
import MetodosMath.Circulo as circulo

circuloBP = Blueprint('circuloBP', __name__,
                      template_folder='templates')


@circuloBP.route('/circulo', methods=["GET", "POST"])
def showc():
    error = None
    if request.method == 'POST':
        radio = request.form['radio']
        try:
            radio=float(radio)
            if radio > 0:
                return redirect(url_for('circuloBP.showic',
                                        area=circulo.area(radio),
                                        perimetro=circulo.perimetro(radio)))
            else:
                error = 'El radio debe ser mayor a 0'
        except Exception as e:
            error = 'El radio debe ser un número mayor a 0'

    return render_template("Circulo.html", error=error)


@circuloBP.route('/InfoCirculo//<area>/<perimetro>', methods=["GET"])
def showic(area, perimetro):
    return render_template("FiguraResultado.html", area=area, perimetro=perimetro, type="circulo", BP=circuloBP)
