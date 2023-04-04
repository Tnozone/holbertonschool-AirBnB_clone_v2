#!/usr/bin/python3
""" script that starts a Flask web application """


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbhn():
    """displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """display C url"""
    return "c {}".format(text.replace('_', ' ')).capitalize()


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythontext(text):
    """display Python url"""
    return "python {}".format(text.replace('_', ' ')).capitalize()


@app.route("/number/<int:n>", strict_slashes=False)
def printn(n):
    """display n if int"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def print_num_template(n):
    """display html page"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def oddoreven(n):
    """display html page"""
    if n % 2 == 0:
        result = "{} is even".format(n)
    else:
        result = "{} is odd".format(n)
    return render_template('6-number_odd_or_even.html', n=n, result=result))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
