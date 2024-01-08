#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<p>Printed string: {parameter}</p>'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers= '\n'.join(str(i) for i in range(1, parameter +1))
    return f'<pre>{numbers}</pre>'

@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    result=0
    if operation == '+':
        result= num1 + num2
    elif operation == '-':
        result = num1-num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<p>Error: Division by zero</p>'
    elif operation == '%':
        result = num1 % num2

    return f'<p>Result of {num1} {operation} {num2} : {result}</p>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
