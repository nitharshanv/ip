import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

 
    
def printdetails(ip):
    res=DbIpCity.get(ip,api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
    #locate(ip)
    return res.city,res.region,res.country,str(res.latitude),str(res.longitude)

