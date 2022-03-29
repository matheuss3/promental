# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import sqlite3
import numpy as np

app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

con = sqlite3.connect('./database/db.sqlite')

df = pd.read_sql('SELECT * FROM dataset_depressao', con)
df_group = df.groupby(['possui_depressao', 'sexo']).size().reset_index(name='counts')
fig = px.bar(df_group, x="possui_depressao", title='Casos positivos e negativos x sexo', 
            y="counts", color='sexo', barmode="group")


df_year_graph = df.groupby(['idade', 'possui_depressao']).size().reset_index(name='counts')
fig2 = px.line(df_year_graph, x='idade', y='counts', color='possui_depressao', title='Quantidade de positivos e negativos x Idade')

fig3 = go.Figure()



fig3.add_trace(go.Indicator(
            value = len(df),
            mode = 'number',
            title='Qtd pessoas avaliadas',
            domain = {'x': [0, 0.33], 'y': [0, 1]}
        ))

fig3.add_trace(go.Indicator(
            value = len(df[df['possui_depressao'] == 'POSSUI']),
            mode = 'number',
            title='Qtd pessoas com depressao',
            domain = {'x': [0.33, 0.66], 'y': [0, 1]}
        ))

fig3.add_trace(go.Indicator(
            value = len(df[df['possui_depressao'] == 'POSSUI']) / len(df) * 100,
            mode = 'number',
            title='%',
            domain = {'x': [0.66, 1], 'y': [0, 1]}
        ))
fig3.update_layout(
    height=200,
    margin= { 't': 75, 'r': 75, 'l': 75, 'b': 75 }
)
app.layout = dbc.Container([
    html.H1(children='Promental'),

    html.Div(children='''
        Dashboard desenvolvido para visualização de dados do Promental
    '''),

    html.Div([
    dbc.Card(
        dbc.CardBody([
            dcc.Graph(
            id='indicators',
            figure=fig3
        ),
            dbc.Row(
                [
                    dbc.Col([
                        html.Div([
                            dbc.Card(
                                dbc.CardBody([
                                    dcc.Graph(
                                        id='bar-graph',
                                        figure=fig
                                    )
                                ])
                            )
                        ])

                    ], width=3),
                    dbc.Col([
                        html.Div([
                            dbc.Card(
                                dbc.CardBody([
                                    dcc.Graph(
                                        id='line-graph',
                                        figure=fig2
                                    )
                                ])
                            )
                        ])

                    ], width=9),
                ]
            )]))])
], fluid=True,)

if __name__ == '__main__':
    app.run_server(debug=True)
