import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

def cal(ip1,ip2):
       res1=DbIpCity.get(ip1) 
       res2=DbIpCity.get(ip2) 
       lat1,long1=res1.latitude,res1.longitude
       lat2,lon2=res2.latitude,res2.longitude
       x="https://www.google.com/maps/dir/?api=1&origin="+str(lat1)+","+str(long1)+"&destination="+str(lat2)+","+str(lon2)
       webbrowser.open(x)
       
       return distance((lat1,long1),(lat2,lon2)).km
   
def locate(ip):
    res=DbIpCity.get(ip,api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
    
    x="https://www.google.com/maps/@"+str(res.latitude)+","+str(res.longitude)+",12z"
    print(x)
    webbrowser.open(x)
    options=Options()
    options.headless=True
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    driver=webdriver.Chrome(options=options)
    driver.get(x)
    driver.save_screenshot("location.png")
    driver.quit()
print("hi")
y=True  
while y==True:
     
    print("ip\nurl\ndistance between two ips") 
    x=input("what you got   :   ")

    if(x=="ip"):
        
        ip_add = input("Enter IP: ")  # 198.35.26.96
        #print(type(ip_add))
       
        locate(ip_add)
        img = Image.open("location.png")
        img.show()
        

    elif x=="url":
        url = input("Enter URL: ")  # www.youtube.com
        ip_add = socket.gethostbyname(url)
       
        locate(ip_add)
        img = Image.open("location.png")
        img.show()

    elif x=="distance between two ips":
        ip1=input("ip1 :")
        ip2=input("ip2 :")
        distance=cal(str(ip1),str(ip2))
        print(distance)
    elif x=="exit":
        y=False
    
    
    
