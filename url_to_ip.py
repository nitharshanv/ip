import socket
import requests

def utoi(url):
    ip= socket.gethostbyname(url)
    return ip