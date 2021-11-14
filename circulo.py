from flask import Blueprint, render_template, abort, session, request, redirect, url_for
import MetodosMath.Circulo as circulo

circuloBP = Blueprint('circuloBP', __name__,
                      template_folder='templates')


@circuloBP.route('/circulo', methods=["GET", "POST"])
def showc():
    if request.method == 'POST':
        radio = request.form['radio']
        print(circulo.area(float(radio)))
        print(circulo.perimetro(float(radio)))
        return redirect(url_for('circuloBP.showic',
                                area=circulo.area(float(radio)),
                                perimetro=circulo.perimetro(float(radio))))

    return render_template("Circulo.html")


@circuloBP.route('/InfoCirculo//<area>/<perimetro>', methods=["GET"])
def showic(area, perimetro):
    return render_template("FiguraResultado.html", area=area, perimetro=perimetro, type="circulo", BP=circuloBP)
