from flask import Flask
from jinja2 import Template
import random
import os

os.chdir('/Users/rashaanrichardson/Desktop/SQL_Notes')

app = Flask(__name__) 

@app.route('/cost')
def greeting():
    x = """
<p>{{func(tax=8.78)}}</b></p>
"""
    template = Template(x)
    return template.render(func=get_item_cost)

def get_item_cost(**kwargs):
    print(kwargs)
    i = random.choice(['Soda','Bread','Water','Kombucha','Fiji Water'])
    tax = kwargs['tax']
    item_cost = {'Soda':1.99,
                'Bread': 4.99,
                'Water': 1.00,
                'Kombucha': 3.99}
    return f'{i} cost = ${round(item_cost.get(i)*float(1 + (tax/100)),2)}' if item_cost.get(i) else f'Price Check for {i} !!!'
    
if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=5000)