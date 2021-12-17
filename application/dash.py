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
data = pd.read_csv("https://raw.githubusercontent.com/fdealbam/0entrada/main/zmall2020.csv?raw=True")
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
                  uniformtext_minsize=10,
                  uniformtext_mode='hide',
                  autosize=True,
                  title_font_size = 10,
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

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(20)

sinderechohabiencia_graf = px.bar_polar(df_a,
                   r="PSINDER_%", theta="NOM_ZM",
                   color="PSINDER_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Peach)
sinderechohabiencia_graf.update_layout(title = 'SIN DERECHOHABIENCIA',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 18,
                                        #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
sinderechohabiencia_graf.update(layout_coloraxis_showscale=False)  


df_b = df_a.sort_values('PSINDER_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['PSINDER_%']
d2v = df_b.iloc[1]['PSINDER_%']
d3v = df_b.iloc[2]['PSINDER_%']
d4v = df_b.iloc[3]['PSINDER_%']
d5v = df_b.iloc[4]['PSINDER_%']

bullPSINDER = ("las 5 zonas metropolitanas con más población sin derechohabiencia son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")


#-------------------------------------------------------------------------------------------------------------------3
# con discapacidad

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

discapacidad_graf = px.bar_polar(df_a,
                   r="PCON_DISC_%", theta="NOM_ZM",
                   color="PCON_DISC_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Peach)
discapacidad_graf.update_layout(title = 'DISCAPACIDAD ',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 18,
                                
                                #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
discapacidad_graf.update(layout_coloraxis_showscale=False)  

df_b = df_a.sort_values('PCON_DISC_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['PCON_DISC_%']
d2v = df_b.iloc[1]['PCON_DISC_%']
d3v = df_b.iloc[2]['PCON_DISC_%']
d4v = df_b.iloc[3]['PCON_DISC_%']
d5v = df_b.iloc[4]['PCON_DISC_%']

bullPCON_DISC = ("las 5 zonas metropolitanas con más discapacitados son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")



#-------------------------------------------------------------------------------------------------------------------3
# CON INTERNET
df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

internet_graf = px.bar_polar(df_a,
                   r="VPH_INTER_%", theta="NOM_ZM",
                   color="VPH_INTER_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Peach)
internet_graf.update_layout(title = 'CON INTERNET',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       title_font_size= 18,
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                            paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
internet_graf.update(layout_coloraxis_showscale=False) 

df_b = df_a.sort_values('VPH_INTER_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['VPH_INTER_%']
d2v = df_b.iloc[1]['VPH_INTER_%']
d3v = df_b.iloc[2]['VPH_INTER_%']
d4v = df_b.iloc[3]['VPH_INTER_%']
d5v = df_b.iloc[4]['VPH_INTER_%']

bullVPH_INTER = ("las 5 zonas metropolitanas con más servicio de internet son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")


#-------------------------------------------------------------------------------------------------------------------3
# DESOCUPADOS

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

desocupada12ymas_graf = px.bar_polar(df_a,
                   r="PDESOCUP_%", theta="NOM_ZM",
                   color="PDESOCUP_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
desocupada12ymas_graf.update_layout(title = 'DESOCUPADOS',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 18,
                                    
                                    #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
desocupada12ymas_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('PDESOCUP_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['PDESOCUP_%']
d2v = df_b.iloc[1]['PDESOCUP_%']
d3v = df_b.iloc[2]['PDESOCUP_%']
d4v = df_b.iloc[3]['PDESOCUP_%']
d5v = df_b.iloc[4]['PDESOCUP_%']

bullPDESOCUP = ("las 5 zonas metropolitanas con más población desocupada son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")


#-------------------------------------------------------------------------------------------------------------------3
#POBLACION NACIDA EN OTRA ENTIDAD

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

nacidaenotraentidad_graf = px.bar_polar(df_a,
                   r="PNACOE_%", theta="NOM_ZM",
                   color="PNACOE_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
nacidaenotraentidad_graf.update_layout(title = 'NACIDOS EN OTRA ENTIDAD',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 18,
                                       
                                       #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
nacidaenotraentidad_graf.update(layout_coloraxis_showscale=False)


df_b = df_a.sort_values('PNACOE_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['PNACOE_%']
d2v = df_b.iloc[1]['PNACOE_%']
d3v = df_b.iloc[2]['PNACOE_%']
d4v = df_b.iloc[3]['PNACOE_%']
d5v = df_b.iloc[4]['PNACOE_%']

bullPNACOE = ("las 5 zonas metropolitanas con más población nacida en otra entidad son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")


#-------------------------------------------------------------------------------------------------------------------3
# 60 Y MAS

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

pobde60ymas_graf = px.bar_polar(df_a,
                   r="P_60YMAS_%", theta="NOM_ZM",
                   color="P_60YMAS_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
pobde60ymas_graf.update_layout(title = '60 AÑOS Y MÁS',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       title_font_size= 18,
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
pobde60ymas_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('P_60YMAS_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['P_60YMAS_%']
d2v = df_b.iloc[1]['P_60YMAS_%']
d3v = df_b.iloc[2]['P_60YMAS_%']
d4v = df_b.iloc[3]['P_60YMAS_%']
d5v = df_b.iloc[4]['P_60YMAS_%']

bullP_60YMAS = ("las 5 zonas metropolitanas con más población de 60 años y más son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")


#-------------------------------------------------------------------------------------------------------------------3
# AFILIADOS SerVICIOS De SALUD PRIVADOS

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

servsaludpriv_graf = px.bar_polar(df_a,
                   r="PAFIL_IPRIV_%", theta="NOM_ZM",
                   color="PAFIL_IPRIV_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Peach)
servsaludpriv_graf.update_layout(title = 'SALUD PRIVADA',#'CON AFILIACIÓN A SERVICIOS DE SALUD PRIVADOS',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 18,
                                 
                                 #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
servsaludpriv_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('PAFIL_IPRIV_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['PAFIL_IPRIV_%']
d2v = df_b.iloc[1]['PAFIL_IPRIV_%']
d3v = df_b.iloc[2]['PAFIL_IPRIV_%']
d4v = df_b.iloc[3]['PAFIL_IPRIV_%']
d5v = df_b.iloc[4]['PAFIL_IPRIV_%']

bullPAFIL_IPRIV = ("las 5 zonas metropolitanas con más servicios de salud privados son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")

#-------------------------------------------------------------------------------------------------------------------3
# PROMEDIOS HABITANTES/CUARTO (DORMITORIO)

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

habitantesporcuarto_graf = px.bar_polar(df_a,
                   r="PRO_OCUP_C", theta="NOM_ZM",
                   color="PRO_OCUP_C", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
habitantesporcuarto_graf.update_layout(title = 'PERSONAS POR CUARTO',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 18,
                                       
                                       #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
habitantesporcuarto_graf.update(layout_coloraxis_showscale=False)

#-------------------------------------------------------------------------------------------------------------------3
# Población con grupo religioso protestante/ cristiano evangélico  
    

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

relgprotevang_graf = px.bar_polar(df_a,
                   r="PRO_CRIEVA_%", theta="NOM_ZM",
                   color="PRO_CRIEVA_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Mint)
relgprotevang_graf.update_layout(title = 'PROTESTANTES O EVANGÉLICOS',#'GRUPO RELIGIOSO PROTESTANTE/CRISTIANO EVANGÉLICO',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       title_font_size= 18,
                                 font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
relgprotevang_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('PRO_CRIEVA_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['PRO_CRIEVA_%']
d2v = df_b.iloc[1]['PRO_CRIEVA_%']
d3v = df_b.iloc[2]['PRO_CRIEVA_%']
d4v = df_b.iloc[3]['PRO_CRIEVA_%']
d5v = df_b.iloc[4]['PRO_CRIEVA_%']

bullPRO_CRIEVA = ("las 5 zonas metropolitanas con más población protestante y evangélica son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")

#-------------------------------------------------------------------------------------------------------------------3
# HOGARES CON JEF-A- DE FAMILIA

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

hogconjfa_graf = px.bar_polar(df_a,
                   r="HOGJEF_F_%", theta="NOM_ZM",
                   color="HOGJEF_F_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Purp)
hogconjfa_graf.update_layout(title = 'JEFAS DE FAMILIA',#'HOGARES CENSALES CON PERSONA DE REFERENCIA MUJER',
                                       title_font_family="Montserrat ExtraBold",
                                       title_font_color="Purple",
                                       
                                       title_font_size= 18,
                             
                             #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
hogconjfa_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('HOGJEF_F_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['HOGJEF_F_%']
d2v = df_b.iloc[1]['HOGJEF_F_%']
d3v = df_b.iloc[2]['HOGJEF_F_%']
d4v = df_b.iloc[3]['HOGJEF_F_%']
d5v = df_b.iloc[4]['HOGJEF_F_%']

bullHOGJEF_F = ("las 5 zonas metropolitanas con más jefas de familia son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")

#-------------------------------------------------------------------------------------------------------------------3
# HOGARES CON BICICLETA

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

hogaresconbici_graf = px.bar_polar(df_a,
                   r="VPH_BICI_%", theta="NOM_ZM",
                   color="VPH_BICI_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
hogaresconbici_graf.update_layout(title = ' CON BICICLETA',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 18,
                                  
                                  #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
hogaresconbici_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('VPH_BICI_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['VPH_BICI_%']
d2v = df_b.iloc[1]['VPH_BICI_%']
d3v = df_b.iloc[2]['VPH_BICI_%']
d4v = df_b.iloc[3]['VPH_BICI_%']
d5v = df_b.iloc[4]['VPH_BICI_%']

bullVPH_BICI = ("las 5 zonas metropolitanas con más uso de bicicletas son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")

#-------------------------------------------------------------------------------------------------------------------3
# POBLACIÖN ANALFABETA

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

pobanalfabeta_graf = px.bar_polar(df_a,
                   r="P15YM_AN_%", theta="NOM_ZM",
                   color="P15YM_AN_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
pobanalfabeta_graf.update_layout(title = 'ANALFABETAS',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 18,
                                 
                                 #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
pobanalfabeta_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('P15YM_AN_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['P15YM_AN_%']
d2v = df_b.iloc[1]['P15YM_AN_%']
d3v = df_b.iloc[2]['P15YM_AN_%']
d4v = df_b.iloc[3]['P15YM_AN_%']
d5v = df_b.iloc[4]['P15YM_AN_%']

bullP15YM_AN = ("las 5 zonas metropolitanas con más analfabetas son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")

#-------------------------------------------------------------------------------------------------------------------3
# POBLACIÖN 18 Y MÄS

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

pob18ymas_graf = px.bar_polar(df_a,
                   r="P_18YMAS_%", theta="NOM_ZM",
                   color="P_18YMAS_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Mint)
pob18ymas_graf.update_layout(title = '18 AÑOS Y MÁS',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 18,
                             #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
pob18ymas_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('P_18YMAS_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['P_18YMAS_%']
d2v = df_b.iloc[1]['P_18YMAS_%']
d3v = df_b.iloc[2]['P_18YMAS_%']
d4v = df_b.iloc[3]['P_18YMAS_%']
d5v = df_b.iloc[4]['P_18YMAS_%']

bullP_18YMAS = ("las 5 zonas metropolitanas con más población de 18 años y más son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")


#-------------------------------------------------------------------------------------------------------------------3
# CATOLICA

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

catolica_graf = px.bar_polar(df_a,
                   r="PCATOLICA_%", theta="NOM_ZM",
                   color="PCATOLICA_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Mint)
catolica_graf.update_layout(title = 'CATÓLICOS',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       title_font_size= 18,
                            font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
catolica_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('PCATOLICA_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['PCATOLICA_%']
d2v = df_b.iloc[1]['PCATOLICA_%']
d3v = df_b.iloc[2]['PCATOLICA_%']
d4v = df_b.iloc[3]['PCATOLICA_%']
d5v = df_b.iloc[4]['PCATOLICA_%']

bullPCATOLICA = ("las 5 zonas metropolitanas con más población católica son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")


#-------------------------------------------------------------------------------------------------------------------3
# SIN RELIGION

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

sinrelig_graf = px.bar_polar(df_a,
                   r="PSIN_RELIG_%", theta="NOM_ZM",
                   color="PSIN_RELIG_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Mint)
sinrelig_graf.update_layout(title = 'SIN RELIGIÓN',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 18,
                            
                            #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
sinrelig_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('PSIN_RELIG_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['PSIN_RELIG_%']
d2v = df_b.iloc[1]['PSIN_RELIG_%']
d3v = df_b.iloc[2]['PSIN_RELIG_%']
d4v = df_b.iloc[3]['PSIN_RELIG_%']
d5v = df_b.iloc[4]['PSIN_RELIG_%']

bullPSIN_RELIG = ("las 5 zonas metropolitanas con más población sin religión son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")

#-------------------------------------------------------------------------------------------------------------------3
# CON COMPUTADORA

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

conpc_graf = px.bar_polar(df_a,
                   r="VPH_PC_%", theta="NOM_ZM",
                   color="VPH_PC_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Peach)
conpc_graf.update_layout(title = 'CON COMPUTADORA',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 18,
                         
                         #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
conpc_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('VPH_PC_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['VPH_PC_%']
d2v = df_b.iloc[1]['VPH_PC_%']
d3v = df_b.iloc[2]['VPH_PC_%']
d4v = df_b.iloc[3]['VPH_PC_%']
d5v = df_b.iloc[4]['VPH_PC_%']

bullVPH_PC = ("las 5 zonas metropolitanas con más viviendas con compuadora son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")


#-------------------------------------------------------------------------------------------------------------------3
# secundaria terminada

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

secundaria_graf = px.bar_polar(df_a,
                   r="P15SEC_CO_%", theta="NOM_ZM",
                   color="P15SEC_CO_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
secundaria_graf.update_layout(title = 'SECUNDARIA COMPLETA',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 18,
                         
                         #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
secundaria_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('P15SEC_CO_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['P15SEC_CO_%']
d2v = df_b.iloc[1]['P15SEC_CO_%']
d3v = df_b.iloc[2]['P15SEC_CO_%']
d4v = df_b.iloc[3]['P15SEC_CO_%']
d5v = df_b.iloc[4]['P15SEC_CO_%']

bullP15SEC_CO = ("las 5 zonas metropolitanas con más población con secundaria completa son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")


#vars-------------------------------------------------------------------------------------------------------------------3
# 18 y mas posbasica

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

posbasica_graf = px.bar_polar(df_a,
                   r="P18YM_PB_%", theta="NOM_ZM",
                   color="P18YM_PB_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
posbasica_graf.update_layout(title = '+18 CON POSBÁSICA',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       
                                       title_font_size= 18,
                         
                         #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
posbasica_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('P18YM_PB_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['P18YM_PB_%']
d2v = df_b.iloc[1]['P18YM_PB_%']
d3v = df_b.iloc[2]['P18YM_PB_%']
d4v = df_b.iloc[3]['P18YM_PB_%']
d5v = df_b.iloc[4]['P18YM_PB_%']

bullP18YM_PB = ("las 5 zonas metropolitanas con más población con educación posbásica completa son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")

#vars-------------------------------------------------------------------------------------------------------------------3
# POBLACION FEMENINA NACIDA EN OTRA ENtIDAD

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

nacidaenotraentidadmujer_graf = px.bar_polar(df_a,
                   r="PNACOE_F_%", theta="NOM_ZM",
                   color="PNACOE_F_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Purp)
nacidaenotraentidadmujer_graf.update_layout(title = 'MUJERES NACIDAS EN OTRA ENTIDAD',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                                       title_font_size= 18,
                         font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
nacidaenotraentidadmujer_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('PNACOE_F_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['PNACOE_F_%']
d2v = df_b.iloc[1]['PNACOE_F_%']
d3v = df_b.iloc[2]['PNACOE_F_%']
d4v = df_b.iloc[3]['PNACOE_F_%']
d5v = df_b.iloc[4]['PNACOE_F_%']

bullPNACOE_F = ("las 5 zonas metropolitanas con más mujeres nacidas en otra entidad son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")

#vars-------------------------------------------------------------------------------------------------------------------3
# POBLACION DE 15 A 64

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

pob15a64_graf = px.bar_polar(df_a,
                   r="P_6A11_%", theta="NOM_ZM",
                   color="P_6A11_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Teal)
pob15a64_graf.update_layout(title = '6 A 11 AÑOS',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                            title_font_size= 20,
                         #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
pob15a64_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('P_6A11_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['P_6A11_%']
d2v = df_b.iloc[1]['P_6A11_%']
d3v = df_b.iloc[2]['P_6A11_%']
d4v = df_b.iloc[3]['P_6A11_%']
d5v = df_b.iloc[4]['P_6A11_%']

bullP_6A11 = ("las 5 zonas metropolitanas con mayor población de 6 a 11 años de edad son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")
             

#vars-------------------------------------------------------------------------------------------------------------------3
# STREAMING

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

hogaresconstreaming_graf = px.bar_polar(df_a,
                   r="VPH_SPMVPI_%", theta="NOM_ZM",
                   color="VPH_SPMVPI_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Peach)
hogaresconstreaming_graf.update_layout(title = 'CON STREAMING',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                            title_font_size= 18,
                         #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
hogaresconstreaming_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('VPH_SPMVPI_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['VPH_SPMVPI_%']
d2v = df_b.iloc[1]['VPH_SPMVPI_%']
d3v = df_b.iloc[2]['VPH_SPMVPI_%']
d4v = df_b.iloc[3]['VPH_SPMVPI_%']
d5v = df_b.iloc[4]['VPH_SPMVPI_%']

bullVPH_SPMVP = ("las 5 zonas metropolitanas con más servicios de streaming son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")
             

#vars-------------------------------------------------------------------------------------------------------------------3
# HLI

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

hli_graf = px.bar_polar(df_a,
                   r="P3YM_HLI_%", theta="NOM_ZM",
                   color="P3YM_HLI_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Purp)
hli_graf.update_layout(title = 'HABLAN LENGUA INDÍGENA',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                            title_font_size= 18,
                         #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
hli_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('P3YM_HLI_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['P3YM_HLI_%']
d2v = df_b.iloc[1]['P3YM_HLI_%']
d3v = df_b.iloc[2]['P3YM_HLI_%']
d4v = df_b.iloc[3]['P3YM_HLI_%']
d5v = df_b.iloc[4]['P3YM_HLI_%']

bullP3YM_HLI = ("las 5 zonas metropolitanas con más hablantes de lenguas indígenas son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")


#vars-------------------------------------------------------------------------------------------------------------------3
# pob en hoagares HLI

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

pobhoghli_graf = px.bar_polar(df_a,
                   r="PHOG_IND_%", theta="NOM_ZM",
                   color="PHOG_IND_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Purp)
pobhoghli_graf.update_layout(title = 'HOGARES INDÍGENAS',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                            title_font_size= 18,
                         #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
pobhoghli_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('PHOG_IND_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['PHOG_IND_%']
d2v = df_b.iloc[1]['PHOG_IND_%']
d3v = df_b.iloc[2]['PHOG_IND_%']
d4v = df_b.iloc[3]['PHOG_IND_%']
d5v = df_b.iloc[4]['PHOG_IND_%']

bullPHOG_IND = ("las 5 zonas metropolitanas con más población en hogares indígenas son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")


#vars-------------------------------------------------------------------------------------------------------------------3
# pob afro

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

afro_graf = px.bar_polar(df_a,
                   r="POB_AFRO_%", theta="NOM_ZM",
                   color="POB_AFRO_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Purp)
afro_graf.update_layout(title = 'AFRODESCENDIENTES',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                            title_font_size= 18,
                         #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
afro_graf.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('POB_AFRO_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['POB_AFRO_%']
d2v = df_b.iloc[1]['POB_AFRO_%']
d3v = df_b.iloc[2]['POB_AFRO_%']
d4v = df_b.iloc[3]['POB_AFRO_%']
d5v = df_b.iloc[4]['POB_AFRO_%']

bullPOB_AFRO = ("las 5 zonas metropolitanas con más población afrodescendiente son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")


#vars-------------------------------------------------------------------------------------------------------------------3
# 1 cuarto

df_a = data.sort_values(by= "POBTOT", ascending=False).iloc[4:36]#.head(10)

viviendascon1cuarto = px.bar_polar(df_a,
                   r="VPH_1CUART_%", theta="NOM_ZM",
                   color="VPH_1CUART_%", template="none",
                   #legend="off",
                   color_continuous_scale=px.colors.sequential.Peach)
viviendascon1cuarto.update_layout(title = 'VIVIENDAS CON UN CUARTO',
                                       title_font_family="Montserrat",
                                       title_font_color="black",
                            title_font_size= 18,
                         #legend=dict(showscale=False),
                  font=dict(family="Arial",
                              size=7,
                              color="black"),
                     paper_bgcolor="rgba(0,0,0,0)",
                     plot_bgcolor="rgba(0,0,0,0)")
viviendascon1cuarto.update(layout_coloraxis_showscale=False)

df_b = df_a.sort_values('VPH_1CUART_%', ascending=False, ignore_index=True)

d1n = df_b.iloc[0]['NOM_ZM']
d2n = df_b.iloc[1]['NOM_ZM']
d3n = df_b.iloc[2]['NOM_ZM']
d4n = df_b.iloc[3]['NOM_ZM']
d5n = df_b.iloc[4]['NOM_ZM']

d1v = df_b.iloc[0]['VPH_1CUART_%']
d2v = df_b.iloc[1]['VPH_1CUART_%']
d3v = df_b.iloc[2]['VPH_1CUART_%']
d4v = df_b.iloc[3]['VPH_1CUART_%']
d5v = df_b.iloc[4]['VPH_1CUART_%']

bullVPH_1CUART = ("las 5 zonas metropolitanas con más habitantes por cuarto son "+ d1n +" ("+ str(d1v) +"%), "+ d2n +" ("+ str(d2v) +"%), "+ d3n +" ("+ str(d3v) +"%), "+ d4n +" ("+ str(d4v) +"%) y "+ d5n +" ("+ str(d5v) +"%).")



######################################
# Apartado "head"
######################################
head = html.Div([
    html.Br(),
   dbc.Row([
                                    #https://github.com/fdealbam/CamaraDiputados/blob/b11ef31e8e0f73e1a4a06ce60402563e1bd0122e/application/static/logocamara.jfif
           dbc.Col(
             dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/main/application/static/logo%20cesopycamara1.PNG?raw=true"),
                        width=5, md={'size': 3,  "offset": 6, }),
            
           dbc.Col(html.H6(" Centro de Estudios Sociales y de Opinión Pública," 
                           " Cámara de Diputados"
                           " México, 2021 "),
                  width={'size': 3, 'offset': 0}),
               ], justify="start",),
            
#    dbc.Row([    
#          dbc.Col(html.H5([dbc.Badge("Equipo responsable", 
#                         href="https://innovation-learning.herokuapp.com/",
#                                    )]),
#                 width={'size': 2,  "offset": 8}),
#                      ], justify="start",),
#  

        ])
######################################
# Apartado "buttons"
######################################

buttons = html.Div([
    
     html.Br(),
     html.Br(),
     dbc.Row(
           [
               dbc.Col(html.H1(["Las metrópolis mexicanas en 2020 " ],
                      style={'textAlign': 'start',
                             "font-size": "45px",
                           "color": "white", 
                          "text-shadow": "10px 20px 30px black",}),
                       width={'size': 20, "offset":1 },
                      )],justify="start",),
   html.Br(),
   html.Br(),
   html.Br(),
    
   dbc.Row([
         dbc.Col(([html.H6("Análisis de un fenómeno con alto dinamismo ",
                   style={"color": "black", 
                               "font-weight": 'bold',
                               "font-size": "16px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               "text-shadow": "10px 20px 30px gray",
                            "background-color": "lightgray"}),
   html.Br(),
                   
   html.P("Las zonas metropolitanas son enclaves con el mayor dinamismo en la vida nacional. " 
          "En este documento interactivo analizamos el Censo Nacional de Población " 
          "y Vivienda de 2020, según el cual en el territorio nacional hay 74 zonas  "
          " metropolitanas que comprenden 417 municipios. Éstas reúnen más de 80 millones de habitantes "
          " (63% del total nacional). " 
          " La importancia de estudiar las zonas metropolitanas radica en que son territorios de alta diversidad, "
          " uno de sus signos principales, aunque ello implica también fuertes desigualdades, "  
          "dado que esa diversidad es reflejo de marginación o "
          "de la falta de recursos para el desarrollo. Entonces, las metrópolis son conglomerados  "
          "tanto de la gran variedad poblacional como de la falta de servicios en las viviendas y de la falta "
          " de recursos materiales; en fin, son espacios de concentración de diferencias tanto en su número "
          "como en su proporción; son territorios estadísticamente diversos, reflejo de las múltiples "
          "urbanidades que caracterizan al territorio nacional. Aquí presentamos elementos analíticos "
          "de las particularidades sociodemográficas más relevantes, con el objetivo de destacar "
          "los “modelos de la vida metropolitana” en México, con los datos más recientes. ", 
                     style={"color": "black", 
                            "text-align": "justify",
                            "font-size": "16px",
                            "font-family": "Arial",   
                            "background-color": "lightgray"})])),
   ], style={"background-color": "lightgray",
             "align": "justify",
                          #"box-shadow": "10px 20px 30px gray",
                           'width': '1200px',
                           'margin-left': '100px',
                           'margin-right': '0px'}),
            

  html.Br(),
  html.Br(),
  html.Br(),
  html.Br(),

  html.H6("Cifras generales", 
                    style={"color": "white", 
                               "font-weight": 'bold',
                               "font-size": "26px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               "text-shadow": "10px 20px 30px black",
                        'margin-left': '90px',
                          "background-color": "lightgray"}),

    
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
                  'margin-left': '110px',
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
                  'margin-left': '110px',
                 
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
                  'margin-left': '110px',
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
   

  html.H6("¿Cuánta población tienen?", 
                    style={"color": "white", 
                               "font-weight": 'bold',
                               "font-size": "26px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               "text-shadow": "10px 20px 30px black",
                        'margin-left': '90px',
                          "background-color": "lightgray"}),
            
            
            
            
   html.Br(),
    
   dbc.Row([
         dbc.Col(([html.H6("Extrema concentración poblacional ",
                   style={"color": "black", 
                               "font-weight": 'bold',
                               "font-size": "16px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               "text-shadow": "10px 20px 30px gray",
                            "background-color": "lightgray"}),
   html.Br(),
                   
   html.P("Tal como se observa en la gráfica siguiente, hay cuatro zonas metropolitanas "
          "de muy alta concentración poblacional, de mayor a menor: Valle de México, Monterrey, "
          " Guadalajara y Puebla-Tlaxcala, que reúnen 27% de la población total del país. ", 
                    style={ "text-align": "justify",
                           "color": "black", 
                            "font-size": "16px",
                            "font-family": "Arial",   
                            "background-color": "lightgray"}),  
   html.P("Hay que resaltar aquí otro fenómeno de alto dinamismo poblacional: la Megalópolis de la Region Centro. "
          "Esta MRC es la interconexión funcional de siete zonas metropolitanas: ZM Valle de México, ZM Puebla-Tlaxcala, "
          " ZM Pachuca, ZM Tula, ZM Cuernavaca-Cuautla, ZM Toluca y ZM de Querétaro. "
          "Se trata de un fenómeno de concentración poblacional extrema en el área central del país. ",
                     style={ "text-align": "justify",
                            "color": "black", 
                            "font-size": "16px",
                            "font-family": "Arial",   
                            "background-color": "lightgray"})])),
   ], style={"background-color": "lightgray",
                          #"box-shadow": "10px 20px 30px gray",
                           'width': '1200px',
                           'margin-bottom': '-20px',
                           'margin-left': '100px',
                           'margin-right': '0px'}),
            

  html.Br(),
            

     # Graph Tree
  dbc.Row([dbc.Col(dcc.Graph(figure=treezm),)],
             style={#'backgroundColor': 'lightgray',
                    'width': '1380px',
                    'margin-top': '-20px',
                    'margin-left': '0px',
                    
                        }),
       

   html.Br(),            
   html.H6("Las cuatro más pobladas (Reportes básicos)", 
                    style={"color": "white", 
                               "font-weight": 'bold',
                               "font-size": "26px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               "text-shadow": "10px 20px 30px black",
                        'margin-left': '90px',
                          "background-color": "lightgray"}),

  html.Br(),  
  html.Br(),
  html.Br(),
  dbc.Row([
      html.P("Enseguida presentamos cuatro reportes básicos de "
          "cada una de las cuatro metrópolis más pobladas. "
          "Para acceder a ellos, haz clic en el mapa. NOTA: Próximamente contaremos en este sitio "
          "con reportes de las 70 metrópolis restantes. Igualmente, "
          "pronto aparecerá aquí un libro con análisis exhaustivos de"
          " todas las metrópolis mexicanas. " ,
                     style={ "text-align": "justify",
                            "color": "black", 
                            "font-size": "16px",
                            "font-family": "Arial",   
                            "background-color": "lightgray"})
       
       ], style={"background-color": "lightgray",
                          #"box-shadow": "10px 20px 30px gray",
                           'width': '1200px',
                           'margin-bottom': '-40px',
                           'margin-left': '100px',
                           'margin-right': '0px'}),
            

  html.Br(),

                
            dbc.Row([
            dbc.Col(dbc.Button(dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/cd70e780b421392cf892dc250a7523c792c9d678/application/static/1zmcdmx.png?raw=true"),
                         href="https://zm-valledemexico.herokuapp.com/",
                               style={"background-color": "lightgray"}
                              ),
                      md={"size": 3,},
                     
                      #style= {"margin-top": "20px",
                      #        "margin-left": "-38px",
                             #"background-color": "orange"}
                   ),
            
            dbc.Col(dbc.Button(dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/cd70e780b421392cf892dc250a7523c792c9d678/application/static/1zmmonterrey.png?raw=true"),
                         href="https://zm-monterrey.herokuapp.com/",
                               style={"background-color": "lightgray"
                               }
                              ),
                      md={"size": 3,},
                      #style= {"margin-top": "-320px",
                      #        "margin-left": "325px"}
                   ),
            
            dbc.Col(dbc.Button(dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/cd70e780b421392cf892dc250a7523c792c9d678/application/static/1zmguadalajara.png?raw=true"),
                         href="https://zm-guadalajara.herokuapp.com/",
                               style={"background-color": "lightgray"}
                              ),
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
                            "font-size": "16px",
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
                            "font-size": "35px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6(f"{int(perpob_mty):,}" "%",
                     style={'textAlign': 'center',
                           "color": "black",
                            "font-weight": 'bold',
                            "font-family": "Montserrat ExtraBold",        
                            "font-size": "35px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6(f"{int(perpob_gdl):,}" "%",
                     style={'textAlign': 'center',
                           "color": "black",
                            "font-weight": 'bold',
                            "font-family": "Montserrat ExtraBold",        
                            "font-size": "35px",
                           'text-transform': "uppercase",
                          "background-color": "light"})),
                 dbc.Col(html.H6(f"{int(perpob_ptl):,}" "%",
                     style={'textAlign': 'center',
                           "color": "black",
                            "font-weight": 'bold',
                            "font-family": "Montserrat ExtraBold",        
                            "font-size": "35px",
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
                               "text-shadow": "10px 20px 30px black",
                        'margin-left': '90px',
                           'margin-bottom': '20px',
                          "background-color": "lightgray"}),
            html.Br(),

            
   dbc.Row([
#         dbc.Col(dcc.Graph(figure=graph1),
#                style={#"width": "50px",
#                      'backgroundColor': 'lightgray'}),
         dbc.Col(dcc.Graph(figure=graph2),
                #style={#"width": "50px",
                     # 'backgroundColor': 'lightgray'}
                     ),
         dbc.Col(dcc.Graph(figure=graph3),
               #  style={#"width": "50px",
                 #     'backgroundColor': 'lightgray'}
                ),
         dbc.Col(dcc.Graph(figure=graph4),
               #  style={#"width": "50px",
               #       'backgroundColor': 'lightgray'}
                ),
     ],
             style={#'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': ' 0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
       
         
            
###################################################            
# Numeralia metropolitana                         
###################################################            

            
            
   html.Br(),
   html.H6("Numeralia metropolitana (variables seleccionadas)", 
                    style={"color": "white", 
                               "font-weight": 'bold',
                               "font-size": "26px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               "text-shadow": "10px 20px 30px black",
                        'margin-left': '90px',
                          "background-color": "lightgray"}),
            
            
     html.Br(),
   dbc.Row([
         dbc.Col(([html.H6(#"Las metropolis según 19 variables seleccionadas ",
                   style={"color": "black", 
                               "font-weight": 'bold',
                               "font-size": "16px",
                               "font-family": "Montserrat",        
                               "font-weight": 'bold',
                               "text-shadow": "10px 20px 30px gray",
                            "background-color": "lightgray"}),
   html.Br(),
                   
   html.P("Enseguida seleccionamos 36 metrópolis (situadas en el intervalo poblacional de 4 millones "
          "hasta 500 mil habitantes) y 19 variables "
          "para mostrar la variedad de la vida metropolitana. "
          " Las gráficas muestran cada variable seleccionada según la metrópoli, de la más a la "
          "menos poblada, conforme al intervalo anteriormente mencionado. ",
                     style={ "text-align": "justify",
                            "color": "black", 
                            "font-size": "16px",
                            "font-family": "Arial",   
                            "background-color": "lightgray"})])),
   ], style={"background-color": "lightgray",
                          #"box-shadow": "10px 20px 30px gray",
                           'width': '1200px',
                           'margin-bottom': '-20px',
                           'margin-left': '100px',
                           'margin-right': '0px'}),
            

  html.Br(),
  html.Br(),
  html.Br(),
  html.Br(),

            
   ################################  EDAD            
   html.H1("Edad", 
            style={'backgroundColor': 'lightgray',
                   'margin-left': '90px',
                   "text-shadow": "10px 20px 30px white",
                   
                  "margin-bottom": "-8px"}),
            
   dbc.Row([
         dbc.Col(dcc.Graph(figure=pob15a64_graf),
                style={#"width": "px",
                      'backgroundColor': 'lightgray'}),
         dbc.Col(dcc.Graph(figure=pob18ymas_graf),
                style={#"width": "px",
                      'backgroundColor': 'lightgray'}),
         dbc.Col(dcc.Graph(figure=pobde60ymas_graf),
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
        dbc.Col(html.P(bullP_6A11, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullP_18YMAS, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullP_60YMAS, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
    ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
            
            
      
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
        
   dbc.Row([
        dbc.Col(html.P(bullPCON_DISC, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullPSINDER, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullPAFIL_IPRIV, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
    ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),

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
       dbc.Col(dcc.Graph(figure=secundaria_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
   dbc.Col(dcc.Graph(figure=posbasica_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),],
             style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
            
        dbc.Row([
            dbc.Col(html.P(bullP15YM_AN, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
            dbc.Col(html.P(bullP15SEC_CO, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
            dbc.Col(html.P(bullP18YM_PB, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
            

   html.Br(),
            

   ################################  RELIGION            
   ################################  RELIGION            
   html.H1("Religión", 
            style={
                   'backgroundColor': 'lightgray',
                   'margin-left': '90px',
                  "margin-bottom": "-8px"}),
   html.H1("Religión", 
           style={"color": "lightgray",
                  'backgroundColor': 'lightgray',
                  'margin-left': '90px',
                 "margin-bottom": "-8px"}),
            html.Br(),


            
   dbc.Row([
                dbc.Col(dcc.Graph(figure=catolica_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
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
    dbc.Row([
        dbc.Col(html.P(bullPCATOLICA, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullPRO_CRIEVA, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullPSIN_RELIG, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
    ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
            
       
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
        dbc.Col(dcc.Graph(figure=nacidaenotraentidadmujer_graf),
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
    dbc.Row([
        dbc.Col(html.P(bullPNACOE, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullPNACOE_F, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullPDESOCUP, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
    ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
    

   html.Br(),    

   ################################  MIGRACION            
   html.H1("Etnicidad", 
            style={'backgroundColor': 'lightgray',
                   'margin-left': '90px',
                  "margin-bottom": "-8px"}),
       
   dbc.Row([
         dbc.Col(dcc.Graph(figure=hli_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
        dbc.Col(dcc.Graph(figure=pobhoghli_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
         dbc.Col(dcc.Graph(figure=afro_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
         ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
    dbc.Row([
        dbc.Col(html.P(bullP3YM_HLI, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullPHOG_IND, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullPOB_AFRO, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
    ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),

   html.Br(),    

   ################################  VIVIENDA            
   html.H1("Vivienda", 
            style={'backgroundColor': 'lightgray',
                   'margin-left': '90px',
                  "margin-bottom": "-8px"}),
       
   dbc.Row([
       dbc.Col(dcc.Graph(figure=hogconjfa_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
       dbc.Col(dcc.Graph(figure=viviendascon1cuarto),
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
    dbc.Row([
        dbc.Col(html.P(bullHOGJEF_F, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullVPH_1CUART, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullVPH_BICI, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
    ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
    
            
            dbc.Row([
       
         ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),

       
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
        dbc.Col(dcc.Graph(figure=hogaresconstreaming_graf),
                 style={#"width": "50px",
                      'backgroundColor': 'lightgray'}),
        
         ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
                    'margin-left': '80px',
                    #"width": "78rem", 
                        }),
    dbc.Row([
        dbc.Col(html.P(bullVPH_PC, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",   }),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullVPH_INTER, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
        dbc.Col(html.P(bullVPH_SPMVP, style={ "text-align": "justify","color": "black", "font-size": "10px","font-family": "Arial",}),style={'backgroundColor': 'lightgray'}),
    ],style={'backgroundColor': 'lightgray',
                    'width': '1200px',
                    'margin-top': '0px',
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
    
   dbc.Row([
                                    #https://github.com/fdealbam/CamaraDiputados/blob/b11ef31e8e0f73e1a4a06ce60402563e1bd0122e/application/static/logocamara.jfif
           dbc.Col(
             dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/main/application/static/logo%20cesopycamara1.PNG?raw=true"),
                        width=5, md={'size': 3,  "offset": 6, }),
            
           dbc.Col(html.H6(" Centro de Estudios Sociales y de Opinión Pública," 
                           " Cámara de Diputados"
                           " México, 2021 "),
                  width={'size': 3, 'offset': 0}),
               ], justify="start",),
     #     
     ##dbc.Row([    
     #      dbc.Col(html.H5([dbc.Badge("Equipo responsable", 
      #                    href="https://innovation-learning.herokuapp.com/",
     #                                )]),
     #             width={'size': 3,  "offset": 4}),
     #                  ], justify="start",),
   
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



app.layout = html.Div([head, 
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
