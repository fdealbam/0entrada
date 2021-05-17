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
data = pd.read_csv("https://raw.githubusercontent.com/fdealbam/0entrada/main/allzm_wpercent.csv?raw=True")
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

zm4totpob= (pobzmvmexico + pobzmonterrey)

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


###########################################Grafica black


#-------------------------------------------------------------------------------------------------------------------1
# POBLACION TOTAL 2
df_c = data.sort_values(by= "POBTOT", ascending=False, ignore_index=True).iloc[36:]
graph1 = px.bar_polar(df_c,
                   r="POBTOT", theta="NOM_ZM",
                   color="POBTOT", #template="none",
                   #legend="off",
                   #color_discrete_sequence= px.colors.sequential.Plasma_r
                     )
graph1.update_layout(#legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=9,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     #plot_bgcolor="rgba(0,0,0,0)"
                      )
graph1.update(layout_coloraxis_showscale=False)  


#-------------------------------------------------------------------------------------------------------------------2
# POBLACION TOTAL 1
df_b = data.sort_values(by= "POBTOT", ascending=False, ignore_index=True).iloc[4:36] 

graph2 = px.bar_polar(df_b, 
                   r="POBTOT", theta="NOM_ZM",
                   color="POBTOT", #template="none",
                   #legend="off",
                   color_discrete_sequence= px.colors.sequential.Plotly3
                     )
graph2.update_layout(font=dict(family="Arial",
                              size=9,
                              color="black"),
                     #opacity=0.1,
                     paper_bgcolor="rgba(0,0,0,0)",
                     #plot_bgcolor="rgba(0,0,0,0)"
                    )
graph2.update(layout_coloraxis_showscale=False)   



#-------------------------------------------------------------------------------------------------------------------3
# SIN DERECHOHABIENCIA

df_a = data.sort_values(by= "POBTOT", ascending=False)#.iloc[4:36]#.head(20)

sinderechohabiencia_graf = px.bar_polar(df_a,
                   r="PSINDER_%", theta="NOM_ZM",
                   color="PSINDER_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
sinderechohabiencia_graf.update_layout(#legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
sinderechohabiencia_graf.update(layout_coloraxis_showscale=False)  



#-------------------------------------------------------------------------------------------------------------------3
# con discapacidad

df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

discapacidad_graf = px.bar_polar(df_a,
                   r="PCON_DISC_%", theta="NOM_ZM",
                   color="PCON_DISC_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Plotly3_r)
discapacidad_graf.update_layout(#legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
discapacidad_graf.update(layout_coloraxis_showscale=False)  



#-------------------------------------------------------------------------------------------------------------------3
# CON INTERNET
df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

internet_graf = px.bar_polar(df_a,
                   r="VPH_INTER_%", theta="NOM_ZM",
                   color="VPH_INTER_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Peach)
internet_graf.update_layout(#legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                    #heigth= "420px",

                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
internet_graf.update(layout_coloraxis_showscale=False) 


#-------------------------------------------------------------------------------------------------------------------3
# DESOCUPADOS

df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

desocupada12ymas_graf = px.bar_polar(df_a,
                   r="PDESOCUP_%", theta="NOM_ZM",
                   color="PDESOCUP_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Mint)
desocupada12ymas_graf.update_layout(#legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
desocupada12ymas_graf.update(layout_coloraxis_showscale=False)


#-------------------------------------------------------------------------------------------------------------------3
#POBLACION NACIDA EN OTRA ENTIDAD

df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

nacidaenotraentidad_graf = px.bar_polar(df_a,
                   r="PNACOE_%", theta="NOM_ZM",
                   color="PNACOE_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
nacidaenotraentidad_graf.update_layout(#legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
nacidaenotraentidad_graf.update(layout_coloraxis_showscale=False)



#-------------------------------------------------------------------------------------------------------------------3
# 60 Y MAS

df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

pobde60ymas_graf = px.bar_polar(df_a,
                   r="P_60YMAS_%", theta="NOM_ZM",
                   color="P_60YMAS_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Mint)
pobde60ymas_graf.update_layout(#legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
pobde60ymas_graf.update(layout_coloraxis_showscale=False)

#-------------------------------------------------------------------------------------------------------------------3
# AFILIADOS SerVICIOS De SALUD PRIVADOS

df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

servsaludpriv_graf = px.bar_polar(df_a,
                   r="PAFIL_IPRIV_%", theta="NOM_ZM",
                   color="PAFIL_IPRIV_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
servsaludpriv_graf.update_layout(#legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
servsaludpriv_graf.update(layout_coloraxis_showscale=False)

#-------------------------------------------------------------------------------------------------------------------3
# PROMEDIOS HABITANTES/CUARTO (DORMITORIO)

df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

habitantesporcuarto_graf = px.bar_polar(df_a,
                   r="PRO_OCUP_C", theta="NOM_ZM",
                   color="PRO_OCUP_C", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Pinkyl)
habitantesporcuarto_graf.update_layout(#legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
habitantesporcuarto_graf.update(layout_coloraxis_showscale=False)

#-------------------------------------------------------------------------------------------------------------------3
# Población con grupo religioso protestante/ cristiano evangélico  
    

df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

relgprotevang_graf = px.bar_polar(df_a,
                   r="PRO_CRIEVA_%", theta="NOM_ZM",
                   color="PRO_CRIEVA_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Mint)
relgprotevang_graf.update_layout(#legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
relgprotevang_graf.update(layout_coloraxis_showscale=False)

#-------------------------------------------------------------------------------------------------------------------3
# HOGARES CON JEF-A- DE FAMILIA

df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

hogconjfa_graf = px.bar_polar(df_a,
                   r="HOGJEF_F_%", theta="NOM_ZM",
                   color="HOGJEF_F_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.PuRd)
hogconjfa_graf.update_layout(#legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
hogconjfa_graf.update(layout_coloraxis_showscale=False)

#-------------------------------------------------------------------------------------------------------------------3
# HOGARES CON BICICLETA

df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

hogaresconbici_graf = px.bar_polar(df_a,
                   r="VPH_BICI_%", theta="NOM_ZM",
                   color="VPH_BICI_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Peach)
hogaresconbici_graf.update_layout(#legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
hogaresconbici_graf.update(layout_coloraxis_showscale=False)

#-------------------------------------------------------------------------------------------------------------------3
# POBLACIÖN ANALFABETA

df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

pobanalfabeta_graf = px.bar_polar(df_a,
                   r="P15YM_AN_%", theta="NOM_ZM",
                   color="P15YM_AN_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
pobanalfabeta_graf.update_layout(#legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
pobanalfabeta_graf.update(layout_coloraxis_showscale=False)



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
                          "background-color": "light"}))
             ]),                  

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

###################################################            
# Graphs Polar Bar                         
###################################################            

#black graph
   html.H6("Clasificación según poblacion", 
                    style={"color": "white", 
                               "font-weight": 'bold',
                               "font-size": "26px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               "text-shadow": "10px 20px 30px gray",
                        'margin-left': '90px',
                          "background-color": "lightgray"}),
   html.Br(),
            
   dbc.Row([
         dbc.Col(dcc.Graph(figure=graph1),
                style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
         dbc.Col(dcc.Graph(figure=graph2),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
         dbc.Col(dcc.Graph(figure=graph2),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
         dbc.Col(dcc.Graph(figure=graph2),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
     ],
             style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
       
       

      
            
            
###################################################            
# Numeralia metropolitana                         
###################################################            

            
            
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
   dbc.Row([
         dbc.Col(dcc.Graph(figure=pobde60ymas_graf),
                style={#"width": "px",
                      'backgroundColor': 'lightgray'}),

         dbc.Col(dcc.Graph(figure=sinderechohabiencia_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),

         dbc.Col(dcc.Graph(figure=discapacidad_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
      
     ],
             style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),

             dbc.Row([
                 dbc.Col(html.H6("60 años y más", 
                     style={'textAlign': 'center',
                           "color": "black",
                           "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
 
                 dbc.Col(html.H6("Sin derechihabiencia", 
                     style={'textAlign': 'center',
                           "color": "black",
                           "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 
                 dbc.Col(html.H6("Discapacidad", 
                     style={'textAlign': 'center',
                           "color": "black",
                           "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 
     ],
             style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '-40px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
            
   html.Br(),

   dbc.Row([
       
         dbc.Col(dcc.Graph(figure=servsaludpriv_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
         dbc.Col(dcc.Graph(figure=pobanalfabeta_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
         dbc.Col(dcc.Graph(figure=nacidaenotraentidad_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
       
       
     ],
             style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
    html.Br(),
    dbc.Row([
                 dbc.Col(html.H6("Servicios de Salud Privado", 
                     style={'textAlign': 'center',
                           "color": "black",
                           "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 
                  dbc.Col(html.H6("Analfabetas", 
                     style={'textAlign': 'center',
                           "color": "black",
                           "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),

                  dbc.Col(html.H6("Nacidos en otra entidad", 
                     style={'textAlign': 'center',
                           "color": "black",
                           "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
    
    ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '-40px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
    ############################################### winik <<<<<<<<<<<<<<<<<<<<<<
   dbc.Row([
       
         dbc.Col(dcc.Graph(figure=desocupada12ymas_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
         dbc.Col(dcc.Graph(figure=relgprotevang_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
         dbc.Col(dcc.Graph(figure=habitantesporcuarto_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
       
       
     ],
             style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
    html.Br(),
    dbc.Row([
                 dbc.Col(html.H6("Desocupados", 
                     style={'textAlign': 'center',
                           "color": "black",
                           "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 
                  dbc.Col(html.H6("Protestantes y evangélicos", 
                     style={'textAlign': 'center',
                           "color": "black",
                           "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),

                  dbc.Col(html.H6("Habitantes por dormitorio", 
                     style={'textAlign': 'center',
                           "color": "black",
                           "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
    
    ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '-40px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
            

   dbc.Row([
       
         dbc.Col(dcc.Graph(figure=hogconjfa_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
         dbc.Col(dcc.Graph(figure=internet_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
         dbc.Col(dcc.Graph(figure=hogaresconbici_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
       
       
     ],
             style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
    html.Br(),
    dbc.Row([
                 dbc.Col(html.H6("Jefatura femenina", 
                     style={'textAlign': 'center',
                           "color": "black",
                           "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 
                  dbc.Col(html.H6("Internet", 
                     style={'textAlign': 'center',
                           "color": "black",
                           "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),

                  dbc.Col(html.H6("Bicicleta", 
                     style={'textAlign': 'center',
                           "color": "black",
                           "font-size": "16px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
    
    ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '-40px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
            
            
            
    ############################################### winik <<<<<<<<<<<<<<<<<<<<<<
           
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
    style={"border": "0",
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
