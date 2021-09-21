from flask import Flask
from jinja2 import Template
import random
import os

os.chdir('/Users/rashaanrichardson/Desktop/SQL_Notes')

app = Flask(__name__) 

@app.route('/')
def greeting():
    store_purchase = random.choice(['Soda','Bread','Water','Kombucha','Fiji Water'])
    x = """
<p>{{func(item)}}</b></p>
"""
    template = Template(x)
    return template.render(func=get_item_cost, item =store_purchase )

def get_item_cost(i):
    item_cost = {'Soda':1.99,
                'Bread': 4.99,
                'Water': 1.00,
                'Kombucha': 3.99}
    return f'{i} cost = ${item_cost.get(i)}' if item_cost.get(i) else f'Price Check for {i} !!!'
    
if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=5000)