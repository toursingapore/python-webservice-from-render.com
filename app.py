from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    celsius = str(escape(request.args.get("celsius", "")))
    return (
        """<form action="" method="get">
                <input type="text" name="celsius">
                <input type="submit" value="Convert">
            </form>"""
        + celsius
    )

@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return str(fahrenheit)


if __name__ == "__main__":
    app.run(debug=True)
