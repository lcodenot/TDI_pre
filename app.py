from flask import Flask, render_template,request,redirect
import requests
import pandas as pd
import numpy as np
import quandl as Qd
import os
import time
from bokeh.io import curdoc
from bokeh.layouts import row, column, gridplot
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import PreText, Select
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components,file_html
from os.path import dirname, join

app = Flask(__name__)



tick = 'FB'
api_url = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?date.gte=20170501&date.lt=20170601&ticker=%s&api_key=TNvqvN5w-dbDua3bVNzk' %tick

r = requests.get(api_url)
data = r.json()
df = pd.DataFrame(data['datatable']['data']) 

df_important= df[[1,5,12,2,9]]
df_important.columns = ['date','close','adjusted close','open','adjusted open']
df_important['date'] = df_important['date'].astype('datetime64[ns]')

@app.route('/')
def main():
  return redirect('/plot')

@app.route('/plot')
def plot():
  p = figure(plot_width = 500, plot_height = 500, title='Data from Quandle WIKI set', x_axis_label='date', x_axis_type='datetime')
  r = p.line(df_important['date'],df_important['close'], line_width = 1)
  script, div = components(p)
  return render_template('graph.html', script=script, div=div)


if __name__ == '__main__':
  app.run(port=33507)