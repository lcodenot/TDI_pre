from flask import Flask, render_template, request, redirect
import pandas as pd
import requests

import sys

from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row
from bokeh.plotting import figure
from bokeh.embed import components 
output_notebook()

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')
    
    

if __name__ == '__main__':
     app.run(host='0.0.0.0') 
    #app.run(port=33507)