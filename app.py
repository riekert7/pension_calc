from flask import Flask, render_template, request
from calculator import calculate_projection, summarise

app = Flask(__name__)

CURRENCIES = [
    ("GBP", "£"),
    ("ZAR", "R"),
    ("USD", "$"),
    ("EUR", "€"),
    ("AUD", "A$"),
]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", currencies=CURRENCIES)


@app.route("/calculate", methods=["POST"])
def calculate():
    errors = {}

    try:
        current_age = int(request.form["current_age"])
    except (ValueError, KeyError):
        errors["current_age"] = "Please enter a valid age."

    try:
        retirement_age = int(request.form["retirement_age"])
    except (ValueError, KeyError):
        errors["retirement_age"] = "Please enter a valid retirement age."

    try:
        current_balance = float(request.form["current_balance"])
        if current_balance < 0:
            errors["current_balance"] = "Balance cannot be negative."
    except (ValueError, KeyError):
        errors["current_balance"] = "Please enter a valid balance."

    try:
        annual_contribution = float(request.form["annual_contribution"])
        if annual_contribution < 0:
            errors["annual_contribution"] = "Contribution cannot be negative."
    except (ValueError, KeyError):
        errors["annual_contribution"] = "Please enter a valid contribution."

    try:
        growth_rate = float(request.form["growth_rate"])
        if not (0 <= growth_rate <= 30):
            errors["growth_rate"] = "Growth rate must be between 0% and 30%."
    except (ValueError, KeyError):
        errors["growth_rate"] = "Please enter a valid growth rate."

    currency_code = request.form.get("currency", "GBP")
    currency_symbol = dict(CURRENCIES).get(currency_code, "£")

    if not errors:
        if retirement_age <= current_age:
            errors["retirement_age"] = (
                "Retirement age must be greater than current age."
            )

    if errors:
        return render_template(
            "index.html", currencies=CURRENCIES, errors=errors, form_data=request.form
        )

    results = calculate_projection(
        current_age, retirement_age, current_balance, annual_contribution, growth_rate
    )
    summary = summarise(results, currency_symbol)

    return render_template(
        "results.html",
        results=results,
        summary=summary,
        currency_symbol=currency_symbol,
        inputs=request.form,
    )


if __name__ == "__main__":
    app.run(debug=True)
