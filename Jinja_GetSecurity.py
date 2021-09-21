import datetime
from flask import Flask
import getpass
import glob
from jinja2 import Template
import logging
import pandas as pd
import math 
import mysql
import mysql.connector
import os
import sqlalchemy
import sqlite3
os.chdir('/Users/rashaanrichardson/Desktop/SQL_Notes')

app = Flask(__name__) 

@app.route('/')
def greeting():
    x = """
<p>Welcome to <b>Code Immersive {{func() }}</b></p>
"""
    template = Template(x)
    return template.render(func=get_security_info)
def get_user_name():
    return getpass.getuser()

def get_security_info():
    mydb = mysql.connector.connect(
    host="localhost",
    user="Rashaan05",
    passwd="rich@rdson"
    )
    cur = mydb.cursor()

    cur.execute('USE final_project;')
    trade_date = '2011-08-11'
    symbol = 'AXP'
    sql = f''' select closing_price from sec_master where trade_date = '{trade_date}' and symbol = '{symbol}' '''
    print(sql)
    cur.execute(sql)
    l = cur.fetchall()
    print(l)
    # or
    for x in l:
        print(x)
    return float(x[0])

if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=5000)