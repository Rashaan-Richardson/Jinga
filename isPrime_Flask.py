import math
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"
@app.route('/user/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/number/<name>')
def prime_number(name):
    return f"<h1>{name} is prime</h1>" if isPrimeLC(name) else f"<h4>{name} is NOT prime</h4>"

def isPrimeLC(num):
    num = int(num)
    return False if num < 2 or [False for x in range(2,int(math.sqrt(num))+1) if num % x == 0  ] else True
    
@app.route('/factors/<name>')    # <----- New endpoint
def get_factors(name):
    name = int(name)
    return f"<h1>The factors of {name} are {[x for x in range(1,name+1) if name % x == 0  ]}</h1>"

if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=4000)