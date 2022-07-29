import dash
import dash_bootstrap_components as dbc
import tkinter as tk
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output, State

import plotly.express as px
import pandas as pd
import numpy as np
from dash import Dash, dcc, html, Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# -- Styles
COLORS = {
    'background': '#C0C0C0',
    'text': '#7FDBFF'
}

TOP_DROPDOWN_STYLE = {
    'margin-left': '10px',
    'margin-right': '10px',
    'width': "200px",
    'display': 'auto'
}

TEXT_STYLE = {
    'margin-left': '20px',
    'margin-right': '10px'
}

HEADING_STYLE = {
    'font-family': "'Gill Sans', sans-serif",
    'font-size': '40px',
    'font-weight': '300',
    'textAlign': 'center',
    'padding': '20px',
    'color': '#F5F5F5',
    'background-color': '#417dc1'
}

SUB_HEADING_STYLE = {
    'font-family': "'Gill Sans', sans-serif",
    'font-size': '20px',
    'padding': '15px',
    'border-top': '1px dashed grey'
}

SUB_HEADING_STYLE_GENRE = {
    'font-family': "'Gill Sans', sans-serif",
    'font-size': '20px',
    'padding': '15px',
}

PREDICTOR_HEADING_STYLE = {
    'font-family': "'Gill Sans', sans-serif",
    'font-size': '20px',
    'padding': '10px',
    'margin-left': '5px'
}

GRAPH_STYLE = {
    'plot_bgcolor': "#303030",
    'paper_bgcolor': "#303030",
    'width' : '500px',
    'margin-left' : '10px'
}

# -- Import our data
df = pd.read_csv('/Users/lewisaun/Documents/hackathon/content-value-predicting/data/joined_table.csv')

fig1 = px.histogram(df, x='genre', y='sales_revenue', labels={"genre": "Genre", "sales_revenue": "Sales Revenue"},color='genre')
fig2 = px.histogram(df, x='genre', y='n_views_pes', labels={"genre": "Genre", "n_views_pes": "Viewing Numbers (PES)"},color='genre')
fig3 = px.histogram(df, x='genre', y='averageRating', labels={"genre": "Genre", "sales_revenue": "Average IMDB Rating"},color='genre',
                    histfunc='avg')

start_year_df = df.copy()
start_year_df = start_year_df[start_year_df["startYear"] > 2017]

fig4 = px.histogram(start_year_df, x='startYear', y='sales_revenue',
                    labels={"startYear": "Start Year", "sales_revenue": "Sales Revenue"},color='startYear')
fig5 = px.histogram(start_year_df, x='startYear', y='n_views_pes',
                    labels={"startYear": "Start Year", "n_views_pes": "Viewing Numbers (PES)"},color='startYear')
fig6 = px.histogram(start_year_df, x='startYear', y='averageRating',
                    labels={"startYear": "Start Year", "sales_revenue": "Average IMDB Rating"},color='startYear', histfunc='avg')

fig1.update_layout(
    paper_bgcolor=COLORS['background'],
    showlegend=False
)
fig2.update_layout(
    paper_bgcolor=COLORS['background'],
    showlegend=False
)
fig3.update_layout(
    paper_bgcolor=COLORS['background'],
    showlegend=False
)
fig4.update_layout(
    paper_bgcolor=COLORS['background'],
    showlegend=False
)
fig5.update_layout(
    paper_bgcolor=COLORS['background'],
    showlegend=False
)
fig6.update_layout(
    paper_bgcolor=COLORS['background'],
    showlegend=False
)
# -- App Layout
app.layout = html.Div([

    html.H1("Content Value Analytics/Predictor", style=HEADING_STYLE),
    html.Div(id='output_container', children=[
        html.P('Analytics by Genre:', style=SUB_HEADING_STYLE_GENRE),
        dcc.Dropdown(id="genre",
                     options=[
                         {"label": "All", "value": "All"},
                         {"label": "Factual", "value": "Factual"},
                         {"label": "Drama", "value": "Drama"},
                         {"label": "Children", "value": "Children"},
                         {"label": "Entertainment", "value": "Entertainment"},
                         {"label": "Documentary", "value": "Documentary"},
                         {"label": "Comedy", "value": "Comedy"},
                         {"label": "Sport", "value": "Sport"},
                         {"label": "Short", "value": "Short"},
                         {"label": "Lifestyle", "value": "Lifestyle"}],
                     multi=False,
                     searchable=False,
                     value="All",
                     style={'width': '200px',
                            'padding-left': '10px',
                            'margin-bottom' : '20px'}
                     ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id='graph_1', figure=fig1, style=GRAPH_STYLE)
                ),
                dbc.Col(
                    dcc.Graph(id='graph_2', figure=fig2, style=GRAPH_STYLE)
                ),
                dbc.Col(
                    dcc.Graph(id='graph_3', figure=fig3, style=GRAPH_STYLE)
                ),
            ]
        ),
        html.P('Analytics by Start Year:', style=SUB_HEADING_STYLE),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id='graph_4', figure=fig4, style=GRAPH_STYLE)
                ),
                dbc.Col(
                    dcc.Graph(id='graph_5', figure=fig5, style=GRAPH_STYLE)
                ),
                dbc.Col(
                    dcc.Graph(id='graph_6', figure=fig6, style=GRAPH_STYLE)
                ),
            ]
        )
    ]),
    html.P('Predictor:', style=PREDICTOR_HEADING_STYLE),
    html.Div(id='dropdown-3', children=[
        dbc.Row(
            [html.Div(children=[
                html.H6("Genre", style=TEXT_STYLE),
                dcc.Dropdown(id="predictor-genre",
                             options=[
                                 {"label": "Drama", "value": "Drama"},
                                 {"label": "Factual", "value": "Factual"},
                                 {"label": "Documentary", "value": "Documentary"},
                                 {"label": "Entertainment", "value": "Entertainment"},
                                 {"label": "Comedy", "value": "Comedy"},
                                 {"label": "Crime", "value": "Crime"},
                                 {"label": "Reality-TV", "value": "Reality-TV"},
                                 {"label": "Sport", "value": "Sport"},
                                 {"label": "Game-Show", "value": "Game-Show"},
                                 {"label": "Short", "value": "Short"},
                                 {"label": "Family", "value": "Family"},
                                 {"label": "Childrens", "value": "Childrens"},
                                 {"label": "Adventure", "value": "Adventure"},
                                 {"label": "Mystery", "value": "Mystery"},
                                 {"label": "Action", "value": "Action"},
                                 {"label": "Science Fiction and Fantasy", "value": "Science Fiction and Fantasy"},
                                 {"label": "Thriller", "value": "Thriller"},
                                 {"label": "Wildlife and Environment", "value": "Wildlife and Environment"},
                                 {"label": "Romance", "value": "Romance"},
                                 {"label": "Animation", "value": "Animation"}],
                             multi=True,
                             searchable=False,
                             value="All",
                             style=TOP_DROPDOWN_STYLE
                             )]),
                html.Div(children=[
                    html.H6("Title Type", style=TEXT_STYLE),
                    dcc.Dropdown(id="predictor-title-type",
                                 options=[
                                     {"label": "Movie", "value": "Movie"},
                                     {"label": "Series", "value": "Series"},
                                     {"label": "Mini Series", "value": "Mini Series"},
                                     {"label": "Short", "value": "Short"}],
                                 multi=False,
                                 searchable=False,
                                 value="All",
                                 style=TOP_DROPDOWN_STYLE)]),
                html.Div(children=[
                    html.H6("Runtime", style=TEXT_STYLE),
                    dcc.Input(id="predictor-runtime",
                              type="number",
                              style=TOP_DROPDOWN_STYLE
                              )]),
                html.Div(children=[
                    html.H6("Synopsis", style=TEXT_STYLE),
                    dcc.Input(id="predictor-synopsis",
                              type="text",
                              style=TOP_DROPDOWN_STYLE)]),
                html.Div(children=[
                    html.H6("Title", style=TEXT_STYLE),
                    dcc.Input(id="predictor-title",
                              type="text",
                              style=TOP_DROPDOWN_STYLE)]),
                html.Div(children=[
                    html.H6("Gender", style=TEXT_STYLE),
                    dcc.Dropdown(id="predictor-gender",
                                 options=[
                                     {"label": "Men", "value": "Men"},
                                     {"label": "Women", "value": "Women"}],
                                 multi=False,
                                 searchable=False,
                                 style=TOP_DROPDOWN_STYLE
                                 )]),
                html.Div(children=[
                    html.H6("Target Age", style=TEXT_STYLE),
                    dcc.Dropdown(id="predictor-target-age",
                                 options=[
                                     {"label": "Children", "value": "Children"},
                                     {"label": "16-34", "value": "16-34"},
                                     {"label": "35-54", "value": "35-54"},
                                     {"label": "55+", "value": "55+"}],
                                 multi=False,
                                 searchable=False,
                                 style=TOP_DROPDOWN_STYLE
                                 )]),

            ], style={'padding-left': '10px'}),
        html.Button('Submit', id='predict-button', n_clicks=0, style={'margin-left': 'auto'
            , 'margin-right': 'auto'
            , 'width': '20%'
            , 'padding': '10px'
            , 'margin-top': '30px'
            , 'display': 'block'}),
        dbc.Row([
            html.Div([
                html.H6("Revenue:"),
                dcc.Input(
                    id='revenue-output',
                    style={'width': '300px'}
                ),
            ], style={'width': '20%',
                      'height': '30px',
                      'margin-left': 'auto',
                      'margin-right': 'auto',
                      'display': 'block',
                      'margin-top': '30px'
                , 'margin-bottom': '10px'}),
            html.Div([
                html.H6("Viewing Numbers (PES):"),
                dcc.Input(
                    id='viewing-output',
                    style={'width': '300px'}
                ),
            ], style={'width': '20%',
                      'height': '30px',
                      'margin-left': 'auto',
                      'display': 'block',
                      'margin-right': 'auto',
                      'margin-top': '30px'
                , 'margin-bottom': '10px'}),
            html.Div([
                html.H6("IMBD Rating:"),
                dcc.Input(
                    id='imdb-output',
                    style={'width': '300px'}
                ),
            ], style={'width': '20%',
                      'height': '30px',
                      'margin-left': 'auto',
                      'margin-right': 'auto',
                      'display': 'block',
                      'margin-top': '30px'
                , 'margin-bottom': '10px'}),
        ]),
        html.Br(),
    ]),
], style={ 'background-color': '#D8D8D8'})


@app.callback(
    Output('graph_1', 'figure'),
    Input('genre', 'value')
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    dff = df.copy()
    dff = dff[dff["genre"] == option_slctd]
    if option_slctd == 'All':
        fig1 = px.histogram(df, x='genre', y='sales_revenue',
                            labels={"genre": "Genre", "sales_revenue": "Sales Revenue"},color='genre')
    else:
        fig1 = px.histogram(dff, x='subgenre', y='sales_revenue',
                            labels={"subgenre": "Subgenre", "sales_revenue": "Sales Revenue"},color='subgenre')
    fig1.update_layout(
        paper_bgcolor=COLORS['background'],
        showlegend=False
    )
    return fig1


@app.callback(
    Output('graph_2', 'figure'),
    Input(component_id='genre', component_property='value')
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    dff = df.copy()
    dff = dff[dff["genre"] == option_slctd]
    if option_slctd == 'All':
        fig2 = px.histogram(df, x='genre', y='n_views_pes',
                            labels={"genre": "Genre", "n_views_pes": "Viewing Numbers (PES)"},color='genre')
    else:
        fig2 = px.histogram(dff, x='subgenre', y='n_views_pes',
                            labels={"subgenre": "Subgenre", "n_views_pes": "Viewing Numbers (PES)"},color='subgenre')
    fig2.update_layout(
        paper_bgcolor=COLORS['background'],
        showlegend=False
    )
    return fig2


@app.callback(
    Output('graph_3', 'figure'),
    Input(component_id='genre', component_property='value')
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    dff = df.copy()
    dff = dff[dff["genre"] == option_slctd]
    if option_slctd == 'All':
        fig3 = px.histogram(df, x='genre', y='averageRating',
                            labels={"genre": "Genre", "sales_revenue": "Average IMDB Rating"}, histfunc='avg',color='genre')
    else:
        fig3 = px.histogram(dff, x='subgenre', y='averageRating',
                            labels={"subgenre": "Subgenre", "sales_revenue": "Average IMDB Rating"}, histfunc='avg',color='subgenre')
    fig3.update_layout(
        paper_bgcolor=COLORS['background'],
        showlegend=False
    )
    return fig3

@app.callback(
    Output('revenue-output', 'value'),
    Input('predict-button', 'n_clicks')
)
def update_output(n_clicks):
    if n_clicks > 0:
        return "£200M"


@app.callback(
    Output('viewing-output', 'value'),
    Input('predict-button', 'n_clicks')
)
def update_output(n_clicks):
    if n_clicks > 0:
        return "217,724"


@app.callback(
    Output('imdb-output', 'value'),
    Input('predict-button', 'n_clicks')
)
def update_output(n_clicks):
    if n_clicks > 0:
        return "5.8"


if __name__ == '__main__':
    app.run_server(debug=True)
