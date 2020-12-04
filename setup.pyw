import os.path
from os import path

if path.exists('discord_webhook_links.txt') != True:
    f = open('discord_webhook_links.txt','x')
    f.close()

if path.exists('proxies.txt') != True:
    f = open('proxies.txt','x')
    f.close()
        

if path.exists('phonenumber.txt') != True:
    f = open('phonenumber.txt','x')
    f.close()    

if path.exists('urls.txt') != True:
    f = open('urls.txt','x')
    f.close()

if path.exists('twilio.txt') != True:
    f = open('twilio.txt','x')
    f.close()
