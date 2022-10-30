# Put"""Basic math operations."""
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)
@app.route("/add")
def add(a, b):
    """Add a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    return a + b
@app.route("/sub")
def sub(a, b):
    """Substract b from a."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return a - b

@app.route("/mult")
def mult(a, b):
    """Multiply a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return a * b

@app.route("/div")
def div(a, b):
    """Divide a by b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return a / b your app in here.
