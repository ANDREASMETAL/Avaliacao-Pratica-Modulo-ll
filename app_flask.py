from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.

@app.route("/soma")
def soma():
    n1 = float(request.args.get("valor1"))
    n2 = float(request.args.get("valor2"))
    return {'resultado': n1 + n2}

@app.route("/subtrair")
def subtrair():
    n1 = float(request.args.get("valor1"))
    n2 = float(request.args.get("valor2"))
    return {'resultado': n1 - n2}

@app.route("/multiplicar")
def multiplicar():
    n1 = float(request.args.get("valor1"))
    n2 = float(request.args.get("valor2"))
    return {'resultado': n1 * n2}


@app.route("/dividir")
def dividir():
    n1 = float(request.args.get("valor1"))
    n2 = float(request.args.get("valor2"))
    if n2 == 0: 
        return{"erro":"divisão por zero não e permitida"}
    return {'resultado': n1 / n2}


if __name__ == "__main__":
    app.run(debug=True)
