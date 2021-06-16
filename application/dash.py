
# feminicidios

import dash
import matplotlib.pyplot as plt 
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
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



###############################
# DATABASES
############################### Abre archivos

defunciones15 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/def15_r_femeninas_tabla%20de%20datos.csv", encoding= "Latin-1", 
                    )
defunciones15.replace(["Ã­","Ã¡", "Ã©", "Ã³", "Ã±", "Ãº"], ["í", "á", "é", "ó", "ñ", "ú"], inplace= True)
defunciones15["Variable"]= defunciones15["Variable"].replace("Ciudad de MÃ©xico", "Ciudad de México") #####################CDMX 
defunciones15["Variable"]= defunciones15["Variable"].replace("Veracruz de Ignacio de la Llave", "Veracruz") #####################CDMX 
defunciones15["Variable"]= defunciones15["Variable"].replace("MÃ©xico", "México") #####################CDMX 
defunciones15["Variable"]= defunciones15["Variable"].replace("VÃ­a pÃºblica", "Vía pública") #####################CDMX 
defunciones15["Variable"]= defunciones15["Variable"].replace("De 15 a 19 aÃ±os", "De 15 a 19 años") #####################CDMX 
defunciones15["Variable"]= defunciones15["Variable"].replace("De 20 a 39 aÃ±os", "De 20 a 39 años") #####################CDMX 
defunciones15["Variable"]= defunciones15["Variable"].replace("De 40 a 55 aÃ±os", "De 40 a 55 años") #####################CDMX 
defunciones15["Variable"]= defunciones15["Variable"].replace("De 55 a 74 aÃ±os", "De 55 a 74 años") #####################CDMX 
defunciones15["Variable"]= defunciones15["Variable"].replace("no especificado", "No especificado") #####################CDMX 
defunciones15["Variable"]= defunciones15["Variable"].replace("familia nuclear", "Familia nuclear") #####################CDMX 
defunciones15["Variable"]= defunciones15["Variable"].replace("UniÃ³n libre", "Unión libre") #####################CDMX 


defunciones16 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/def16_r_femeninas_tabla%20de%20datos.csv", encoding= "Latin-1", 
                   )
defunciones16.replace(["Ã­","Ã¡", "Ã©", "Ã³", "Ã±", "Ãº"], ["í", "á", "é", "ó", "ñ", "ú"], inplace= True)
defunciones16["Variable"]= defunciones16["Variable"].replace("Ciudad de MÃ©xico", "Ciudad de México") #####################CDMX 
defunciones16["Variable"]= defunciones16["Variable"].replace("Veracruz de Ignacio de la Llave", "Veracruz") #####################CDMX 
defunciones16["Variable"]= defunciones16["Variable"].replace("MÃ©xico", "México") #####################CDMX 
defunciones16["Variable"]= defunciones16["Variable"].replace("VÃ­a pÃºblica", "Vía pública") #####################CDMX 
defunciones16["Variable"]= defunciones16["Variable"].replace("De 15 a 19 aÃ±os", "De 15 a 19 años") #####################CDMX 
defunciones16["Variable"]= defunciones16["Variable"].replace("De 20 a 39 aÃ±os", "De 20 a 39 años") #####################CDMX 
defunciones16["Variable"]= defunciones16["Variable"].replace("De 40 a 55 aÃ±os", "De 40 a 55 años") #####################CDMX 
defunciones16["Variable"]= defunciones16["Variable"].replace("De 55 a 74 aÃ±os", "De 55 a 74 años") #####################CDMX 
defunciones16["Variable"]= defunciones16["Variable"].replace("no especificado", "No especificado") #####################CDMX 
defunciones16["Variable"]= defunciones16["Variable"].replace("familia nuclear", "Familia nuclear") #####################CDMX 
defunciones16["Variable"]= defunciones16["Variable"].replace("UniÃ³n libre", "Unión libre") #####################CDMX 




defunciones17 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/def17_r_femeninas_tabla%20de%20datos.csv", encoding= "Latin-1", 
                    )
defunciones17.replace(["Ã­","Ã¡", "Ã©", "Ã³", "Ã±", "Ãº"], ["í", "á", "é", "ó", "ñ", "ú"], inplace= True)
defunciones17["Variable"]= defunciones17["Variable"].replace("Ciudad de MÃ©xico", "Ciudad de México") #####################CDMX 
defunciones17["Variable"]= defunciones17["Variable"].replace("Veracruz de Ignacio de la Llave", "Veracruz") #####################CDMX 
defunciones17["Variable"]= defunciones17["Variable"].replace("MÃ©xico", "México") #####################CDMX 
defunciones17["Variable"]= defunciones17["Variable"].replace("VÃ­a pÃºblica", "Vía pública") #####################CDMX 
defunciones17["Variable"]= defunciones17["Variable"].replace("De 15 a 19 aÃ±os", "De 15 a 19 años") #####################CDMX 
defunciones17["Variable"]= defunciones17["Variable"].replace("De 20 a 39 aÃ±os", "De 20 a 39 años") #####################CDMX 
defunciones17["Variable"]= defunciones17["Variable"].replace("De 40 a 55 aÃ±os", "De 40 a 55 años") #####################CDMX 
defunciones17["Variable"]= defunciones17["Variable"].replace("De 55 a 74 aÃ±os", "De 55 a 74 años") #####################CDMX 
defunciones17["Variable"]= defunciones17["Variable"].replace("no especificado", "No especificado") #####################CDMX 
defunciones17["Variable"]= defunciones17["Variable"].replace("De 30 a 34 aÃ±os", "De 30 a 34 años") #####################CDMX 
defunciones17["Variable"]= defunciones17["Variable"].replace("familia nuclear", "Familia nuclear") #####################CDMX 
defunciones17["Variable"]= defunciones17["Variable"].replace("UniÃ³n libre", "Unión libre") #####################CDMX 



defunciones18 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/def18_r_femeninas_tabla%20de%20datos.csv", encoding= "Latin-1", 
                    )
defunciones18.replace(["Ã­","Ã¡", "Ã©", "Ã³", "Ã±", "Ãº"], ["í", "á", "é", "ó", "ñ", "ú"], inplace= True)
defunciones18["Variable"]= defunciones18["Variable"].replace("Ciudad de MÃ©xico", "Ciudad de México") #####################CDMX 
defunciones18["Variable"]= defunciones18["Variable"].replace("Veracruz de Ignacio de la Llave", "Veracruz") #####################CDMX 
defunciones18["Variable"]= defunciones18["Variable"].replace("MÃ©xico", "México") #####################CDMX 
defunciones18["Variable"]= defunciones18["Variable"].replace("VÃ­a pÃºblica", "Vía pública") #####################CDMX 
defunciones18["Variable"]= defunciones18["Variable"].replace("De 15 a 19 aÃ±os", "De 15 a 19 años") #####################CDMX 
defunciones18["Variable"]= defunciones18["Variable"].replace("De 20 a 39 aÃ±os", "De 20 a 39 años") #####################CDMX 
defunciones18["Variable"]= defunciones18["Variable"].replace("De 40 a 55 aÃ±os", "De 40 a 55 años") #####################CDMX 
defunciones18["Variable"]= defunciones18["Variable"].replace("De 55 a 74 aÃ±os", "De 55 a 74 años") #####################CDMX 
defunciones18["Variable"]= defunciones18["Variable"].replace("no especificado", "No especificado") #####################CDMX 
defunciones18["Variable"]= defunciones18["Variable"].replace("De 30 a 34 aÃ±os", "De 30 a 34 años") #####################CDMX 
defunciones18["Variable"]= defunciones18["Variable"].replace("familia nuclear", "Familia nuclear") #####################CDMX 
defunciones18["Variable"]= defunciones18["Variable"].replace("UniÃ³n libre", "Unión libre") #####################CDMX 


defunciones19 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/def19_r_femeninas_tabla%20de%20datos.csv", encoding= "Latin-1", 
                    )
defunciones19.replace(["Ã­","Ã¡", "Ã©", "Ã³", "Ã±", "Ãº"], ["í", "á", "é", "ó", "ñ", "ú"], inplace= True)
defunciones19["Variable"]= defunciones19["Variable"].replace("Ciudad de MÃ©xico", "Ciudad de México") #####################CDMX 
defunciones19["Variable"]= defunciones19["Variable"].replace("Veracruz de Ignacio de la Llave", "Veracruz") #####################CDMX 
defunciones19["Variable"]= defunciones19["Variable"].replace("MÃ©xico", "México") #####################CDMX 
defunciones19["Variable"]= defunciones19["Variable"].replace("VÃ­a pÃºblica", "Vía pública") #####################CDMX 
defunciones19["Variable"]= defunciones19["Variable"].replace("De 15 a 19 aÃ±os", "De 15 a 19 años") #####################CDMX 
defunciones19["Variable"]= defunciones19["Variable"].replace("De 20 a 39 aÃ±os", "De 20 a 39 años") #####################CDMX 
defunciones19["Variable"]= defunciones19["Variable"].replace("De 40 a 55 aÃ±os", "De 40 a 55 años") #####################CDMX 
defunciones19["Variable"]= defunciones19["Variable"].replace("De 55 a 74 aÃ±os", "De 55 a 74 años") #####################CDMX 
defunciones19["Variable"]= defunciones19["Variable"].replace("no especificado", "No especificado") #####################CDMX 
defunciones19["Variable"]= defunciones19["Variable"].replace("De 30 a 34 aÃ±os", "De 30 a 34 años") #####################CDMX 
defunciones19["Variable"]= defunciones19["Variable"].replace("familia nuclear", "Familia nuclear") #####################CDMX 
defunciones19["Variable"]= defunciones19["Variable"].replace("UniÃ³n libre", "Unión libre") #####################CDMX 



#defunciones20 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/def20_r_femeninas_tabla%20de%20datos.csv", encoding= "Latin-1", 
#                    )
# 2015_______________________________________________________<<<
def_tot15 =defunciones15.iloc[0]['Valor']
def15_tot = defunciones15.iloc[0]['Valor']
agr15_val = defunciones15.iloc[34]['Valor']
agr15_txt = defunciones15.iloc[34]['Variable']
agr215_val  = defunciones15.iloc[35]['Valor']
agr215_txt  = defunciones15.iloc[35]['Variable']
agr315_val  = defunciones15.iloc[36]['Valor']
agr315_txt  = defunciones15.iloc[36]['Variable']

viofm115_val = defunciones15.iloc[21]['Valor']
viofm115_txt = defunciones15.iloc[21]['Variable']
viofm215_val = defunciones15.iloc[22]['Valor']
viofm215_txt = defunciones15.iloc[22]['Variable']

lug115_val = defunciones15.iloc[12]['Valor']
lug115_txt = defunciones15.iloc[12]['Variable']
lug215_val = defunciones15.iloc[13]['Valor']
lug215_txt = defunciones15.iloc[13]['Variable']

aurb15_val = defunciones15.iloc[19]['Valor']
aurb15_txt = defunciones15.iloc[19]['Variable']

ent115_val = defunciones15.iloc[2]['Valor']
ent115_txt = defunciones15.iloc[2]['Variable']
ent215_val = defunciones15.iloc[3]['Valor']
ent215_txt = defunciones15.iloc[3]['Variable']
ent315_val = defunciones15.iloc[4]['Valor']
ent315_txt = defunciones15.iloc[4]['Variable']
ent415_val = defunciones15.iloc[5]['Valor']
ent415_txt = defunciones15.iloc[5]['Variable']
ent515_val = defunciones15.iloc[6]['Valor']
ent515_txt = defunciones15.iloc[6]['Variable']

eda115_val = defunciones15.iloc[24]['Valor']
eda115_txt = defunciones15.iloc[24]['Variable']
eda215_val = defunciones15.iloc[25]['Valor']
eda215_txt = defunciones15.iloc[25]['Variable']
eda315_val = defunciones15.iloc[26]['Valor']
eda315_txt = defunciones15.iloc[26]['Variable']
eda415_val = defunciones15.iloc[27]['Valor']
eda415_txt = defunciones15.iloc[27]['Variable']
eda515_val = defunciones15.iloc[28]['Valor']
eda515_txt = defunciones15.iloc[28]['Variable']

emba115_val = defunciones15.iloc[15]['Valor']
emba115_txt = defunciones15.iloc[15]['Variable']
emba215_val = defunciones15.iloc[16]['Valor']
emba215_txt = defunciones15.iloc[16]['Variable']
emba315_val = defunciones15.iloc[17]['Valor']
emba315_txt = defunciones15.iloc[17]['Variable']

esc115_val = defunciones15.iloc[8]['Valor']
esc115_txt = defunciones15.iloc[8]['Variable']
esc215_val = defunciones15.iloc[9]['Valor']
esc215_txt = defunciones15.iloc[9]['Variable']
esc315_val = defunciones15.iloc[10]['Valor']
esc315_txt = defunciones15.iloc[10]['Variable']

civl115_val = defunciones15.iloc[38]['Valor']
civl115_txt = defunciones15.iloc[38]['Variable']
civl215_val = defunciones15.iloc[39]['Valor']
civl215_txt = defunciones15.iloc[39]['Variable']
civl315_val = defunciones15.iloc[40]['Valor']
civl315_txt = defunciones15.iloc[40]['Variable']
civl415_val = defunciones15.iloc[41]['Valor']
civl415_txt = defunciones15.iloc[41]['Variable']



#2016_______________________________________________________<<<
def_tot16 =defunciones16.iloc[0]['Valor']
def16_tot = defunciones16.iloc[0]['Valor']
agr16_val = defunciones16.iloc[34]['Valor']
agr16_txt = defunciones16.iloc[34]['Variable']
agr216_val  = defunciones16.iloc[35]['Valor']
agr216_txt  = defunciones16.iloc[35]['Variable']
agr316_val  = defunciones16.iloc[36]['Valor']
agr316_txt  = defunciones16.iloc[36]['Variable']

viofm116_val = defunciones16.iloc[21]['Valor']
viofm116_txt = defunciones16.iloc[21]['Variable']
viofm216_val = defunciones16.iloc[22]['Valor']
viofm216_txt = defunciones16.iloc[22]['Variable']

lug116_val = defunciones16.iloc[12]['Valor']
lug116_txt = defunciones16.iloc[12]['Variable']
lug216_val = defunciones16.iloc[13]['Valor']
lug216_txt = defunciones16.iloc[13]['Variable']

aurb16_val = defunciones16.iloc[19]['Valor']
aurb16_txt = defunciones16.iloc[19]['Variable']

ent116_val = defunciones16.iloc[2]['Valor']
ent116_txt = defunciones16.iloc[2]['Variable']
ent216_val = defunciones16.iloc[3]['Valor']
ent216_txt = defunciones16.iloc[3]['Variable']
ent316_val = defunciones16.iloc[4]['Valor']
ent316_txt = defunciones16.iloc[4]['Variable']
ent416_val = defunciones16.iloc[5]['Valor']
ent416_txt = defunciones16.iloc[5]['Variable']
ent516_val = defunciones16.iloc[6]['Valor']
ent516_txt = defunciones16.iloc[6]['Variable']

eda116_val = defunciones16.iloc[24]['Valor']
eda116_txt = defunciones16.iloc[24]['Variable']
eda216_val = defunciones16.iloc[25]['Valor']
eda216_txt = defunciones16.iloc[25]['Variable']
eda316_val = defunciones16.iloc[26]['Valor']
eda316_txt = defunciones16.iloc[26]['Variable']
eda416_val = defunciones16.iloc[27]['Valor']
eda416_txt = defunciones16.iloc[27]['Variable']
eda516_val = defunciones16.iloc[28]['Valor']
eda516_txt = defunciones16.iloc[28]['Variable']

emba116_val = defunciones16.iloc[15]['Valor']
emba116_txt = defunciones16.iloc[15]['Variable']
emba216_val = defunciones16.iloc[16]['Valor']
emba216_txt = defunciones16.iloc[16]['Variable']
emba316_val = defunciones16.iloc[17]['Valor']
emba316_txt = defunciones16.iloc[17]['Variable']


esc116_val = defunciones16.iloc[8]['Valor']
esc116_txt = defunciones16.iloc[8]['Variable']
esc216_val = defunciones16.iloc[9]['Valor']
esc216_txt = defunciones16.iloc[9]['Variable']
esc316_val = defunciones16.iloc[10]['Valor']
esc316_txt = defunciones16.iloc[10]['Variable']

civl116_val = defunciones16.iloc[38]['Valor']
civl116_txt = defunciones16.iloc[38]['Variable']
civl216_val = defunciones16.iloc[39]['Valor']
civl216_txt = defunciones16.iloc[39]['Variable']
civl316_val = defunciones16.iloc[40]['Valor']
civl316_txt = defunciones16.iloc[40]['Variable']
civl416_val = defunciones16.iloc[41]['Valor']
civl416_txt = defunciones16.iloc[41]['Variable']

#2017_______________________________________________________<<<
def_tot17 =defunciones17.iloc[0]['Valor']
def17_tot = defunciones17.iloc[0]['Valor']
agr17_val = defunciones17.iloc[34]['Valor']
agr17_txt = defunciones17.iloc[34]['Variable']
agr217_val  = defunciones17.iloc[35]['Valor']
agr217_txt  = defunciones17.iloc[35]['Variable']
agr317_val  = defunciones17.iloc[36]['Valor']
agr317_txt  = defunciones17.iloc[36]['Variable']

viofm117_val = defunciones17.iloc[21]['Valor']
viofm117_txt = defunciones17.iloc[21]['Variable']
viofm217_val = defunciones17.iloc[22]['Valor']
viofm217_txt = defunciones17.iloc[22]['Variable']

lug117_val = defunciones17.iloc[12]['Valor']
lug117_txt = defunciones17.iloc[12]['Variable']
lug217_val = defunciones17.iloc[13]['Valor']
lug217_txt = defunciones17.iloc[13]['Variable']

aurb17_val = defunciones17.iloc[19]['Valor']
aurb17_txt = defunciones17.iloc[19]['Variable']

ent117_val = defunciones17.iloc[2]['Valor']
ent117_txt = defunciones17.iloc[2]['Variable']
ent217_val = defunciones17.iloc[3]['Valor']
ent217_txt = defunciones17.iloc[3]['Variable']
ent317_val = defunciones17.iloc[4]['Valor']
ent317_txt = defunciones17.iloc[4]['Variable']
ent417_val = defunciones17.iloc[5]['Valor']
ent417_txt = defunciones17.iloc[5]['Variable']
ent517_val = defunciones17.iloc[6]['Valor']
ent517_txt = defunciones17.iloc[6]['Variable']

eda117_val = defunciones17.iloc[24]['Valor']
eda117_txt = defunciones17.iloc[24]['Variable']
eda217_val = defunciones17.iloc[25]['Valor']
eda217_txt = defunciones17.iloc[25]['Variable']
eda317_val = defunciones17.iloc[26]['Valor']
eda317_txt = defunciones17.iloc[26]['Variable']
eda417_val = defunciones17.iloc[27]['Valor']
eda417_txt = defunciones17.iloc[27]['Variable']
eda517_val = defunciones17.iloc[28]['Valor']
eda517_txt = defunciones17.iloc[28]['Variable']

emba117_val = defunciones17.iloc[15]['Valor']
emba117_txt = defunciones17.iloc[15]['Variable']
emba217_val = defunciones17.iloc[16]['Valor']
emba217_txt = defunciones17.iloc[16]['Variable']
emba317_val = defunciones17.iloc[17]['Valor']
emba317_txt = defunciones17.iloc[17]['Variable']

esc117_val = defunciones17.iloc[8]['Valor']
esc117_txt = defunciones17.iloc[8]['Variable']
esc217_val = defunciones17.iloc[9]['Valor']
esc217_txt = defunciones17.iloc[9]['Variable']
esc317_val = defunciones17.iloc[10]['Valor']
esc317_txt = defunciones17.iloc[10]['Variable']

civl117_val = defunciones17.iloc[38]['Valor']
civl117_txt = defunciones17.iloc[38]['Variable']
civl217_val = defunciones17.iloc[39]['Valor']
civl217_txt = defunciones17.iloc[39]['Variable']
civl317_val = defunciones17.iloc[40]['Valor']
civl317_txt = defunciones17.iloc[40]['Variable']
civl417_val = defunciones17.iloc[41]['Valor']
civl417_txt = defunciones17.iloc[41]['Variable']

#2018_______________________________________________________<<<
def_tot18 =defunciones18.iloc[0]['Valor']
def18_tot = defunciones18.iloc[0]['Valor']
agr18_val = defunciones18.iloc[34]['Valor']
agr18_txt = defunciones18.iloc[34]['Variable']
agr218_val  = defunciones18.iloc[35]['Valor']
agr218_txt  = defunciones18.iloc[35]['Variable']
agr318_val  = defunciones18.iloc[36]['Valor']
agr318_txt  = defunciones18.iloc[36]['Variable']

viofm118_val = defunciones18.iloc[21]['Valor']
viofm118_txt = defunciones18.iloc[21]['Variable']
viofm218_val = defunciones18.iloc[22]['Valor']
viofm218_txt = defunciones18.iloc[22]['Variable']

lug118_val = defunciones18.iloc[12]['Valor']
lug118_txt = defunciones18.iloc[12]['Variable']
lug218_val = defunciones18.iloc[13]['Valor']
lug218_txt = defunciones18.iloc[13]['Variable']

aurb18_val = defunciones18.iloc[19]['Valor']
aurb18_txt = defunciones18.iloc[19]['Variable']

ent118_val = defunciones18.iloc[2]['Valor']
ent118_txt = defunciones18.iloc[2]['Variable']
ent218_val = defunciones18.iloc[3]['Valor']
ent218_txt = defunciones18.iloc[3]['Variable']
ent318_val = defunciones18.iloc[4]['Valor']
ent318_txt = defunciones18.iloc[4]['Variable']
ent418_val = defunciones18.iloc[5]['Valor']
ent418_txt = defunciones18.iloc[5]['Variable']
ent518_val = defunciones18.iloc[6]['Valor']
ent518_txt = defunciones18.iloc[6]['Variable']

eda118_val = defunciones18.iloc[24]['Valor']
eda118_txt = defunciones18.iloc[24]['Variable']
eda218_val = defunciones18.iloc[25]['Valor']
eda218_txt = defunciones18.iloc[25]['Variable']
eda318_val = defunciones18.iloc[26]['Valor']
eda318_txt = defunciones18.iloc[26]['Variable']
eda418_val = defunciones18.iloc[27]['Valor']
eda418_txt = defunciones18.iloc[27]['Variable']
eda518_val = defunciones18.iloc[28]['Valor']
eda518_txt = defunciones18.iloc[28]['Variable']

emba118_val = defunciones18.iloc[15]['Valor']
emba118_txt = defunciones18.iloc[15]['Variable']
emba218_val = defunciones18.iloc[16]['Valor']
emba218_txt = defunciones18.iloc[16]['Variable']
emba318_val = defunciones18.iloc[17]['Valor']
emba318_txt = defunciones18.iloc[17]['Variable']

esc118_val = defunciones18.iloc[8]['Valor']
esc118_txt = defunciones18.iloc[8]['Variable']
esc218_val = defunciones18.iloc[9]['Valor']
esc218_txt = defunciones18.iloc[9]['Variable']
esc318_val = defunciones18.iloc[10]['Valor']
esc318_txt = defunciones18.iloc[10]['Variable']

civl118_val = defunciones18.iloc[38]['Valor']
civl118_txt = defunciones18.iloc[38]['Variable']
civl218_val = defunciones18.iloc[39]['Valor']
civl218_txt = defunciones18.iloc[39]['Variable']
civl318_val = defunciones18.iloc[40]['Valor']
civl318_txt = defunciones18.iloc[40]['Variable']
civl418_val = defunciones18.iloc[41]['Valor']
civl418_txt = defunciones18.iloc[41]['Variable']

#2019_______________________________________________________<<<
def_tot19 =defunciones19.iloc[0]['Valor']
def19_tot = defunciones19.iloc[0]['Valor']
agr19_val = defunciones19.iloc[34]['Valor']
agr19_txt = defunciones19.iloc[34]['Variable']
agr219_val  = defunciones19.iloc[35]['Valor']
agr219_txt  = defunciones19.iloc[35]['Variable']
agr319_val  = defunciones19.iloc[36]['Valor']
agr319_txt  = defunciones19.iloc[36]['Variable']

viofm119_val = defunciones19.iloc[21]['Valor']
viofm119_txt = defunciones19.iloc[21]['Variable']
viofm219_val = defunciones19.iloc[22]['Valor']
viofm219_txt = defunciones19.iloc[22]['Variable']

lug119_val = defunciones19.iloc[12]['Valor']
lug119_txt = defunciones19.iloc[12]['Variable']
lug219_val = defunciones19.iloc[13]['Valor']
lug219_txt = defunciones19.iloc[13]['Variable']

aurb19_val = defunciones19.iloc[19]['Valor']
aurb19_txt = defunciones19.iloc[19]['Variable']

ent119_val = defunciones19.iloc[2]['Valor']
ent119_txt = defunciones19.iloc[2]['Variable']
ent219_val = defunciones19.iloc[3]['Valor']
ent219_txt = defunciones19.iloc[3]['Variable']
ent319_val = defunciones19.iloc[4]['Valor']
ent319_txt = defunciones19.iloc[4]['Variable']
ent419_val = defunciones19.iloc[5]['Valor']
ent419_txt = defunciones19.iloc[5]['Variable']
ent519_val = defunciones19.iloc[6]['Valor']
ent519_txt = defunciones19.iloc[6]['Variable']

eda119_val = defunciones19.iloc[24]['Valor']
eda119_txt = defunciones19.iloc[24]['Variable']
eda219_val = defunciones19.iloc[25]['Valor']
eda219_txt = defunciones19.iloc[25]['Variable']
eda319_val = defunciones19.iloc[26]['Valor']
eda319_txt = defunciones19.iloc[26]['Variable']
eda419_val = defunciones19.iloc[27]['Valor']
eda419_txt = defunciones19.iloc[27]['Variable']
eda519_val = defunciones19.iloc[28]['Valor']
eda519_txt = defunciones19.iloc[28]['Variable']

emba119_val = defunciones19.iloc[15]['Valor']
emba119_txt = defunciones19.iloc[15]['Variable']
emba219_val = defunciones19.iloc[16]['Valor']
emba219_txt = defunciones19.iloc[16]['Variable']
emba319_val = defunciones19.iloc[17]['Valor']
emba319_txt = defunciones19.iloc[17]['Variable']

esc119_val = defunciones19.iloc[8]['Valor']
esc119_txt = defunciones19.iloc[8]['Variable']
esc219_val = defunciones19.iloc[9]['Valor']
esc219_txt = defunciones19.iloc[9]['Variable']
esc319_val = defunciones19.iloc[10]['Valor']
esc319_txt = defunciones19.iloc[10]['Variable']

civl119_val = defunciones19.iloc[38]['Valor']
civl119_txt = defunciones19.iloc[38]['Variable']
civl219_val = defunciones19.iloc[39]['Valor']
civl219_txt = defunciones19.iloc[39]['Variable']
civl319_val = defunciones19.iloc[40]['Valor']
civl319_txt = defunciones19.iloc[40]['Variable']
civl419_val = defunciones19.iloc[41]['Valor']
civl419_txt = defunciones19.iloc[41]['Variable']

#os.chdir(r"C:\Users\PRIME\AnacondaProjects\Project_curso\\")

delitos = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/feminicidios2015_2021.csv")
delitos.drop('Unnamed: 0',1, inplace=True)

delitos.groupby(['Año','Entidad','Tipo de delito'])['Enero', 
                 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
       'Julio', 'Agosto', 'Septiembre', 'Octubre',
       'Noviembre', 'Diciembre'].sum().to_csv("00.csv",  header=True)

fem= pd.read_csv("00.csv")


############################################### separación de años

year15= fem[fem.Año == 2015]
year16= fem[fem.Año == 2016]
year17= fem[fem.Año == 2017]
year18= fem[fem.Año == 2018]
year19= fem[fem.Año == 2019]
year20= fem[fem.Año == 2020]
year21= fem[fem.Año == 2021]

############################################### Agregar suffix de años

y15 = year15.add_suffix('15')
y15.rename(columns ={'Año15': 'Año', 'Tipo de delito15': 'Tipo de delito', 'Unnamed: 015' : 'Unnamed: 0',
                            'Entidad15': 'Entidad'}, inplace = True)

y16 = year16.add_suffix('16')
y16.rename(columns ={'Año16': 'Año', 'Tipo de delito16': 'Tipo de delito', 'Unnamed: 016' : 'Unnamed: 0',
                            'Entidad16': 'Entidad'}, inplace = True)

y17 = year17.add_suffix('17')
y17.rename(columns ={'Año17': 'Año', 'Tipo de delito17': 'Tipo de delito', 'Unnamed: 017' : 'Unnamed: 0',
                            'Entidad17': 'Entidad'}, inplace = True)

y18= year18.add_suffix('18')
y18.rename(columns ={'Año18': 'Año', 'Tipo de delito18': 'Tipo de delito','Unnamed: 018' : 'Unnamed: 0',
                            'Entidad18': 'Entidad'}, inplace = True)

y19= year19.add_suffix('19')
y19.rename(columns ={'Año19': 'Año', 'Tipo de delito19': 'Tipo de delito', 'Unnamed: 019' : 'Unnamed: 0',
                            'Entidad19': 'Entidad'}, inplace = True)

y20= year20.add_suffix('20')
y20.rename(columns ={'Año20': 'Año', 'Tipo de delito20': 'Tipo de delito','Unnamed: 020' : 'Unnamed: 0',
                            'Entidad20': 'Entidad'}, inplace = True)

y21= year21.add_suffix('21')
y21.rename(columns ={'Año21': 'Año', 'Tipo de delito21': 'Tipo de delito','Unnamed: 021' : 'Unnamed: 0',
                            'Entidad21': 'Entidad'}, inplace = True)


############################################### Concat todos los años

fa = y15.merge(y16, on="Entidad",  how="inner")
fb = fa.merge(y17, on="Entidad",  how="inner")
fc = fb.merge(y18, on="Entidad",  how="inner")
fd = fc.merge(y19, on="Entidad",  how="inner")
fe = fd.merge(y20, on="Entidad",  how="inner")
ff = fe.merge(y21, on="Entidad",  how="inner")
                    
femi15_21 = ff[[
 'Entidad','Enero15','Febrero15','Marzo15','Abril15','Mayo15','Junio15',
 'Julio15','Agosto15','Septiembre15','Octubre15','Noviembre15','Diciembre15',
 
 'Enero16','Febrero16','Marzo16','Abril16','Mayo16','Junio16','Julio16',
 'Agosto16','Septiembre16','Octubre16','Noviembre16','Diciembre16',

 'Enero17','Febrero17','Marzo17','Abril17','Mayo17','Junio17','Julio17',
 'Agosto17','Septiembre17','Octubre17','Noviembre17','Diciembre17',
    
 'Enero18','Febrero18','Marzo18','Abril18','Mayo18','Junio18','Julio18',
 'Agosto18','Septiembre18','Octubre18','Noviembre18','Diciembre18',
 
 'Enero19','Febrero19','Marzo19','Abril19','Mayo19','Junio19','Julio19',
 'Agosto19','Septiembre19','Octubre19','Noviembre19','Diciembre19',

 'Enero20','Febrero20','Marzo20','Abril20','Mayo20','Junio20','Julio20',
 'Agosto20','Septiembre20','Octubre20','Noviembre20','Diciembre20',
    
 'Enero21','Febrero21','Marzo21','Abril21',#'Mayo21','Junio21','Julio21',
# 'Agosto21','Septiembre21','Octubre21','Noviembre21','Diciembre21'
             ]]



##CRear columna de TOTAL ANUAL 
femi15_21['Total2015']= femi15_21[[ 'Enero15', 'Febrero15', 'Marzo15', 'Abril15', 'Mayo15',
                               'Junio15', 'Julio15', 'Agosto15', 'Septiembre15', 'Octubre15',
                               'Noviembre15', 'Diciembre15',]].sum(axis=1)
femi15_21['Total2016']= femi15_21[[ 'Enero16', 'Febrero16', 'Marzo16', 'Abril16', 'Mayo16',
                               'Junio16', 'Julio16', 'Agosto16', 'Septiembre16', 'Octubre16',
                               'Noviembre16', 'Diciembre16',]].sum(axis=1)
femi15_21['Total2017']= femi15_21[[ 'Enero17', 'Febrero17', 'Marzo17', 'Abril17', 'Mayo17',
                               'Junio17', 'Julio17', 'Agosto17', 'Septiembre17', 'Octubre17',
                               'Noviembre17', 'Diciembre17',]].sum(axis=1)
femi15_21['Total2018']= femi15_21[[ 'Enero18', 'Febrero18', 'Marzo18', 'Abril18', 'Mayo18',
                               'Junio18', 'Julio18', 'Agosto18', 'Septiembre18', 'Octubre18',
                               'Noviembre18', 'Diciembre18',]].sum(axis=1)
femi15_21['Total2019']= femi15_21[[ 'Enero19', 'Febrero19', 'Marzo19', 'Abril19', 'Mayo19',
                               'Junio19', 'Julio19', 'Agosto19', 'Septiembre19', 'Octubre19',
                               'Noviembre19', 'Diciembre19',]].sum(axis=1)
femi15_21['Total2020']= femi15_21[[ 'Enero20', 'Febrero20', 'Marzo20', 'Abril20', 'Mayo20',
                               'Junio20', 'Julio20', 'Agosto20', 'Septiembre20', 'Octubre20',
                               'Noviembre20', 'Diciembre20',]].sum(axis=1)

femi15_21['Total2021']= femi15_21[[ 'Enero21','Febrero21', 'Marzo21', 'Abril21',# 'Mayo21',
                                   #'Junio21','Julio21','Agosto21','Septiembre21','Octubre21',
                                   #'Noviembre21','Diciembre21'
                                  ]].sum(axis=1)


#identificadores
conf_2015= femi15_21.Total2015.sum()
conf_2016= femi15_21.Total2016.sum()
conf_2017= femi15_21.Total2017.sum()
conf_2018= femi15_21.Total2018.sum()
conf_2019= femi15_21.Total2019.sum()
conf_2020= femi15_21.Total2020.sum()
conf_2021= femi15_21.Total2021.sum()



################################################## PREPARA GRAFICA MENSUAL
pagra = ff[[
  'Enero15', 'Febrero15', 'Marzo15', 'Abril15', 'Mayo15', 'Junio15', 'Julio15', 'Agosto15', 
    'Septiembre15', 'Octubre15', 'Noviembre15', 'Diciembre15',
 
 'Enero16', 'Febrero16', 'Marzo16', 'Abril16', 'Mayo16', 'Junio16', 'Julio16', 'Agosto16', 
    'Septiembre16', 'Octubre16', 'Noviembre16', 'Diciembre16',

 'Enero17', 'Febrero17', 'Marzo17', 'Abril17', 'Mayo17', 'Junio17', 'Julio17', 'Agosto17', 
    'Septiembre17', 'Octubre17', 'Noviembre17', 'Diciembre17', 
    'Enero18', 'Febrero18', 'Marzo18',    'Abril18', 'Mayo18', 'Junio18', 'Julio18', 'Agosto18',
    'Septiembre18', 'Octubre18', 'Noviembre18', 'Diciembre18',
 
 'Enero19', 'Febrero19', 'Marzo19', 'Abril19', 'Mayo19', 'Junio19', 'Julio19', 'Agosto19', 
    'Septiembre19', 'Octubre19', 'Noviembre19', 'Diciembre19',

 'Enero20', 'Febrero20', 'Marzo20', 'Abril20', 'Mayo20', 'Junio20', 'Julio20', 'Agosto20',
    'Septiembre20','Octubre20', 'Noviembre20', 'Diciembre20',

 'Enero21', 'Febrero21', 'Marzo21', 'Abril21', #'Mayo21', #'Junio21',# 'Julio21',# 'Agosto21',
  #  'Septiembre21','Octubre21','Noviembre21','Diciembre21'
            ]]


pagrafm = pagra.stb.subtotal()
pagrafm.to_csv("0000procesod.csv")
#Selecciona ultima columna (Totales)
other  = pd.read_csv('0000procesod.csv')
other_s = other.iloc[32]
other_b = pd.DataFrame(other_s)
other_b.to_csv('0000procesodi.csv')
vuelve_a_abrir = pd.read_csv('0000procesodi.csv')
##Elimina filas 0 a 4 
gra_mes = vuelve_a_abrir.drop([0])
#Renombra titulo de columna
gra_mes = gra_mes.rename(columns= {"Unnamed: 0": "Mes"})
gra_mes = gra_mes.rename(columns= {"32": "Total"})
gra_mes['Total'] = pd.to_numeric(gra_mes['Total'])


#Grafica mensual 
graf_meses = go.Figure()
graf_meses.add_trace(go.Bar(x=gra_mes['Mes'],y=gra_mes['Total'],
                marker_color='indianred'  # cambiar nuemeritos de rgb
                ))
graf_meses.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 12,
    yaxis=dict(
        title='Acumulados mensuales',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    #autosize=False,
    #width=1000,
    #height=400
    )





#- FILE JSON PARA ENTIDADES ------------------------------------------------------------------------------



################################################ SUMA TODOS LOS AÑOS ranking de municipios por estado (3edos)

#filtro de feminicidio
delitos.groupby(['Municipio','Entidad',])['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo',
                                             'Junio','Julio', 'Agosto', 'Septiembre', 'Octubre',
                                             'Noviembre', 'Diciembre'].sum().to_csv('0000procesofem.csv')

fem_filter1=pd.read_csv('0000procesofem.csv')
fem_filter1[['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
                                 'Septiembre','Octubre','Noviembre','Diciembre']] = fem_filter1[['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
                                 'Septiembre','Octubre','Noviembre','Diciembre']].astype(int)
    
fem_filter1['Total']=fem_filter1[['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
                                 'Septiembre','Octubre','Noviembre','Diciembre']].sum(1)



#- FILE MUNICIPIOS ------------------------------------------------------------------------------

fem_filter1.fillna(0, inplace=True) 
fem_filter1['Total']=fem_filter1['Total'].astype(int)


############################################### filtro para estados(4) e identifiación de mpios y abs feminicidios

# estado 1
estado1=fem_filter1[fem_filter1.Entidad=='México']
edo1orden=estado1[['Municipio','Total']].sort_values('Total',ascending=False)
#1
edo1mpio1=edo1orden.iloc[0]['Municipio']
edo1mpio1v=edo1orden.iloc[0]['Total']
#2
edo1mpio2=edo1orden.iloc[1]['Municipio']
edo1mpio2v=edo1orden.iloc[1]['Total']
#3
edo1mpio3=edo1orden.iloc[2]['Municipio']
edo1mpio3v=edo1orden.iloc[2]['Total']
#4
edo1mpio4=edo1orden.iloc[3]['Municipio']
edo1mpio4v=edo1orden.iloc[3]['Total']
#5
edo1mpio5=edo1orden.iloc[4]['Municipio']
edo1mpio5v=edo1orden.iloc[4]['Total']


# estado 2
estado2=fem_filter1[fem_filter1.Entidad=='Veracruz de Ignacio de la Llave']
edo2orden=estado2[['Municipio','Total']].sort_values('Total',ascending=False)
#1
edo2mpio1=edo2orden.iloc[0]['Municipio']
edo2mpio1v=edo2orden.iloc[0]['Total']
#2
edo2mpio2=edo2orden.iloc[1]['Municipio']
edo2mpio2v=edo2orden.iloc[1]['Total']
#3
edo2mpio3=edo2orden.iloc[2]['Municipio']
edo2mpio3v=edo2orden.iloc[2]['Total']
#4
edo2mpio4=edo2orden.iloc[3]['Municipio']
edo2mpio4v=edo2orden.iloc[3]['Total']
#5
edo2mpio5=edo2orden.iloc[4]['Municipio']
edo2mpio5v=edo2orden.iloc[4]['Total']


# estado 3
estado3=fem_filter1[fem_filter1.Entidad=='Ciudad de México']
edo3orden=estado3[['Municipio','Total']].sort_values('Total',ascending=False)
#1
edo3mpio1=edo3orden.iloc[0]['Municipio']
edo3mpio1v=edo3orden.iloc[0]['Total']
#2
edo3mpio2=edo3orden.iloc[1]['Municipio']
edo3mpio2v=edo3orden.iloc[1]['Total']
#3
edo3mpio3=edo3orden.iloc[2]['Municipio']
edo3mpio3v=edo3orden.iloc[2]['Total']
#4
edo3mpio4=edo3orden.iloc[3]['Municipio']
edo3mpio4v=edo3orden.iloc[3]['Total']
#5
edo3mpio5=edo3orden.iloc[4]['Municipio']
edo3mpio5v=edo3orden.iloc[4]['Total']


# estado 4
estado4=fem_filter1[fem_filter1.Entidad=='Jalisco']
edo4orden=estado4[['Municipio','Total']].sort_values('Total',ascending=False)
#1
edo4mpio1=edo4orden.iloc[0]['Municipio']
edo4mpio1v=edo4orden.iloc[0]['Total']
#2
edo4mpio2=edo4orden.iloc[1]['Municipio']
edo4mpio2v=edo4orden.iloc[1]['Total']
#3
edo4mpio3=edo4orden.iloc[2]['Municipio']
edo4mpio3v=edo4orden.iloc[2]['Total']
#4
edo4mpio4=edo4orden.iloc[3]['Municipio']
edo4mpio4v=edo4orden.iloc[3]['Total']
#5
edo4mpio5=edo4orden.iloc[4]['Municipio']
edo4mpio5v=edo4orden.iloc[4]['Total']



######################################################### tablas Ranking municipios
# tabla 1
patabla1 = {'Mpio' : [edo1mpio1,edo1mpio2,edo1mpio3,edo1mpio4,edo1mpio5],
            'Casos': [edo1mpio1v,edo1mpio2v,edo1mpio3v,edo1mpio4v,edo1mpio5v],}

patabla1a = pd.DataFrame (patabla1, columns = ['Mpio','Casos'])


############## tabla 2
patabla2 = {'Mpio'  : [edo2mpio1,edo2mpio2,edo2mpio3,edo2mpio4,edo2mpio5],
            'Casos' : [edo2mpio1v,edo2mpio2v,edo2mpio3v,edo2mpio4v,edo2mpio5v],}

patabla2a = pd.DataFrame (patabla2, columns = ['Mpio','Casos'])


############## tabla 3
patabla3 = {'Mpio'  : [edo3mpio1,edo3mpio2,edo3mpio3,edo3mpio4,edo3mpio5],
            'Casos' : [edo3mpio1v,edo3mpio2v,edo3mpio3v,edo3mpio4v,edo3mpio5v],}

patabla3a = pd.DataFrame (patabla3, columns = ['Mpio','Casos'])


############## tabla 4
patabla4 = {'Mpio'  : [edo4mpio1,edo4mpio2,edo4mpio3,edo4mpio4,edo4mpio5],
            'Casos' : [edo4mpio1v,edo4mpio2v,edo4mpio3v,edo4mpio4v,edo4mpio5v],}

patabla4a = pd.DataFrame (patabla4, columns = ['Mpio','Casos'])




######################################################### Graf. Tasas de feminicidios por entidad 2015-2020

junto1 = pd.read_csv('https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/POB_15_21.csv')
fem15_21 = femi15_21[['Entidad', 'Total2015', 'Total2016', 'Total2017',
       'Total2018', 'Total2019', 'Total2020', 'Total2021']]

junto15_21 = fem15_21.merge(junto1,right_on='NOM_ENT',left_on='Entidad')
junto15_21["Entidad"].replace('Veracruz de Ignacio de la Llave','Veracruz' , inplace=True)

junto15_21['Totfem1521']=junto15_21[['Total2015', 'Total2016', 'Total2017', 'Total2018','Total2019', 'Total2020', 'Total2021']].sum(1)
junto15_21['Totpob1521']=junto15_21[['POB15', 'POB16', 'POB17', 'POB18','POB19', 'POB20', 'POB21']].sum(1)
junto15_21['Tasa1521']=((junto15_21.Totfem1521/junto15_21.Totpob1521)*100000).round(2)

TasasFem15_21index=junto15_21[['Entidad','Totfem1521','Totpob1521','Tasa1521']].sort_values('Tasa1521',ascending=False)


######################################################### Grafica Totales

graf_tasafem = go.Figure()
graf_tasafem.add_trace(go.Bar(x=TasasFem15_21index['Entidad'],y=TasasFem15_21index['Tasa1521'],
                marker_color='sandybrown'  # cambiar nuemeritos de rgb
                ))

graf_tasafem.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    #title='Tasa feminicidio periodo 2015-2020',
    xaxis_tickfont_size= 12,
    yaxis=dict(
        title='Tasa cada 100 000 habitantes',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    autosize=True,
#    width=2100,
#    height=600
    )


######################################################### Grafica Total

TasasTot15_21index=junto15_21[['Entidad','Totfem1521','Totpob1521','Tasa1521']].sort_values('Totfem1521',ascending=False)

graf_totfem = go.Figure()
graf_totfem.add_trace(go.Bar(x=TasasTot15_21index['Entidad'],y=TasasTot15_21index['Totfem1521'],
                marker_color='indianred'  # cambiar nuemeritos de rgb
                ))

graf_totfem.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    #title='Tasa feminicidio periodo 2015-2020',
    xaxis_tickfont_size= 12,
    yaxis=dict(
        title='Tasa cada 100 000 habitantes',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    autosize=True,
 #   width=2100,
  #  height=600
    )



####################################

# A P P

####################################

########### Define your variables
mytitle=' '
tabtitle='Feminicidios'
sourceurl='https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva?state=published'
autores = ('https://raw.githubusercontent.com/winik-pg/exercises_pythoncitos/master/Autores.docx')


server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. LUX], server=server)

body = html.Div([
# Cintillo 000
    
   html.Br(),
    
   dbc.Row([
                                    #https://github.com/fdealbam/CamaraDiputados/blob/b11ef31e8e0f73e1a4a06ce60402563e1bd0122e/application/static/logocamara.jfif
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/ce2cda9ccf7732861b8494b36562ebe9c8c642a6/application/static/logo%20cesopycamara.jpeg?raw=true"),
                        width=5, md={'size': 2,  "offset": 2, }),
            
           dbc.Col(html.H6(" Centro de Estudios Sociales y de Opinión Pública," 
                           " Cámara de Diputados"
                           " México, 2021 "),
                  width={'size': 3, 'offset': 0}),
               ], justify="end",),
            
   
   
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
    
        dbc.Row(
           [
               #dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true"),
               #         width={'size': 1,  "offset": 1}),
               dbc.Col(html.P("Feminicidios en México (2015-2020)"),
                        style={"font-size": 86, "text-align": "center"}),
           ], justify= "start"),

    
#Cintillo 00    
    dbc.Row(
           [
               dbc.Col(html.H6(d2),           #Fecha de actualización
               width={'size' : "auto",
                      'offset' : 2}), 
               dbc.Col(html.H6("Fuente: Datos abiertos de incidencia delictiva, SENSNSP"),
                        width={'size': 5,  "offset":2 }),
            ]),
               
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
    
#cintillo 0
    
       dbc.Row(
           [
               dbc.Col(html.H1(["Casos ", 
                                dbc.Badge("anuales", color="info", className="mr-1")]),
                        width={'size': 8,  "offset":1 }),
            ]),

       html.Br(),
    
# prueba recuadros
    
       dbc.Row([
       dbc.Col(dbc.Button(([html.H5("2015", style={"font-size": 18,"color": "black","background-color": "white"}),
                            html.H1(conf_2015, style={"font-size": 64, "color": "black","background-color": "white"}),
                            dbc.CardImg(src="https://github.com/fdealbam/feminicidios/blob/main/application/static/Mapa%20Feminicidio%20Total2015.jpeg?raw=true", 
                                        style={"background-color":"white"}),
               ]), style={"background-color":"white",
                         "box-shadow": "10px 20px 30px black",
                         'margin-left': '10px',
                        'width': '250px'
                         }, disabled=True)),
    
       dbc.Col(dbc.Button(([html.H5("2016", style= {"font-size": 18,"color": "black","background-color": "white",}),
                            html.H1(conf_2016,style= {"font-size": 64, "color": "black","background-color": "white",}),
                            dbc.CardImg(src="https://github.com/fdealbam/feminicidios/blob/main/application/static/Mapa%20Feminicidio%20Total2016.jpeg?raw=true",                               style= {"background-color": "white"}),
               ]),style={"background-color":"white",
                         "box-shadow": "10px 20px 30px black",
                        'width': '250px',
                         #'margin-left': '-390px'
                        }, disabled=True)),

        dbc.Col(dbc.Button(([html.H5("2017", style= {"font-size": 18,"color": "black","background-color": "white",}),
                            html.H1(conf_2017,style= {"font-size": 64, "color": "black","background-color": "white",}),
                            dbc.CardImg(src="https://github.com/fdealbam/feminicidios/blob/main/application/static/Mapa%20Feminicidio%20Total2017.jpeg?raw=true",                               style= {"background-color": "white"}),
               ]),style={"background-color":"white",
                         "box-shadow": "10px 20px 30px black",
                        'width': '250px',
                         #'margin-left': '-90px'
                        }, disabled=True)),

       dbc.Col(dbc.Button(([html.H5("2018", style= {"font-size": 18,"color": "black","background-color": "white",}),
                            html.H1(conf_2018,style= {"font-size": 64, "color": "black","background-color": "white",}),
                            dbc.CardImg(src="https://github.com/fdealbam/feminicidios/blob/main/application/static/Mapa%20Feminicidio%20Total2018.jpeg?raw=true",                               style= {"background-color": "white"}),
               ]),style={"background-color":"white",
                         "box-shadow": "10px 20px 30px black",
                        'width': '250px',
                         #'margin-left': '-390px'
                        }, disabled=True)),
           
       dbc.Col(dbc.Button(([html.H5("2019", style= {"font-size": 18,"color": "black","background-color": "white",}),
                            html.H1(conf_2019,style= {"font-size": 64, "color": "black","background-color": "white",}),
                            dbc.CardImg(src="https://github.com/fdealbam/feminicidios/blob/main/application/static/Mapa%20Feminicidio%20Total2019.jpeg?raw=true",                               style= {"background-color": "white"}),
               ]),style={"background-color":"white",
                         "box-shadow": "10px 20px 30px black",
                        'width': '250px',
                         #'margin-left': '-390px'
                        }, disabled=True)),
       dbc.Col(dbc.Button(([html.H5("2020", style= {"font-size": 18,"color": "black","background-color": "white",}),
                            html.H1(conf_2020,style= {"font-size": 64, "color": "red","background-color": "white",}),
                            dbc.CardImg(src="https://github.com/fdealbam/feminicidios/blob/main/application/static/Mapa%20Feminicidio%20Total2020.jpeg?raw=true",                               style= {"background-color": "white"}),
               ]),style={"background-color":"white",
                         "box-shadow": "10px 20px 30px black",
                        'width': '250px',
                         #'margin-left': '-390px'
                        }, disabled=True)),
           
    ],style={ "background-color": "white",
              #"box-shadow": "10px 20px 30px black",
              'margin-left': '50px'}),
    
    
 
       html.Br(),
    

    
       html.Br(),

       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
   
       
#---------Grafica mensual
     dbc.Row(
           [
               dbc.Col(html.H1(["Casos ", 
                       dbc.Badge("mensuales", color="info", className="mr-1")]), 
                                       width={'size': 11,  "offset":1 })]),
       dbc.Row(
           [        
               dbc.Col(html.H5("(hasta abril 2021)"),
                                       width={ 'size': 3, "offset":1 }),

            ]),
   
    dbc.Row(
        [
            dbc.Col(dcc.Graph(figure=graf_meses, config= "autosize", style={"margin-left":"50px"})),
        ]),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
    
##Cintillo mapas y ranking

    #títulos
     dbc.Row(
           [
               dbc.Col(html.H1([dbc.Badge("Municipios", color="info", className="ml-1"), 
                               " en entidades con más casos acumulados ",]),
                       
                        width={'size': 10,  "offset":1 }),
            ]),
    html.Br(),
    html.Br(),
    
    #4 CUADROS
    
     dbc.Row([
       dbc.Col(dbc.Button(([html.P("México", style={"font-size": 30,"color": "black","background-color": "white"}),
                            dbc.CardImg(src="https://github.com/fdealbam/feminicidios/blob/main/application/static/mx2.jpeg?raw=true",
                                        style={"background-color":"white"}),
                            html.P(
                           "Los 10 municipios con mayor número de casos de feminicidios son:"
                           " Ecatepec de Morelos (56), Chimalhuacán (35), Nezahualcóyotl (31)"
                           ", Toluca (27), Naucalpan de Juárez (22), Ixtapaluca (22), Zumpango"
                           "(21), Tecámac (19), Cuautitlán Izcalli (19), y Valle de Chalco"
                           "Solidaridad (16).",
                       style={'font-size': 14, "font-family":"Arial", "text-align":"justify" }),
               ]), style={"background-color":"white",
                         "box-shadow": "10px 20px 30px black",
                         'margin-left': '300px',
                        'width': '450px'
                         }, disabled=True)),
    
     
         dbc.Col(dbc.Button(([html.H3("Veracruz",style={"font-size": 30,"color": "black","background-color": "white"}),
                     dbc.CardImg(src="https://github.com/fdealbam/feminicidios/blob/main/application/static/ver2.jpeg?raw=true"),
                        html.P(
                           "Los 10 municipios con mayor número de casos de feminicidios son:"
                           " Veracruz (49), Xalapa (42), Coatzacoalcos (25), Córdoba (24), "
                           "Poza Rica de Hidalgo (17), Tuxpan (13), Papantla (12), Tierra "
                           "Blanca (11), Minatitlán (11), y San Andrés Tuxtla (11).",
                       style={'font-size': 14, "font-family":"Arial", "text-align":"justify" }),
                       ]), style={"background-color":"white",
                         "box-shadow": "10px 20px 30px black",
                        # 'margin-left': '10px',
                        'width': '450px'
                         }, disabled=True)),
     ]),
               

html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
    #################################################################  MUNICIPIOS ranking    
          dbc.Row([
          dbc.Col(dbc.Button(([html.P("Ciudad de México",style={"font-size": 30,"color": "black","background-color": "white"}),
                        dbc.CardImg(src="https://github.com/fdealbam/feminicidios/blob/main/application/static/cdmx2.jpeg?raw=true",
                                        style={"background-color":"white"}),
                               html.P(
                           "Las 10 alcaldías con mayor número de casos de feminicidios son:"
                           " Iztapalapa (68), Gustavo A. Madero (37), Tlalpan (35), Cuauhtémoc"
                           "(34), Xochimilco (25), Miguel Hidalgo (19), Álvaro Obregón (17),"
                           " Tláhuac (16), Coyoacán (14), y Venustiano Carranza (14).",
                       style={'font-size': 14, "font-family":"Arial", "text-align":"justify" }),
                              ]),
                             style={"background-color":"white",
                                    "box-shadow": "10px 20px 30px black",
                                    'margin-left': '300px',
                                    'width': '450px'
                         }, disabled=True)),
          dbc.Col(dbc.Button(([html.H3("Jalisco",style={"font-size": 30,"color": "black","background-color": "white"}),
                       dbc.CardImg(src="https://github.com/fdealbam/feminicidios/blob/main/application/static/jal2.jpeg?raw=true",
                                        style={"background-color":"white"}),
                               html.P(
                           "Los 10 municipios con mayor número de casos de feminicidios son:"
                           " Guadalajara (51), Tlajomulco de Zúñiga (38), Zapopan (34), "
                           "El Salto (24), Tonalá (17), Puerto Vallarta (10), Ocotlán (6),"
                           " Tequila (6), Mezquitic (6), y Ixtlahuacán de los Membrillos (6)                     .",
                       style={'font-size': 14, "font-family":"Arial", "text-align":"justify" }),
               ]), style={"background-color":"white",
                         "box-shadow": "10px 20px 30px black",
                        # 'margin-left': '10px',
                        'width': '450px'
                         }, disabled=True)),
          ]),
  


#  
       html.Br(),
       html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
   
    
# Cintillo 3
     
       
#---------Grafica por entidad
     dbc.Row(
           [
               dbc.Col(html.H1([dbc.Badge("Comparativo", color="info", className="mr-1"),
                               " entre casos acumulados & tasas "]),
                       width={'size': 10,  "offset":1 }),
            ]),

    html.Br(),
    html.Br(),
    
    dbc.Row(
           [
               dbc.Col(html.H4("Total acumulado por entidad"),
                        width=2,lg={'size': 4,  "offset": 1, }),

               dbc.Col(html.H4("Tasa por entidad"),
                       width=1, lg={'size': 3,  "offset": 4, }),                     #size=12
               
            ], justify="end",),
   
    dbc.Row(
        [
            dbc.Col(dcc.Graph(figure=graf_totfem , config= "autosize", style={"margin-left":"50px"})),
                   #lg={'size': 5,  "offset": 0,}),
            
            dbc.Col(dcc.Graph(figure= graf_tasafem, config= "autosize")),
                   #lg={'size': 5,  "offset": 1,}),
        ], justify="end", no_gutters=True,),

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
        dbc.Col(html.H2([dbc.Alert("Perfil de Homicidios femeninos", color="primary",# className="alert-link",
                                  className="alert-heading"),
                        ]),width={'size': 12,  "offset":0 }),
    ]),
    dbc.Row(
    [
        dbc.Col(html.H6("Fuente: Datos de defunciones (2015-2019), Secretaría de Salud, DGIS, marzo 2021"),
                        width={'size': 6,  "offset":6 }),
     ], justify= "end"),
    
       html.Br(),
       html.Br(),




       dbc.Row([
        dbc.Col([dbc.Card(
            dbc.CardBody([
            html.H4("2015", className="card-title"),
            html.P((f'{int(def15_tot):,}'),style={"font-size":"60px","color":"gray",}),
            html.Hr(),
            html.H4("Mayor incidencia", className="card-title"),
            html.Hr(),
            html.Code("¿Dónde ocurren más?"),
            html.H6([ (ent115_txt),": ", (ent115_val),"%",]),
            html.H6([ (ent215_txt),": ", (ent215_val),"%",]),
            html.H6([ (ent315_txt),": ", (ent315_val),"%",]),
            html.H6([ (ent415_txt),": ", (ent415_val),"%",]),
            html.H6([ (ent515_txt),": ", (ent515_val),"%",]),                
            html.Code("Área urbana "),
            html.H6([ (aurb15_txt),": ", (aurb15_val),"%",]),
            html.Hr(),
            html.H4("Modus Operandi", className="card-title"),
            html.Hr(),
            html.Code("Parentesco con agresor", className="card-text"),
            html.H6([ (agr15_txt),": ", (agr15_val),"%",]),
            html.H6([ (agr215_txt),": ", (agr215_val),"%",]),
            html.H6([ (agr315_txt),": ", (agr315_val),"%",]),
            html.Code("¿Hubo violencia?", className="card-text"), 
            html.H6([ (viofm215_txt),": ", (viofm215_val),"%",]),          
            html.H6([ (viofm115_txt),": ", (viofm115_val),"%",]),
            html.Code("¿Dónde ocurrió? "),
            html.H6([ (lug115_txt),": ", (lug115_val),"%",]),
            html.H6([ (lug215_txt),": ", (lug215_val),"%",]),
            html.Hr(),
            html.H4("Perfil de la víctima ", className="card-title"), 
            html.Hr(),
            html.Code("Estado civil"),
            html.H6([ (civl115_txt),": ", (civl115_val),"%",]),
            html.H6([ (civl215_txt),": ", (civl215_val),"%",]),
            html.H6([ (civl315_txt),": ", (civl315_val),"%",]),
            html.H6([ (civl415_txt),": ", (civl415_val),"%",]),
            html.Code("¿Qué rangos de edad tenían?"),
            html.H6([ (eda115_txt),": ", (eda115_val),"%",]),
            html.H6([ (eda215_txt),": ", (eda215_val),"%",]),
            html.H6([ (eda315_txt),": ", (eda315_val),"%",]),
            html.H6([ (eda415_txt),": ", (eda415_val),"%",]),
            html.H6([ (eda515_txt),": ", (eda515_val),"%",]),
            html.Code("¿Estaba embarazada?"),
            html.H6([ (emba315_txt),": ", (emba315_val),"%",]), 
            html.H6([ (emba215_txt),": ", (emba215_val),"%",]), 
            html.H6([ (emba115_txt),": ", (emba115_val),"%",]), 
            html.Code("Escolaridad"),
            html.H6([ (esc115_txt),": ", (esc115_val),"%",]),
            html.H6([ (esc215_txt),": ", (esc215_val),"%",]),
            html.H6([ (esc315_txt),": ", (esc315_val),"%",]),
            
            #html.Code("Ocupación"),
            #html.H6([ (ocu115_txt),": ", (ocu115_val),"%",]),
            #html.H6([ (ocu215_txt),": ", (ocu215_val),"%",]),
            #html.H6([ (ocu315_txt),": ", (ocu315_val),"%",]),


          
        ]
    ),
    style={"width": "16rem"},
),]),
        dbc.Col([dbc.Card(
            dbc.CardBody([
             html.H4("2016", className="card-title"),
            html.P((f'{int(def16_tot):,}'),style={"font-size":"60px","color":"gray",}),
            html.Hr(),
            html.H4("Mayor incidencia", className="card-title"),
            html.Hr(),
            html.Code("¿Dónde ocurren más?"),
            html.H6([ (ent116_txt),": ", (ent116_val),"%",]),
            html.H6([ (ent216_txt),": ", (ent216_val),"%",]),
            html.H6([ (ent316_txt),": ", (ent316_val),"%",]),
            html.H6([ (ent416_txt),": ", (ent416_val),"%",]),
            html.H6([ (ent516_txt),": ", (ent516_val),"%",]),                
            html.Code("Área urbana "),
            html.H6([ (aurb16_txt),": ", (aurb16_val),"%",]),
            html.Hr(),
            html.H4("Modus Operandi", className="card-title"),
            html.Hr(),
            html.Code("Parentesco con agresor", className="card-text"),
            html.H6([ (agr16_txt),": ", (agr16_val),"%",]),
            html.H6([ (agr216_txt),": ", (agr216_val),"%",]),
            html.H6([ (agr316_txt),": ", (agr316_val),"%",]),
            html.Code("¿Hubo violencia?", className="card-text"), 
            html.H6([ (viofm216_txt),": ", (viofm216_val),"%",]),
            html.H6([ (viofm116_txt),": ", (viofm116_val),"%",]),                
            html.Code("¿Dónde ocurrió? "),
            html.H6([ (lug116_txt),": ", (lug116_val),"%",]),
            html.H6([ (lug216_txt),": ", (lug216_val),"%",]),
            html.Hr(),
            html.H4("Perfil de la víctima ", className="card-title"), 
            html.Hr(),
            html.Code("Estado civil"),
            html.H6([ (civl116_txt),": ", (civl116_val),"%",]),
            html.H6([ (civl216_txt),": ", (civl216_val),"%",]),
            html.H6([ (civl316_txt),": ", (civl316_val),"%",]),
            html.H6([ (civl416_txt),": ", (civl416_val),"%",]),
            html.Code("¿Qué rangos de edad tenían?"),
            html.H6([ (eda116_txt),": ", (eda116_val),"%",]),
            html.H6([ (eda216_txt),": ", (eda216_val),"%",]),
            html.H6([ (eda316_txt),": ", (eda316_val),"%",]),
            html.H6([ (eda416_txt),": ", (eda416_val),"%",]),
            html.H6([ (eda516_txt),": ", (eda516_val),"%",]),
            html.Code("¿Estaba embarazada?"),
            html.H6([ (emba316_txt),": ", (emba316_val),"%",]), 
            html.H6([ (emba216_txt),": ", (emba216_val),"%",]), 
            html.H6([ (emba116_txt),": ", (emba116_val),"%",]), 
            html.Code("Escolaridad"),
            html.H6([ (esc116_txt),": ", (esc116_val),"%",]),
            html.H6([ (esc216_txt),": ", (esc216_val),"%",]),
            html.H6([ (esc316_txt),": ", (esc316_val),"%",]),
            
            #html.Code("Ocupación"),
            #html.H6([ (ocu116_txt),": ", (ocu116_val),"%",]),
            #html.H6([ (ocu216_txt),": ", (ocu216_val),"%",]),
            #html.H6([ (ocu316_txt),": ", (ocu316_val),"%",]),

        ]
    ),
    style={"width": "16rem"},
),]),
         dbc.Col([dbc.Card(
            dbc.CardBody([
            
            html.H4("2017", className="card-title"),
            html.P((f'{int(def17_tot):,}'),style={"font-size":"60px","color":"gray",}),
            html.Hr(),
            html.H4("Mayor incidencia", className="card-title"),
            html.Hr(),
            html.Code("¿Dónde ocurren más?"),
            html.H6([ (ent117_txt),": ", (ent117_val),"%",]),
            html.H6([ (ent217_txt),": ", (ent217_val),"%",]),
            html.H6([ (ent317_txt),": ", (ent317_val),"%",]),
            html.H6([ (ent417_txt),": ", (ent417_val),"%",]),
            html.H6([ (ent517_txt),": ", (ent517_val),"%",]),                
            html.Code("Área urbana "),
            html.H6([ (aurb17_txt),": ", (aurb17_val),"%",]),
            html.Hr(),
            html.H4("Modus Operandi", className="card-title"),
            html.Hr(),
            html.Code("Parentesco con agresor", className="card-text"),
            html.H6([ (agr17_txt),": ", (agr17_val),"%",]),
            html.H6([ (agr217_txt),": ", (agr217_val),"%",]),
            html.H6([ (agr317_txt),": ", (agr317_val),"%",]),
            html.Code("¿Hubo violencia?", className="card-text"), 
            html.H6([ (viofm217_txt),": ", (viofm217_val),"%",]),
            html.H6([ (viofm117_txt),": ", (viofm117_val),"%",]),                
            html.Code("¿Dónde ocurrió? "),
            html.H6([ (lug117_txt),": ", (lug117_val),"%",]),
            html.H6([ (lug217_txt),": ", (lug217_val),"%",]),
            html.Hr(),
            html.H4("Perfil de la víctima ", className="card-title"), 
            html.Hr(),
            html.Code("Estado civil"),
            html.H6([ (civl117_txt),": ", (civl117_val),"%",]),
            html.H6([ (civl217_txt),": ", (civl217_val),"%",]),
            html.H6([ (civl317_txt),": ", (civl317_val),"%",]),
            html.H6([ (civl417_txt),": ", (civl417_val),"%",]),
            html.Code("¿Qué rangos de edad tenían?"),
            html.H6([ (eda117_txt),": ", (eda117_val),"%",]),
            html.H6([ (eda217_txt),": ", (eda217_val),"%",]),
            html.H6([ (eda317_txt),": ", (eda317_val),"%",]),
            html.H6([ (eda417_txt),": ", (eda417_val),"%",]),
            html.H6([ (eda517_txt),": ", (eda517_val),"%",]),
            html.Code("¿Estaba embarazada?"),
            html.H6([ (emba317_txt),": ", (emba317_val),"%",]), 
            html.H6([ (emba217_txt),": ", (emba217_val),"%",]), 
            html.H6([ (emba117_txt),": ", (emba117_val),"%",]),
            html.Code("Escolaridad"),
            html.H6([ (esc117_txt),": ", (esc117_val),"%",]),
            html.H6([ (esc217_txt),": ", (esc217_val),"%",]),
            html.H6([ (esc317_txt),": ", (esc317_val),"%",]),
            
            #html.Code("Ocupación"),
            #html.H6([ (ocu117_txt),": ", (ocu117_val),"%",]),
            #html.H6([ (ocu217_txt),": ", (ocu217_val),"%",]),
            #html.H6([ (ocu317_txt),": ", (ocu317_val),"%",]),
 
        ]
    ),
    style={"width": "16rem"},
),]),
         dbc.Col([dbc.Card(
            dbc.CardBody([
            html.H4("2018", className="card-title"),
            html.P((f'{int(def18_tot):,}'),style={"font-size":"60px","color":"gray",}),
            html.Hr(),
         
            html.H4("Mayor incidencia", className="card-title"),
            html.Hr(),
            html.Code("¿Dónde ocurren más?"),
            html.H6([ (ent118_txt),": ", (ent118_val),"%",]),
            html.H6([ (ent218_txt),": ", (ent218_val),"%",]),
            html.H6([ (ent318_txt),": ", (ent318_val),"%",]),
            html.H6([ (ent418_txt),": ", (ent418_val),"%",]),
            html.H6([ (ent518_txt),": ", (ent518_val),"%",]),
            html.Code("Área urbana "),
            html.H6([ (aurb18_txt),": ", (aurb18_val),"%",]),
            html.Hr(),
            html.H4("Modus Operandi", className="card-title"),
            html.Hr(),
            html.Code("Parentesco con agresor", className="card-text"),
            html.H6([ (agr18_txt),": ", (agr18_val),"%",]),
            html.H6([ (agr218_txt),": ", (agr218_val),"%",]),
            html.H6([ (agr318_txt),": ", (agr318_val),"%",]),
            html.Code("¿Hubo violencia?", className="card-text"), 
            html.H6([ (viofm218_txt),": ", (viofm218_val),"%",]),
            html.H6([ (viofm118_txt),": ", (viofm118_val),"%",]),
            html.Code("¿Dónde ocurrió? "),
            html.H6([ (lug118_txt),": ", (lug118_val),"%",]),
            html.H6([ (lug218_txt),": ", (lug218_val),"%",]),
            html.Hr(),
            html.H4("Perfil de la víctima ", className="card-title"), 
            html.Hr(),
            html.Code("Estado civil"),
            html.H6([ (civl118_txt),": ", (civl118_val),"%",]),
            html.H6([ (civl218_txt),": ", (civl218_val),"%",]),
            html.H6([ (civl318_txt),": ", (civl318_val),"%",]),
            html.H6([ (civl418_txt),": ", (civl418_val),"%",]),
            html.Code("¿Qué rangos de edad tenían?"),
            html.H6([ (eda118_txt),": ", (eda118_val),"%",]),
            html.H6([ (eda218_txt),": ", (eda218_val),"%",]),
            html.H6([ (eda318_txt),": ", (eda318_val),"%",]),
            html.H6([ (eda418_txt),": ", (eda418_val),"%",]),
            html.H6([ (eda518_txt),": ", (eda518_val),"%",]),
            html.Code("¿Estaba embarazada?"),
            html.H6([ (emba318_txt),": ", (emba318_val),"%",]), 
            html.H6([ (emba218_txt),": ", (emba218_val),"%",]), 
            html.H6([ (emba118_txt),": ", (emba118_val),"%",]), 
            html.Code("Escolaridad"),
            html.H6([ (esc118_txt),": ", (esc118_val),"%",]),
            html.H6([ (esc218_txt),": ", (esc218_val),"%",]),
            html.H6([ (esc318_txt),": ", (esc318_val),"%",]),
              
            #html.Code("Ocupación"),
            #html.H6([ (ocu118_txt),": ", (ocu118_val),"%",]),
            #html.H6([ (ocu218_txt),": ", (ocu218_val),"%",]),
            #html.H6([ (ocu318_txt),": ", (ocu318_val),"%",]),
                        ]
    ),
    style={"width": "16rem"},
),]),
         dbc.Col([dbc.Card(
            dbc.CardBody([
             html.H4("2019", className="card-title"),
            html.P((f'{int(def19_tot):,}'),style={"font-size":"60px","color":"gray",}),
            html.Hr(),
           
            html.H4("Mayor incidencia", className="card-title"),
            html.Hr(),
            html.Code("¿Dónde ocurren más?"),
            html.H6([ (ent119_txt),": ", (ent119_val),"%",]),
            html.H6([ (ent219_txt),": ", (ent219_val),"%",]),
            html.H6([ (ent319_txt),": ", (ent319_val),"%",]),
            html.H6([ (ent419_txt),": ", (ent419_val),"%",]),
            html.H6([ (ent519_txt),": ", (ent519_val),"%",]),                
            html.Code("Área urbana "),
            html.H6([ (aurb19_txt),": ", (aurb19_val),"%",]),
            html.Hr(),
            html.H4("Modus Operandi", className="card-title"),
            html.Hr(),
            html.Code("Parentesco con agresor", className="card-text"),
            html.H6([ (agr19_txt),": ", (agr19_val),"%",]),
            html.H6([ (agr219_txt),": ", (agr219_val),"%",]),
            html.H6([ (agr319_txt),": ", (agr319_val),"%",]),
            html.Code("¿Hubo violencia?", className="card-text"), 
            html.H6([ (viofm219_txt),": ", (viofm219_val),"%",]),
            html.H6([ (viofm119_txt),": ", (viofm119_val),"%",]),                
            html.Code("¿Dónde ocurrió? "),
            html.H6([ (lug119_txt),": ", (lug119_val),"%",]),
            html.H6([ (lug219_txt),": ", (lug219_val),"%",]),
            html.Hr(),
            html.H4("Perfil de la víctima ", className="card-title"), 
            html.Hr(),
            html.Code("Estado civil"),
            html.H6([ (civl119_txt),": ", (civl119_val),"%",]),
            html.H6([ (civl219_txt),": ", (civl219_val),"%",]),
            html.H6([ (civl319_txt),": ", (civl319_val),"%",]),
            html.H6([ (civl419_txt),": ", (civl419_val),"%",]),
            html.Code("¿Qué rangos de edad tenían?"),
            html.H6([ (eda119_txt),": ", (eda119_val),"%",]),
            html.H6([ (eda219_txt),": ", (eda219_val),"%",]),
            html.H6([ (eda319_txt),": ", (eda319_val),"%",]),
            html.H6([ (eda419_txt),": ", (eda419_val),"%",]),
            html.H6([ (eda519_txt),": ", (eda519_val),"%",]),
            html.Code("¿Estaba embarazada?"),
            html.H6([ (emba319_txt),": ", (emba319_val),"%",]), 
            html.H6([ (emba219_txt),": ", (emba219_val),"%",]), 
            html.H6([ (emba119_txt),": ", (emba119_val),"%",]), 
            html.Code("Escolaridad"),
            html.H6([ (esc119_txt),": ", (esc119_val),"%",]),
            html.H6([ (esc219_txt),": ", (esc219_val),"%",]),
            html.H6([ (esc319_txt),": ", (esc319_val),"%",]),
            #html.Code("Ocupación"),
            #html.H6([ (ocu119_txt),": ", (ocu119_val),"%",]),
            #html.H6([ (ocu219_txt),": ", (ocu219_val),"%",]),
            #html.H6([ (ocu319_txt),": ", (ocu319_val),"%",]),
 
                        ]
    ),
    style={"width": "16rem"},
),]),], style={"margin-left": "10px"}),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),

# nuevo
    
    dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.H4("Consideraciones generales "),
                html.P(
                    "Los feminicidios son un problema aún irresuelto y son tema central de la " 
                    "agenda de seguridad nacional. Su gravedad se observa "
                    "en los registros anuales y registros mensuales, que se presentan al "
                    "inicio de esta visualización. Además, completamos este análisis con "
                    "un perfil de homicidios femeninos según año."
                    "Existe cada vez mayor atención institucional al fenómeno y fuerte preocupación de la sociedad, " 
                    "esto último se evidencia en el hecho que todos seamos más vigilantes al respecto. "
                    "No obstante, aún hace falta más acción social, sobretodo, más intervención institucional "
                    "para diseñar estrategias efectivas de prevención y promover su denuncia. Es imperante "
                    "acabar con esta violencia de género. "
                    "El presente dashboard (tablero de datos) es un ejercicio institucional con el objeto de "
                    "informar a la sociedad. La información proviene, primero, del Secretariado Ejecutivo Nacional del Sistema Nacional de "
                    "Seguridad Pública (SENSNSP) (2015-2021); segundo, de la Secretaría de Salud y su base de datos sobre defunciones anuales (2015-2019). "
                    "Ademas, esta dashboard seguramente puede ser completado con otras fuentes de información "
                    "gubernamental y por toda aquella información proveniente de organizaciones civiles que " 
                    "dan seguimiento al tema. En ningún caso, este contenido representa algún "
                    "posicionamiento partidista, personal o institucional, mucho menos opinión o postura alguna "
                    "sobre el fenómeno. ",
                    className="lead"),
                html.Br(),
                html.H5("Metodología "),
                html.P(
                    "Esta información fue tratada con el lenguaje de programación Python y varias de las librerías "
                    "más comunes (Dash, Choropleth, Pandas, Numpy, Geopandas, etc.), que nos ayudan a automatizar "
                    "la recurrencia (request) a la fuente de información y las operaciones necesarias para creargraficas "
                    "interactivas y mapas presentados. El volumen de información fue de 230 megabytes de la base de datos "
                    "del SENSNSP y 2.4 gigabytes de la base de datos de defunciones, provista por la Secretaría de Salud, "
                    "Dirección General de Información de Salud. ",
                    className="lead"),
                    
            ], fluid=True,
        )
    ], style= {"margin-left":"50px"},
    fluid=True,
    ),    
    
        
    
       
       
       html.Br(),
       html.Br(),
   html.Br(),
    
   dbc.Row([
                                    #https://github.com/fdealbam/CamaraDiputados/blob/b11ef31e8e0f73e1a4a06ce60402563e1bd0122e/application/static/logocamara.jfif
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/ce2cda9ccf7732861b8494b36562ebe9c8c642a6/application/static/logo%20cesopycamara.jpeg?raw=true"),
                        width=5, md={'size': 2,  "offset": 1, }),
            
           dbc.Col(html.H6(" Centro de Estudios Sociales y de Opinión Pública," 
                           " Cámara de Diputados"
                           " México, 2021 "),
                  width={'size': 3, 'offset': 0}),
               ], justify="start",),
            
     dbc.Row([    
           dbc.Col(html.P([dbc.Badge("Equipo responsable", style={"font-size":20},
                          href="https://innovation-learning.herokuapp.com/",
                                     )]),
                  width={'size': 3,  "offset": 3}),
                       ], justify="start",),
   
    html.Br(),
    html.Br(),
    html.Br(),

    

    
    html.Br(),
                  
                  
                  ])


app.layout = html.Div([body],
                              style={'width': '1800px'})

                     
                     

#from application.dash import app
#from settings import config

if __name__ == "__main__":
    app.run_server()
    
