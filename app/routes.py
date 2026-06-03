from flask import Blueprint, render_template, request
from app.calculadora import Calculadora

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None
    numero1 = ""
    numero2 = ""
    operacao = "somar"

    if request.method == "POST":
        numero1 = request.form.get("numero1", "")
        numero2 = request.form.get("numero2", "")
        operacao = request.form.get("operacao", "somar")

        try:
            a = float(numero1)
            b = float(numero2)
            calc = Calculadora()

            if operacao == "somar":
                resultado = calc.somar(a, b)
            elif operacao == "subtrair":
                resultado = calc.subtrair(a, b)
            elif operacao == "multiplicar":
                resultado = calc.multiplicar(a, b)
            elif operacao == "dividir":
                resultado = calc.dividir(a, b)
            else:
                erro = "Operação inválida."
        except ValueError as e:
            erro = str(e)

    return render_template(
        "index.html",
        resultado=resultado,
        erro=erro,
        numero1=numero1,
        numero2=numero2,
        operacao=operacao,
    )


@bp.route("/health")
def health():
    return {"status": "ok"}, 200
