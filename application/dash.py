# Script 0entrada

import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
import geopandas as gpd
import flask
import os
yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

today = date.today()
d2 = today.strftime("Fecha de actualización : %d-%m-%Y")

pobsindh = 7804407

entidades_s= pd.read_csv("https://raw.githubusercontent.com/fdealbam/censo2020/main/entidades2020.csv", encoding= "Latin-1")
entidades_s.replace('Ciudad de MÃ©xico','Ciudad de México', inplace=True)
entidades_s.replace('MÃ©xico','México', inplace=True)
entidades_s.replace('Nuevo LeÃ³n','Nuevo León', inplace=True)

poblacion_pais = entidades_s.POBTOT.sum()

entidades_s_4 = entidades_s[(entidades_s.NOM_ENT=='Nuevo León')|
                            (entidades_s.NOM_ENT=='México')|
                            (entidades_s.NOM_ENT=='Jalisco')|
                            (entidades_s.NOM_ENT=='Ciudad de México')]

pob_total = entidades_s_4.POBTOT.sum()
pob_total_p = ((pob_total*100)/poblacion_pais).round(1)

presentation = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Fuente: Censo de Población y Vivienda 2020, INEGI", 
                    style={'textAlign': 'left',
                           "color": "white",
                           #"background-color": "#6A1B9A"
                          }),
            
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H6("Entidades más pobladas", 
                    style={'textAlign': 'left',
                           "color": "white",
                           "background-color": "#6A1B9A"}),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            
            html.H6("Metrópolis más pobladas", 
                    style={'textAlign': 'left',
                           "color": "white",
                           "background-color": "#6A1B9A"}),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
         
 
     

            html.H6("Contacto", 
                    style={'textAlign': 'left',
                           "color": "white",
                           "background-color": "#6A1B9A"}),

            dbc.Button(html.Span(["", html.H3(className="far fa-envelope", 
                                      style={"background-color": "#6A1B9A","color":"white"} 
                                             )]),
                      style={"background-color": "#6A1B9A"},),
                                  
            
   #         dbc.Button(
   #             html.Span(["", html.H1(className="far fa-envelope", style={"color": "white",
   #                        "background-color": "#6A1B9A"}),]),),
        ]),
    style={"width": "13rem", 
          "border": "0",
           #"margin-left": "40px",
          "background-color": "#6A1B9A",
           'color':'#BA68C8',
           "height": "850px",
          })



laboratorio = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Plataforma de Análisis Estratégico", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "orange"}),
            html.H6("En esta plataforma integraremos insumos de información para los diputados y diputadas y público interesado",
                    "Es información cuantitativa de dos referentes geojurídicos principales del país: las entidades y las zonas metropolitanas",
                    
                    style={'textAlign': 'left',
                           "color": "black",
                           'text-transform': "uppercase",
                          "background-color": "orange"}),
 


            
        ]),
    
    style={"width": "48rem", 
          "border": "0",
          "margin-left": "-4px",
          "background-color": "orange",
           "justify": "justify"
          })



entidades = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Entidades más pobladas", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "orange"}),
            html.H6(["Cuatro entidades reúnen ",(pob_total_p),"% de la población del país, es decir, ",(f"{pob_total:,d}")," personas."], 
                    style={'textAlign': 'left',
                           "color": "black",
                           'text-transform': "uppercase",
                          "background-color": "orange"}),
 

            dbc.Col(dbc.Button(dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/application/static/1nleona.png?raw=true"),
                         href="https://censo2020-nuevoleon.herokuapp.com/",
                               style={"background-color": "orange"}),
                      md={"size": 4,},
                     
                      style= {"margin-top": "0px",
                              "margin-left": "-35px",
                             #"background-color": "orange"
                             }),
            
            dbc.Col(dbc.Button(dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/application/static/1edomex.png?raw=true"),
                         href="https://censo2020-nuevoleon.herokuapp.com/",
                               style={"background-color": "orange"}),
                      md={"size": 4,},
                      style= {"margin-top": "-180px",
                              "margin-left": "130px"
                             }),

            dbc.Col(dbc.Button(dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/application/static/1jal.png?raw=true"),
                         href="https://censo2020-nuevoleon.herokuapp.com/",
                               style={"background-color": "orange"}),
                      md={"size": 4,},
                      style= {"margin-top": "-180px",
                              "margin-left": "330px"}),

            dbc.Col(dbc.Button(dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/application/static/1cdmx.png?raw=true"),
                         href="https://censo2020-nuevoleon.herokuapp.com/",
                               style={"background-color": "orange"}),
                      md={"size": 4,},
                      style= {"margin-top": "-195px",
                              "margin-left": "510px"}),
            
             dbc.Row([
                 dbc.Col(html.H6("Nuevo León", 
                     style={'textAlign': 'left',
                           "color": "black",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6("estado de México", 
                     style={'textAlign': 'left',
                           "color": "black",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6("Jalisco", 
                     style={'textAlign': 'left',
                           "color": "black",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6("Ciudad de México", 
                     style={'textAlign': 'left',
                           "color": "black",
                           'text-transform': "uppercase",
                          "background-color": "light"}))]),            
        ]),
    
    style={"width": "48rem", 
          "border": "0",
          "margin-left": "-4px",
          "background-color": "orange",
           "justify": "justify"
          })




metropolis = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Metrópolis más pobladas", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "orange"}),
            
            html.H6("Tres metrópolis que reúnen (TOT_POB.SUM) habitantes, es decir, PERCENT% de la población del país", 
                    style={'textAlign': 'left',
                           "color": "black",
                           'text-transform': "uppercase",
                          "background-color": "orange"}),
            html.H6("Monterrrey,  Guadalajara y Valle de México", 
                    style={'textAlign': 'left',
                           "color": "black",
                           'text-transform': "uppercase",
                          "background-color": "orange"}),
            
        ]),
    style={"width": "48rem", 
          "border": "0",
          "margin-left": "-4px",
          "background-color": "orange",
           "justify": "justify"
          })






########################################################################
# A P P 
########################################################################



# identificadores
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
server = flask.Flask(__name__)    
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. 
                                                LUX, FONT_AWESOME
                                               ], server=server)




# make a reuseable navitem for the different examples
nav_item1 = dbc.NavItem(dbc.NavLink("Inicio", href="https://innovation-learning.herokuapp.com/"))
nav_item2 = dbc.NavItem(dbc.NavLink("Entidades", href="#"))
nav_item3 = dbc.NavItem(dbc.NavLink("Metrópolis", href="#"))


default = dbc.NavbarSimple(
    children=[nav_item1,nav_item2,nav_item3,],
    brand="Menu",
    brand_href="#",
    sticky="top",
    className="mb-5",
)

body = html.Div([
    
    dbc.Row([
        dbc.Col(dbc.Card(presentation),    
               style={'margin-top': '0px',    
                      'margin-left': '50px',
                   
                   "color":"#BA68C8"
               #       'width': '479px',
               #       'height': '100%',
               }, sm={  "offset": 1, })
     ],  no_gutters= True, justify= "start",
     className="blockquote"),

 
    

    dbc.Row([
        dbc.Col(dbc.Card(laboratorio), 
               style={'margin-top': '-830px',
                      'margin-left': '240px', 
                     }),
    
        dbc.Col(dbc.Card(entidades),
               style={'margin-top': '-660px',      
                      'margin-left': '255px', 
               }, sm={  "offset": 1, })
     ], className="blockquote"),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
    dbc.Row([
        dbc.Col(dbc.Card(metropolis),
               style={'margin-top': '-380px',      
                      'margin-left': '255px', 
               }, sm={  "offset": 1, })
     ], className="blockquote"),
    
      ])  

##########################################################################################################
##Collapse:
#collapse = html.Div(
#    [
#        dbc.Button(
#            "Felipe de Alba",
#            id="collapse-button",
#            className="mb-3",
#            color="warning",
#            #background-color= "orange",
#            style={'margin-left': '285px',}
#        ),
#        dbc.Collapse(
#            html.P("Doctor en Planeación Urbana por la Universidad de Montreal (2004-2008) con estancias de dos años en el Massachusetts Institute of Technology (MIT) (2009-2011) y de un año en l´École normale supérieure (ENS) de Lyon (Francia) (2012). También fue profesor invitado de tiempo completo “C” en la Universidad Autónoma Metropolitana (Cuajimalpa) (2012- 2014). Es investigador “A” del Centro de Estudios Sociales y de Opinión Publica (CESOP). Ha publicado más de 60 artículos en revistas internacionales y 12 libros"),
#            id="collapse",
#            style={'margin-left': '255px', }), 
#        
#                    
#                 ]
#)
#
#app.layout = collapse
#
#@app.callback(
#    Output("collapse", "is_open"),
#    [Input("collapse-button", "n_clicks")],
#    [State("collapse", "is_open")],
#)
#def toggle_collapse(n, is_open):
#    if n:
#        return not is_open
#    return is_open
#
#
###############################################################################################################
#
##Fade
#
#
#
#
#fade = html.Div(
#    [
#        dbc.Button("Toggle fade", id="fade-button", 
#                   className="mb-3",
#                   style={'margin-left': '255px',}),
#        dbc.Fade(
#            dbc.Card(
#                dbc.CardBody(
#                    html.P(
#                        "This content fades in and out", 
#                        className="card-text",
#                         style={'margin-left': '255px',}
#                    )
#                )
#            ),
#            id="fade",
#            is_in=True,
#            appear=False,
#        ),
#    ]
#)
#
#
#@app.callback(
#    Output("fade", "is_in"),
#    [Input("fade-button", "n_clicks")],
#    [State("fade", "is_in")],
#)
#def toggle_fade(n, is_in):
#    if not n:
#        # Button has never been clicked
#        return True
#    return not is_in
#
############################################################################

#App

app.layout = html.Div([default, body, 
                       #collapse, fade
                      ])

from application.dash import app
from settings import config

if __name__ == '__main__':
    app.run_server(use_reloader = False)

    
