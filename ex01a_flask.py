from flask import Flask
app = Flask(__name__)
from templates import *

def soma(a,b):
    tot = a + b
    return tot

@app.route("/pag1")
def outra():
    return template4

    
@app.route("/")
def index():
    """
    index
    """
    a = 1
    b = 2
    c = soma(a,b)
    #return template1 % (a,b,c)
    #return template2.format(a,b,c)
    return template3.format(num1=a,num2=b,total=c)

if __name__ == "__main__":
    app.run()


