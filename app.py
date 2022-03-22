# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import sqlite3

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
  "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
  "Amount": [4, 1, 2, 2, 4, 5],
  "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

con = sqlite3.connect('./database/db.sqlite')

df = pd.read_sql('SELECT possui_depressao FROM dataset_depressao', con)
print(df.head())
df_group = df.groupby(['possui_depressao']).size().reset_index(name='counts')
print(df_group.head())
fig = px.bar(df_group, x="possui_depressao", y="counts", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Promental'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='bar-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
