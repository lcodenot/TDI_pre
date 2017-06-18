from flask import Flask, render_template, request, redirect
import pandas as pd
import requests

import sys

from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row
from bokeh.plotting import figure
from bokeh.embed import components 
output_notebook()

response = raw_input("Insert Tick i.e. GOOG: ")

def picture(tick):
    api_url = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?date.gte=20170501&date.lt=20170601&ticker=%s&api_key=TNvqvN5w-dbDua3bVNzk' %tick

    r = requests.get(api_url)
    data = r.json()
    df = pd.DataFrame(data['datatable']['data']) 

    df_important= df[[1,5,12,2,9]]
    df_important.columns = ['date','close','adjusted close','open','adjusted open']

    p = figure(plot_width = 500, plot_height = 500, title='Data from Quandle WIKI set', x_axis_label='date', x_axis_type='datetime')
    r = p.line(df_important['date'],df_important['close'], line_width = 1)
    #t = show(p, notebook_handle = True)
    script, div = components(p)
    return render_template('graph.html', script=script, div=div)

picture(response)
