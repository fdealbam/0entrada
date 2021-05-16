# Script 0 Entrada

import dash
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
#import geopandas as gpd
import flask
import os
yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

##############################################################

# this is the data of the city
data = pd.read_csv("https://raw.githubusercontent.com/fdealbam/0entrada/main/allzm2020.csv?raw=True")
entidades_s= pd.read_csv("https://raw.githubusercontent.com/fdealbam/censo2020/main/entidades2020.csv", encoding= "Latin-1")



##############################################################
# identificadores
totpobmetrop = data.POBTOT.sum()
num_zm= 74
tot_mpios_zm = 417
totnal = entidades_s.POBTOT.sum()
per_pobnal = (totpobmetrop/totnal)*100

pobzmvmexico = data[data.NOM_ZM == "Valle de México"].POBTOT.sum()
pobzmonterrey = data[data.NOM_ZM == "Monterrey"].POBTOT.sum()
pobzmguadalajara = data[data.NOM_ZM == "Guadalajara"].POBTOT.sum()
pobzmvpuetlax = data[data.NOM_ZM == "Puebla-Tlaxcala"].POBTOT.sum()


###########################################GRAFICA ÁRBOL 
treezm = px.treemap(data, path=['NOM_ZM'],
                 values='POBTOT')
  
treezm.write_html("porcentZMtreegraph.html")
treezm.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  uniformtext_minsize=12,
                  uniformtext_mode='hide',
                  autosize=True,
                  title_font_size = 12,
                  font_color="white",
                  title_font_color="white",
                  margin = dict(autoexpand= False),
                  showlegend=False,
                  #width=100 
                    ),


######################################
# Apartado "buttons"
######################################

buttons = html.Div([
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
     dbc.Row(
           [
               dbc.Col(html.H1(["Metrópolis, 2020 " ],
                      style={'textAlign': 'start',
                           "color": "white", 
                          "text-shadow": "10px 20px 30px gray",}),
                       width={'size': 20, "offset":1 },
                      )],justify="start",),
    html.Br(),
    html.Br(),
 
    
    
    #2dobotón 
    dbc.Button(([html.P("Metrópolis"), 
                 html.P(f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               #"font-weight": 'bold',
                               "font-size": "40px",
                               "font-family": "Montserrat",        
                               #"font-weight": 'bold'
                        }),                      
       ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-left': '100px',
                 } ,disabled=True),
    
    
    
    #3erBotón 
    dbc.Button(([html.P("Municipios"), 
                 html.P(f"{int(tot_mpios_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-weight": 'bold',
                               "font-size": "40px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold'}),                      
       ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-left': '50px',
                 } ,disabled=True),
    

 
    
       dbc.Button(([html.P("Población total"), 
                 html.P(f"{int(totpobmetrop):,}",  
                        style={
                               "color": "orange", 
                               "font-weight": 'bold',
                               "font-size": "40px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               'backgroundColor': 'white',}),                      
       ]),style={ 'backgroundColor': 'white',
                  "box-shadow": "10px 20px 30px gray",
                  'margin-left': '50px',
                 
                 } ,disabled=True),

    
    #4toBotón 
       dbc.Button(([html.P("% nacional"), 
                 html.P(f"{int(per_pobnal):,}" "%",  
                        style={ 
                               "color": "dark", 
                               "font-weight": 'bold',
                               "font-size": "40px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold'}),                      
       ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-left': '50px',
                 } ,disabled=True),
    
    html.Br(),
    html.Br(),
    html.Br(),
      ])
       

######################################
# Apartado "Metropolis"
######################################
    
metropolis = dbc.Card(
    dbc.CardBody(
        [
   html.Br(),
   html.Br(),
            
            html.H6("Las cuatro más pobladas", 
                    style={"color": "white", 
                               "font-weight": 'bold',
                               "font-size": "26px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               "text-shadow": "10px 20px 30px gray",
                        'margin-left': '90px',
                          "background-color": "lightgray"}),

   html.Br(),
            
            html.P("CORREGIR CIFRAS: Cuatro metrópolis reúnen 35,613,864 habitantes, es decir, 28.2% de la población del país (INEGI,2020)", 
                    style={'textAlign': 'left',
                           "color": "black",
                           'margin-left': '90px',
                           #'text-transform': "uppercase",
                          "background-color": "lightgray"}),
        
            dbc.Row([
            dbc.Col(dbc.Button(dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/cd70e780b421392cf892dc250a7523c792c9d678/application/static/1zmcdmx.png?raw=true"),
                         href="https://zm-valledemexico.herokuapp.com/",
                               style={"background-color": "lightgray"}),
                      md={"size": 3,},
                     
                      #style= {"margin-top": "20px",
                      #        "margin-left": "-38px",
                             #"background-color": "orange"}
                   ),
            
            dbc.Col(dbc.Button(dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/cd70e780b421392cf892dc250a7523c792c9d678/application/static/1zmmonterrey.png?raw=true"),
                         href="https://zm-monterrey.herokuapp.com/",
                               style={"background-color": "lightgray"}),
                      md={"size": 3,},
                      #style= {"margin-top": "-320px",
                      #        "margin-left": "325px"}
                   ),
            
            dbc.Col(dbc.Button(dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/cd70e780b421392cf892dc250a7523c792c9d678/application/static/1zmguadalajara.png?raw=true"),
                         href="https://zm-guadalajara.herokuapp.com/",
                               style={"background-color": "lightgray"}),
                      md={"size": 3,},
                     
                      #style= {"margin-top": "20px",
                      #        "margin-left": "-38px"}
                   ),

            dbc.Col(dbc.Button(dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/cd70e780b421392cf892dc250a7523c792c9d678/application/static/1zmpueblatlaxcala.png?raw=true"),
                         href="https://zm-pueblatlaxcala.herokuapp.com/",
                               style={"background-color": "lightgray"}),
                      md={"size": 3,},
                      #style= {"margin-top": "-320px",
                      #        "margin-left": "325px"}
                   ),
              ]),  
            
             dbc.Row([
                 dbc.Col(html.H6("Valle de México", 
                     style={'textAlign': 'center',
                           "color": "black",
                           "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6("Monterrey", 
                     style={'textAlign': 'center',
                           "color": "black",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6("Guadalajara", 
                     style={'textAlign': 'center',
                           "color": "black",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6("Puebla-Tlaxcala", 
                     style={'textAlign': 'center',
                           "color": "black",
                           'text-transform': "uppercase",
                          "background-color": "light"}))]),                  

             dbc.Row([
                 dbc.Col(html.H6(f"{int(pobzmvmexico):,}",
                     style={'textAlign': 'center',
                           "color": "red",
                            "font-weight": 'bold',
                            "font-size": "20px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6(f"{int(pobzmonterrey):,}",
                     style={'textAlign': 'center',
                           "color": "black",
                            "font-weight": 'bold',
                            "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6(f"{int(pobzmguadalajara):,}",
                     style={'textAlign': 'center',
                           "color": "black",
                            "font-weight": 'bold',
                            "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6(f"{int(pobzmvpuetlax):,}",
                     style={'textAlign': 'center',
                           "color": "black",
                            "font-weight": 'bold',
                            "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"}))]),                  
            
            
   html.Br(),
   html.Br(),
   html.Br(),

   html.Br(),
   html.H6("¿Cuánta población tienen?", 
                    style={"color": "white", 
                               "font-weight": 'bold',
                               "font-size": "26px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               "text-shadow": "10px 20px 30px gray",
                        'margin-left': '90px',
                          "background-color": "lightgray"}),

     # Graph Tree
    dbc.Row([dbc.Col(dcc.Graph(figure=treezm))],
             style={'backgroundColor': 'lightgray',
                    'width': '1250px',
                    'margin-top': '0px',
                    'margin-left': '0px',
                    
                        }),
       
  html.Br(),
   html.Br(),
   html.Br(),

   html.Br(),
   html.H6("Numeralia metropolitana", 
                    style={"color": "white", 
                               "font-weight": 'bold',
                               "font-size": "26px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               "text-shadow": "10px 20px 30px gray",
                        'margin-left': '90px',
                          "background-color": "lightgray"}),
            
            
   html.Br(),
   html.Br(),
   html.Br(),
   html.Br(),
   html.Br(),
   html.Br(),
   html.Br(),
   html.Br(),
    
   dbc.Row([
                                    #https://github.com/fdealbam/CamaraDiputados/blob/b11ef31e8e0f73e1a4a06ce60402563e1bd0122e/application/static/logocamara.jfif
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true"),
                        width=5, md={'size': 1,  "offset": 3, }),
            
           dbc.Col(html.H6(" S e c r e t a r í a   G e n e r a l," 
                           " Secretaría de Servicios Parlamentarios, "
                           " México, 2021 "),
                  width={'size': 5, 'offset': 0}),
               ], justify="start",),
     dbc.Row([    
           dbc.Col(html.H5([dbc.Badge("Equipo responsable", 
                          href="https://innovation-learning.herokuapp.com/",
                                     )]),
                  width={'size': 3,  "offset": 4}),
                       ], justify="start",),
   
    html.Br(),
    
    
                
            
        ]),
    style={"width": "78rem", 
          "border": "0",
          "margin-left": "-4px",
          "background-color": "lightgray",
           "justify": "justify"
          })
    
    
    

################################################
# a p p 
################################################

FONT_AWESOMEpro1 = "{% static 'fontawesome_pro/js/all.min.js' %}"
FONT_AWESOMEpro = "{% static 'fontawesome_pro/css/all.min.css' %}"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
server = flask.Flask(__name__)    
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. 
                                                LUX, 
                                                FONT_AWESOMEpro1,
                                                FONT_AWESOME, 
                                                FONT_AWESOMEpro], server=server)




app.layout = html.Div([ buttons, metropolis# layer2,
                       #collapse, fade
                      ],style={
            'margin-top': '0px',
            'margin-left': '10px',
            'width': '1400px',
            'height': '1413px',
            'backgroundColor': 'lightgray'
            })


if __name__ == '__main__':
    app.run_server()
