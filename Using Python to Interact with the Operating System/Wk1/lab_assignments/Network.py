#!/usr/bin/env Python3

import requests
import socket

localhost = socket.gethostbyname('localhost')
requests = requests.get("http://www.google.com")

def check_localhost():
    if localhost == '127.0.0.1':
        return True

def check_connectivity():
    if requests.status_codes == 200:
        return True
        
