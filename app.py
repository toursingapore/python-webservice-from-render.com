from flask import Flask
app = Flask(__name__)

@app.route('/')
#def hello_world():
#    return 'Hello World, welcome to you!'
    return '''
        <html>
            <body>
                {errors}
                <p>Enter your numbers:</p>
                <form method="post" action=".">
                    <p><input name="number1" /></p>
                    <p><input name="number2" /></p>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)


if __name__ == "__main__":
    app.run(debug=True)
