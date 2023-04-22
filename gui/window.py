import PySimpleGUI as sg    
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import a
from PIL import Image
import io
import url_to_ip
import geocoder

tab1_layout =  [[sg.T('ip')]
                ,[sg.In(key='ip')]]    

tab2_layout = [[sg.T('enter the url')],    
               [sg.In(key='url')]]   

layout = [[sg.TabGroup([[sg.Tab('ip Tab ', tab1_layout, tooltip='tip'), sg.Tab('url Tab ', tab2_layout)]], tooltip='TIP2')],    
          [sg.Output(size=(50,10), key='-OUTPUT-')],
          [sg.Button('Read')],[sg.Button('google map')]]    

window = sg.Window('ip', layout, default_element_size=(12,1))    
x=""

while True:    
    event, values = window.read()    
    print(values) 
    
    if(values['ip']!=''):
          
        x=values['ip']
        ip=x
        city,region,country,lat,longi=a.printdetails(ip)
        x="https://www.google.com/maps/@"+lat+","+longi+",12z"
        window['-OUTPUT-'].update("region :"+region
                                  +'\n'+"city :"+city
                                  +'\n'+"country :"+country
                                  +'\n'+"(latitude,longitude) :"+"("+lat+","+longi+")"+"\n"+"google map link   :"+"\n"+x)
        values['ip']=''                  
        
    if(values['url']!=''):
        x=values['url']
        ip=url_to_ip.utoi(x)
        #ip= socket.gethostbyname(x)
        city,region,country,lat,longi=a.printdetails(ip)
        x="https://www.google.com/maps/@"+lat+","+longi+",12z"
        window['-OUTPUT-'].update("region :"+region
                                  +'\n'+"city :"+city
                                  +'\n'+"country :"+country
                                  +'\n'+"(latitude,longitude) :"+"("+lat+","+longi+")"+"\n"+"google map link"+x)
        values['url']=''
          
    if(event=='google map'):   
        webbrowser.open(x)
        
    
          
        
        
    if event == sg.WIN_CLOSED:    # always,  always give a way out!    
        loop=1
        break  
        
        
    
        
