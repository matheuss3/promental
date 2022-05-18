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

con = sqlite3.connect('../data/db.sqlite')

df = pd.read_sql('SELECT * FROM dataset_depressao', con)
df_group = df.groupby(['possui_depressao', 'sexo']).size().reset_index(name='counts')
fig = px.bar(df_group, x="possui_depressao", title='Casos positivos e negativos x sexo', 
            y="counts", color='sexo', barmode="group")


df_year_graph = df.groupby(['idade', 'possui_depressao']).size().reset_index(name='counts')
fig2 = px.bar(df_year_graph, x='idade', y='counts', title='Quantidade de pessoas entrevistadas x Idade')

df_graph_year_depression = df[df['possui_depressao'] == 'POSSUI'].groupby(['idade', 'possui_depressao']).size().reset_index(name='counts')
fig4 = px.bar(df_graph_year_depression, x='idade', y='counts', title='Quantidade de casos por idade')

fig5 = px.scatter_matrix(df,
    dimensions=['sexo', 'idade', 'fumante', 'saude_fisica'],
    color='possui_depressao')

fig3 = go.Figure()

fig3.add_trace(go.Indicator(
            value = len(df),
            mode = 'number',
            title='Pessoas avaliadas',
            domain = {'x': [0, 0.33], 'y': [0, 1]}
        ))

fig3.add_trace(go.Indicator(
            value = len(df[df['possui_depressao'] == 'POSSUI']),
            mode = 'number',
            title='Depressivos',
            domain = {'x': [0.33, 0.66], 'y': [0, 1]}
        ))

fig3.add_trace(go.Indicator(
            value = len(df[df['possui_depressao'] == 'POSSUI']) / len(df) * 100,
            mode = 'number',
            title='%',
            domain = {'x': [0.66, 1], 'y': [0, 1]}
        ))
fig3.update_layout(
)
app.layout = dbc.Container([
    html.H1(children='🧠 Promental'),

    html.P(children='''
        Dashboard criado para visualização de dados do Promental
    '''),

    html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id='indicators',
                    figure=fig3
                ),
            dbc.Row([
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
                                        id='histogram',
                                        figure=fig2
                                    )
                                ])
                            )
                        ])

                    ], width=9),
                ]
            )])),
            html.Div([
                            dbc.Card(
                                dbc.CardBody([
                                    dcc.Graph(
                                        id='line-graph',
                                        figure=fig4
                                    )
                                ])
                            )
                        ]),
                        html.Div([
                            dbc.Card(
                                dbc.CardBody([
                                    dcc.Graph(
                                        id='pairplot-graph',
                                        figure=fig5
                                    )
                                ])
                            )
                        ])])
], fluid=True,)

if __name__ == '__main__':
    app.run_server(debug=True)
