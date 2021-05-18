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

pobde4zm = pobzmvmexico+pobzmonterrey+pobzmguadalajara+pobzmvpuetlax
percentpobde4zm = (pobde4zm/totnal)*100
perpob_vm = (pobzmvmexico/totnal)*100
perpob_mty= (pobzmonterrey/totnal)*100
perpob_gdl= (pobzmguadalajara/totnal)*100
perpob_ptl= (pobzmvpuetlax/totnal)*100
#zm4totpob= (pobzmvmexico + pobzmonterrey)

###########################################GRAFICA ÁRBOL 
treezm = px.treemap(data, path=['NOM_ZM'],
                 values='POBTOT',color_continuous_scale='RdBu',)
  
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


#-------------------------------------------------------------------------------------------------------------------2
# POBLACION TOTAL 2

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:17]

graph2 = px.bar_polar(df_a,
                   r="POBTOT", theta="NOM_ZM",
                   color="POBTOT", template="none",#legend="off",
                   color_continuous_scale=px.colors.sequential.Peach)
graph2.update_layout(font=dict(family="Arial",size=9,
                               color="black"),
                               title = 'DE 4 A 1 MILLÓN',
                               title_font_size=20,
                               title_font_family="Montserrat",
                               title_font_color="black",
                               paper_bgcolor="rgba(0,0,0,0)",)#plot_bgcolor="rgba(0,0,0,0)"
graph2.update(layout_coloraxis_showscale=False)

#-------------------------------------------------------------------------------------------------------------------2
# POBLACION TOTAL 3

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[17:36]

graph3 = px.bar_polar(df_a,
                   r="POBTOT", theta="NOM_ZM",
                   color="POBTOT", template="none",#legend="off",
                   color_continuous_scale=px.colors.sequential.Peach)
graph3.update_layout(font=dict(family="Arial",size=9,
                               color="black"),
                               title = 'DE 1 MILLÓN A 500 MIL',
                               title_font_family="Montserrat",
                               title_font_size=20,
                               title_font_color="black",
                               paper_bgcolor="rgba(0,0,0,0)",)#plot_bgcolor="rgba(0,0,0,0)"
graph3.update(layout_coloraxis_showscale=False)

#-------------------------------------------------------------------------------------------------------------------2
# POBLACION TOTAL 4

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[36:]

graph4 = px.bar_polar(df_a,
                   r="POBTOT", theta="NOM_ZM",
                   color="POBTOT", template="none",#legend="off",
                   color_continuous_scale=px.colors.sequential.Peach)
graph4.update_layout(font=dict(family="Arial",size=9,
                               color="black"),
                               title = 'MENOS DE 500 MIL',
                               title_font_size=20,
                               title_font_family="Montserrat",
                               title_font_color="black",
                               paper_bgcolor="rgba(0,0,0,0)",)#plot_bgcolor="rgba(0,0,0,0)"
graph4.update(layout_coloraxis_showscale=False)

#-------------------------------------------------------------------------------------------------------------------3
# SIN DERECHOHABIENCIA

df_a = data.sort_values(by= "POBTOT", ascending=False)#.iloc[4:36]#.head(20)

sinderechohabiencia_graf = px.bar_polar(df_a,
                   r="PSINDER_%", theta="NOM_ZM",
                   color="PSINDER_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
sinderechohabiencia_graf.update_layout(title = 'sin afiliación a servicios de salud ',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                                        #legend=dict(showscale=False),
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
discapacidad_graf.update_layout(title = 'discapacidad ',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                                
                                #legend=dict(showscale=False),
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
internet_graf.update_layout(title = 'internet ',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                            
                            #legend=dict(showscale=False),
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
desocupada12ymas_graf.update_layout(title = 'población desocupada ',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                                    
                                    #legend=dict(showscale=False),
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
nacidaenotraentidad_graf.update_layout(title = 'población nacida en otra entidad ',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                                       
                                       #legend=dict(showscale=False),
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
pobde60ymas_graf.update_layout(title = '60 años y más ',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       title_font_size= 20,
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
servsaludpriv_graf.update_layout(title = 'con afiliación a servicios de salud privados',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                                 
                                 #legend=dict(showscale=False),
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
habitantesporcuarto_graf.update_layout(title = 'promedio de habitantes por cuarto',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                                       
                                       #legend=dict(showscale=False),
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
relgprotevang_graf.update_layout(title = 'grupo religioso protestante/ cristiano evangélico  ',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                                 
                                 #legend=dict(showscale=False),
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
hogconjfa_graf.update_layout(title = 'hogares censales con persona de referencia mujer  ',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                             
                             #legend=dict(showscale=False),
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
hogaresconbici_graf.update_layout(title = 'bicicleta',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                                  
                                  #legend=dict(showscale=False),
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
pobanalfabeta_graf.update_layout(title = 'población analfabeta  ',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                                 
                                 #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
pobanalfabeta_graf.update(layout_coloraxis_showscale=False)

#-------------------------------------------------------------------------------------------------------------------3
# POBLACIÖN 18 Y MÄS

df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

pob18ymas_graf = px.bar_polar(df_a,
                   r="P_18YMAS_%", theta="NOM_ZM",
                   color="P_18YMAS_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Mint)
pob18ymas_graf.update_layout(title = '18 años y más ',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                             #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
pob18ymas_graf.update(layout_coloraxis_showscale=False)

#-------------------------------------------------------------------------------------------------------------------3
# SIN RELIGION

df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

sinrelig_graf = px.bar_polar(df_a,
                   r="PSIN_RELIG_%", theta="NOM_ZM",
                   color="PSIN_RELIG_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
sinrelig_graf.update_layout(title = 'población sin religión  ',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                            
                            #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
sinrelig_graf.update(layout_coloraxis_showscale=False)

#-------------------------------------------------------------------------------------------------------------------3
# CON COMPUTADORA

df_a = data.sort_values(by= "POBTOT", ascending=False)#.head(10)

conpc_graf = px.bar_polar(df_a,
                   r="VPH_PC_%", theta="NOM_ZM",
                   color="VPH_PC_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Peach)
conpc_graf.update_layout(title = 'computadora  ',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 20,
                         
                         #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
conpc_graf.update(layout_coloraxis_showscale=False)



######################################
# Apartado "head"
######################################
head = html.Div([
    html.Br(),
    dbc.Row([#https://github.com/fdealbam/CamaraDiputados/blob/b11ef31e8e0f73e1a4a06ce60402563e1bd0122e/application/static/logocamara.jfif
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true"),
                        width=45, md={'size': 1,  "offset": 1, }),
            
           dbc.Col(html.H6(" S e c r e t a r í a   G e n e r a l," 
                           " Secretaría de Servicios Parlamentarios, "
                           " México, 2021 "),
                  width={'size': 6, 'offset': 0}),
               ], justify="start",),])
######################################
# Apartado "buttons"
######################################

buttons = html.Div([
    
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
     dbc.Row(
           [
               dbc.Col(html.H1(["Metrópolis, 2020 " ],
                      style={'textAlign': 'start',
                             "font-size": "45px",
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
                    'width': '1380px',
                    'margin-top': '0px',
                    'margin-left': '0px',
                    
                        }),
       

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
  html.Br(),
#           dbc.Row([
#                   html.P("Cuatro metrópolis reúnen "  f"{int(pobde4zm):,}"     
#                          "habitantes, es decir, " f"{int(percentpobde4zm):,}" "%" 
#                          "de la población del país (INEGI,2020)", 
#                   style={'textAlign': 'left',
#                          "color": "black",
#                          "font-size": "16px",
#                          "font-family": "Montserrat Medium",        
#                          'margin-left': '100px',
#                         "background-color": "lightgray"}),
#                  ]),  

                
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

            #porcentajes
             dbc.Row([          
                 dbc.Col(html.H6(f"{int(perpob_vm):,}" "%",
                     style={'textAlign': 'center',
                           "color": "red",
                            "font-weight": 'bold',
                            "font-family": "Montserrat ExtraBold",        
                            "font-size": "25px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6(f"{int(perpob_mty):,}" "%",
                     style={'textAlign': 'center',
                           "color": "black",
                            "font-weight": 'bold',
                            "font-family": "Montserrat ExtraBold",        
                            "font-size": "20px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6(f"{int(perpob_gdl):,}" "%",
                     style={'textAlign': 'center',
                           "color": "black",
                            "font-weight": 'bold',
                            "font-family": "Montserrat ExtraBold",        
                            "font-size": "20px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6(f"{int(perpob_ptl):,}" "%",
                     style={'textAlign': 'center',
                           "color": "black",
                            "font-weight": 'bold',
                            "font-family": "Montserrat ExtraBold",        
                            "font-size": "20px",
                           'text-transform': "uppercase",
                          "background-color": "light"}))]), 
            
            
   html.Br(),
   html.Br(),
   html.Br(),
   html.Br(),

   html.Br(),
 

###################################################            
# Graphs Polar Bar                         
###################################################            

#black graph
   html.H6("¿Cómo se agrupan las restantes?", 
                    style={"color": "white", 
                               "font-weight": 'bold',
                               "font-size": "26px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               "text-shadow": "10px 20px 30px gray",
                        'margin-left': '90px',
                           'margin-bottom': '20px',
                          "background-color": "lightgray"}),
            html.Br(),
#           dbc.Row([
#                   html.P("Se identifican cuatro grupos, primero; 4 zonas metropolitanas con más de cuatro millones de habitantes, " 
#                          "segundo; 13 zonas metropolitanas entre cuatro y un millón de habitantes ,tercero; 19 zonas metropolitanas "
#                          " de un millón a medio millón de habitantes, y finalmente el cuarto grupo; 34 zonas metropolitanas con "
#                          " menos de medio millón de habitantes.",#" (INEGI,2020)", 
#                   style={'textAlign': 'left',
#                          "color": "black",
#                          "font-size": "16px",
#                          "font-family": "Montserrat Medium",        
#                          'margin-left': '90px',
#                         "background-color": "lightgray"}),],
#               style={#'margin-buttom': '-50px'
#                      'width': '1200px'}),
   #html.Br(),
            
   dbc.Row([
#         dbc.Col(dcc.Graph(figure=graph1),
#                style={#"width": "50px",
#                      'backgroundColor': 'lightgray'}),
         dbc.Col(dcc.Graph(figure=graph2),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
         dbc.Col(dcc.Graph(figure=graph3),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
         dbc.Col(dcc.Graph(figure=graph4),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
     ],
             style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': ' 0px',
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

            
   ################################  EDAD            
   html.H1("Edad", 
            style={'backgroundColor': 'lightgray',
                   'margin-left': '90px',
                  "margin-bottom": "-8px"}),
            
   dbc.Row([
         dbc.Col(dcc.Graph(figure=pobde60ymas_graf),
                style={#"width": "px",
                      'backgroundColor': 'lightgray'}),

         dbc.Col(dcc.Graph(figure=pob18ymas_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
      
     ],
             style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),

 #   dbc.Row([
 #                dbc.Col(html.H6("60 años y más eliminar", 
 #                    style={'textAlign': 'center',
 #                          "color": "black",
 #                          "font-size": "16px",
 #                          'text-transform': "uppercase",
 #                         "background-color": "light"})),
 #
 #                dbc.Col(html.H6("18 años y más", 
 #                    style={'textAlign': 'center',
 #                          "color": "black",
 #                          "font-size": "16px",
 #                          'text-transform': "uppercase",
 #                         "background-color": "light"})),
 #              
 #    ],
 #            style={'backgroundColor': 'lightgray',
 #                   'width': '1200px',
 #                   'margin-top': '-40px',
 #                   'margin-left': '80px',
 #                   #"width": "78rem", 
 #                       }),
 #           
   html.Br(),

   ################################  SALUD            
   html.H1("Salud", 
            style={'backgroundColor': 'lightgray',
                   'margin-left': '90px',
                  "margin-bottom": "-8px"}),

            
   dbc.Row([
         dbc.Col(dcc.Graph(figure=discapacidad_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),

         dbc.Col(dcc.Graph(figure=sinderechohabiencia_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
         dbc.Col(dcc.Graph(figure=servsaludpriv_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),

         ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
    
 # #  dbc.Row([
#
  #               dbc.Col(html.H6("Discapacidad", 
  #                   style={'textAlign': 'center',
  #                         "color": "black",
  #                         "font-size": "16px",
  #                         'text-transform': "uppercase",
  #                        "background-color": "light"})),
  #      
  #               dbc.Col(html.H6("Sin derechohabiencia", 
  #                   style={'textAlign': 'center',
  #                         "color": "black",
  #                         "font-size": "16px",
  #                         'text-transform': "uppercase",
  #                        "background-color": "light"})),
  #      
  #               dbc.Col(html.H6("Servicios de Salud Privado", 
  #                   style={'textAlign': 'center',
  #                         "color": "black",
  #                         "font-size": "16px",
  #                         'text-transform': "uppercase",
  #                        "background-color": "light"})),
  #               
  #      ],style={'backgroundColor': 'lightgray',
  #                  'width': '1200px',
  #                  'margin-top': '-40px',
  #                  'margin-left': '80px',
  #                  #"width": "78rem", 
  #                      }),
   html.Br(),
            
   ################################  EDUCACION            
   html.H1("Educación", 
            style={'backgroundColor': 'lightgray',
                   'margin-left': '90px',
                  "margin-bottom": "-8px"}),

   dbc.Row([
         dbc.Col(dcc.Graph(figure=pobanalfabeta_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
           ],
             style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
            
 #  dbc.Row([
 #       dbc.Col(html.H6("Analfabetas", 
 #                   style={'textAlign': 'center',
 #                         "color": "black",
 #                         "font-size": "16px",
 #                         'text-transform': "uppercase",
 #                        "background-color": "light"})),
 #  
 #          ],style={'backgroundColor': 'lightgray',
 #                  'width': '1200px',
 #                  'margin-top': '-40px',
 #                  'margin-left': '80px',
 #                  #"width": "78rem", 
 #                      }),
   html.Br(),         

   ################################  RELIGION            
   html.H1("Religión", 
            style={'backgroundColor': 'lightgray',
                   'margin-left': '90px',
                  "margin-bottom": "-8px"}),
            
   dbc.Row([
         dbc.Col(dcc.Graph(figure=relgprotevang_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
         dbc.Col(dcc.Graph(figure=sinrelig_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),

        
         ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '-40px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),


    
 #  dbc.Row([
 #               dbc.Col(html.H6("Protestantes y evangélicos", 
 #                   style={'textAlign': 'center',
 #                         "color": "black",
 #                         "font-size": "16px",
 #                         'text-transform': "uppercase",
 #                        "background-color": "light"})),
 #               
 #                dbc.Col(html.H6("Sin religión", 
 #                   style={'textAlign': 'center',
 #                         "color": "black",
 #                         "font-size": "16px",
 #                         'text-transform': "uppercase",
 #                        "background-color": "light"})),
 #      ],style={'backgroundColor': 'lightgray',
 #                  'width': '1200px',
 #                  'margin-top': '-40px',
 #                  'margin-left': '80px',
 #                  #"width": "78rem", 
 #                      }),
 #          
 #     
       
   html.Br(),    
   ################################  MIGRACION            
   html.H1("Migración", 
            style={'backgroundColor': 'lightgray',
                   'margin-left': '90px',
                  "margin-bottom": "-8px"}),
       
   dbc.Row([
         dbc.Col(dcc.Graph(figure=nacidaenotraentidad_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
         dbc.Col(dcc.Graph(figure=desocupada12ymas_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
         ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),


 # dbc.Row([
 #                dbc.Col(html.H6("Nacidos en otra entidad", 
 #                   style={'textAlign': 'center',
 #                         "color": "black",
 #                         "font-size": "16px",
 #                         'text-transform': "uppercase",
 #                        "background-color": "light"})),   
 #     
 #                dbc.Col(html.H6("Población desocupada", 
 #                   style={'textAlign': 'center',
 #                         "color": "black",
 #                         "font-size": "16px",
 #                         'text-transform': "uppercase",
 #                        "background-color": "light"})),
 #     
 #       ],style={'backgroundColor': 'lightgray',
 #                  'width': '1200px',
 #                  'margin-top': '0px',
 #                  'margin-left': '80px',
 #                  #"width": "78rem", 
 #                      }),

   html.Br(),    
       
   ################################  VIVIENDA            
   html.H1("Vivienda", 
            style={'backgroundColor': 'lightgray',
                   'margin-left': '90px',
                  "margin-bottom": "-8px"}),
       
   dbc.Row([
         dbc.Col(dcc.Graph(figure=habitantesporcuarto_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
         dbc.Col(dcc.Graph(figure=hogconjfa_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       
         ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),

 # dbc.Row([
 #                dbc.Col(html.H6("Habitantes por cuarto", 
 #                   style={'textAlign': 'center',
 #                         "color": "black",
 #                         "font-size": "16px",
 #                         'text-transform': "uppercase",
 #                        "background-color": "light"})),

 #                dbc.Col(html.H6("Jefatura femenina", 
 #                   style={'textAlign': 'center',
 #                         "color": "black",
 #                         "font-size": "16px",
 #                         'text-transform': "uppercase",
 #                        "background-color": "light"})),
 #     
 #       ],style={'backgroundColor': 'lightgray',
 #                  'width': '1200px',
 #                  'margin-top': '0px',
 #                  'margin-left': '80px',
 #                  #"width": "78rem", 
 #                      }),
 #          

       
   html.Br(),    
   ################################  SERVICIOS            
   html.H1("Servicios", 
            style={'backgroundColor': 'lightgray',
                   'margin-left': '90px',
                  "margin-bottom": "-8px"}),
       
    dbc.Row([
         dbc.Col(dcc.Graph(figure=conpc_graf),
                style={#"width": "px",
                      'backgroundColor': 'lightgray'}),

         dbc.Col(dcc.Graph(figure=internet_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),

         dbc.Col(dcc.Graph(figure=hogaresconbici_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
      
         ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),

 #   dbc.Row([
 #       dbc.Col(html.H6("Computadora", 
 #                    style={'textAlign': 'center',
 #                          "color": "black",
 #                          "font-size": "16px",
 #                          'text-transform': "uppercase",
 #                         "background-color": "light"})),
 #       dbc.Col(html.H6("Internet", 
 #                    style={'textAlign': 'center',
 #                          "color": "black",
 #                          "font-size": "16px",
 #                          'text-transform': "uppercase",
 #                         "background-color": "light"})),
 #       dbc.Col(html.H6("Bicicleta", 
 #                    style={'textAlign': 'center',
 #                          "color": "black",
 #                          "font-size": "16px",
 #                          'text-transform': "uppercase",
 #                         "background-color": "light"})),
 #                
 #        ],style={'backgroundColor': 'lightgray',
 #                   'width': '1200px',
 #                   'margin-top': '-40px',
 #                   'margin-left': '80px',
 #                   #"width": "78rem", 
 #                       }),
#
       
       
    ############################################### winik <<<<<<<<<<<<<<<<<<<<<<
           
   html.Br(),
   html.Br(),
   html.Br(),
   html.Br(),
   dbc.Row([
         dbc.Col(([html.H4(("¿Qué hace “moderna” a una metrópolis?"),
                   style={"color": "white", 
                               "font-weight": 'bold',
                               "font-size": "26px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               "text-shadow": "10px 20px 30px gray",
                            "background-color": "lightgray"})])),
         dbc.Col(html.P("La diversidad es uno de los signos propios de una metrópolis, muestra la aunque no implica necesariamente igualdad si no, en ciertos contextos específicamente mexicanos, esa diversidad es reflejo de desigualdad. Como expresión de desigualdad, la diversidad es una representación de la diferencia, aquélla que se expresa como la concentración en un territorio de población con características sociodemográficas o de condiciones familiares no similares, o de variedad en la disponibilidad de servicios urbanos, por ejemplo. "
                    "La metrópolis es entonces un espacio de concentración territorial de las diferencias, tanto en su monto o extensión; tanto en su número como en su proporcionalidad. Esta concentración territorial es estadísticamente variada y diversa, porque en los múltiples territorios urbanos del país, se encuentran tanto regularidades como irregularidades, que aquí identificaremos con algunas variables de análisis específicas. "
                    "En esta ocasión, presentamos un ejercicio de visualización de algunos resultados del Censo de Población y Vivienda 2020 (Inegi, 2020) en función de los territorios metropolitanos, en sus particularidades estadísticas. "
                    "El objetivo es destacar tanto regularidades como irregularidades como elementos que pueden ayudarnos a definir un “modelo de la vida” de la población en territorios metropolitanos en México con datos recientes. "), 
                     style={"color": "black", 
                            "font-size": "14px",
                            "font-family": "Arial",   
                            "background-color": "lightgray"}),
           ],style={"background-color": "lightgray",
                          "box-shadow": "10px 20px 30px gray",
                           'width': '1100px',
                           'margin-left': '100px',
                           'margin-right': '0px'}),
            

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
    
    
                
            
        ],
    style={"border": "0",
          "margin-left": "-4px",
          "background-color": "lightgray",
           "justify": "justify"
          }))
    
    
    

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




app.layout = html.Div([ #head, 
                       buttons, metropolis# layer2,
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


    
