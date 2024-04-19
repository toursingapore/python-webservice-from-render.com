from flask import Flask
from flask import request, escape

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


if __name__ == "__main__":
    app.run(debug=True)
