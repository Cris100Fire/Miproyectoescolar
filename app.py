from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    steps = None

    if request.method == "POST":
        operation = request.form.get("operation")
        base = float(request.form.get("base"))
        numero1 = float(request.form.get("numero1"))
        numero2 = request.form.get("numero2")
        exponente = request.form.get("exponente")

        try:
            if operation == "simple":
                result = math.log(numero1, base)
                steps = (
                    f"Paso 1: log₍{base}₎({numero1})\n"
                    f"Paso 2: ¿Cuál es el exponente x tal que {base}^x = {numero1}?\n"
                    f"Paso 3: log₍{base}₎({numero1}) = {base}^x = {numero1} → x = {result:.2f}"
                )

            elif operation == "producto":
                numero2 = float(numero2)
                log1 = math.log(numero1, base)
                log2 = math.log(numero2, base)
                result = log1 + log2
                steps = (
                    f"Paso 1: log₍{base}₎({numero1} × {numero2})\n"
                    f"Paso 2: log₍{base}₎({numero1}) + log₍{base}₎({numero2})\n"
                    f"Paso 3: {log1:.2f} + {log2:.2f} = {result:.2f}"
                )

            elif operation == "cociente":
                numero2 = float(numero2)
                log1 = math.log(numero1, base)
                log2 = math.log(numero2, base)
                result = log1 - log2
                steps = (
                    f"Paso 1: log₍{base}₎({numero1} ÷ {numero2})\n"
                    f"Paso 2: log₍{base}₎({numero1}) - log₍{base}₎({numero2})\n"
                    f"Paso 3: {log1:.2f} - {log2:.2f} = {result:.2f}"
                )

            elif operation == "potencia":
                exponente = float(exponente)
                logn = math.log(numero1, base)
                result = exponente * logn
                steps = (
                    f"Paso 1: log₍{base}₎({numero1}^{exponente})\n"
                    f"Paso 2: {exponente} × log₍{base}₎({numero1})\n"
                    f"Paso 3: {exponente} × {logn:.2f} = {result:.2f}"
                )

            elif operation == "cambio_base":
                exponente = float(exponente)  # b
                result = (1 / exponente) * math.log(numero1, base)
                steps = (
                    f"Paso 1: log₍{base}^{exponente}₎({numero1})\n"
                    f"Paso 2: (1/{exponente}) × log₍{base}₎({numero1})\n"
                    f"Paso 3: (1/{exponente}) × {math.log(numero1, base):.2f} = {result:.2f}"
                )

            elif operation == "logaritmos_encadenados":
                s = float(numero1)
                r = float(numero2)
                c = float(exponente)
                result = math.log(c, base)
                steps = (
                    f"Paso 1: log₍{base}₎({s}) × log₍{s}₎({r}) × log₍{r}₎({c})\n"
                    f"Paso 2: Aplicando la propiedad encadenada:\n"
                    f"Paso 3: log₍{base}₎({c}) = {result:.2f}"
                )

            elif operation == "cologaritmo":
                result = math.log(1 / numero1, base)
                steps = (
                    f"Paso 1: colog₍{base}₎({numero1}) = log₍{base}₎(1/{numero1})\n"
                    f"Paso 2: log₍{base}₎({1/numero1:.4f}) = {result:.2f}"
                )

            elif operation == "antilogaritmo":
                result = base ** numero1
                steps = (
                    f"Paso 1: antilog₍{base}₎({numero1}) = {base}^{numero1}\n"
                    f"Paso 2: Resultado = {result:.2f}"
                )

        except ValueError:
            result = "Entrada no válida. Verifica que los números sean positivos y que la base sea válida."
            steps = ""

    return render_template("index.html", result=result, steps=steps)

if __name__ == "__main__":
    app.run(debug=True)