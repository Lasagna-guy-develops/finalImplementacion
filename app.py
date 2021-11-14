from flask import Flask, render_template
import circulo, factorial, fibonacci, rectangulo, triangulo

app = Flask(__name__)
app.register_blueprint(factorial.factorialBP)
app.register_blueprint(circulo.circuloBP)
app.register_blueprint(triangulo.trianguloBP)
app.register_blueprint(rectangulo.rectanguloBP)
app.register_blueprint(fibonacci.fibonacciBP)

@app.route('/')
def menu():  # put application's code here
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)