from flask import Flask
app = Flask(__name__)

@app.route('/')
#def hello_world():
#    return 'Hello World, welcome to you!'

def my_func_doing(number1, number2):
    return number1 + number2

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
solution = do_calculation(number1, number2)
print("The sum of your numbers is {}".format(solution))


if __name__ == "__main__":
    app.run(debug=True)
