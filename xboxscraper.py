from colorama import Fore
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
import random
import proxies

#global variables
def initialize():
    global phonenumbers
    phonenumbers = '+16302473767'

#funcs
def twilio(number, MessageBODY):
  #twilio messaging
  account_sid = 'ACc99025e313cc1b5184aafcfdf798e6ae'
  auth_token = 'd02878352724f9f9d7a228d70e3bf322'
  client = Client(account_sid, auth_token)

  message = client.messages.create(
                                body=MessageBODY,
                                from_='+16124318220',
                                to=number
                            )


#bestbuy
def bestbuy(proxiesDict):
    bbylinks = 'https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    
    try:
        requestBby = requests.get(bbylinks,headers=headers,proxies=proxiesDict)
    except:
        print('fail, new proxy')
        proxies.newproxy()
        print
        return
    soup = BeautifulSoup(requestBby.text, 'html.parser') 
    try:
        inStockBBY = soup.find('div',{'class':'fulfillment-add-to-cart-button'}).text
        if inStockBBY == 'Sold Out':
            print(Fore.RED,'SOLD OUT',Fore.RESET)
            #print(inStockBBY)
        else:
            print(Fore.BLUE,"IN STOCK",Fore.RESET)
            for _ in phonenumbers:
                print(_)
                twilio(phonenumbers,f'XBOX SERIES X IS IN STOCK :: URL = {bbylinks}')
            return
    except:
        pass



initialize()
proxies.formatProxy()
proxies.newproxy()
proxiesDict = proxies.proxiesDict
print(proxiesDict)
while True:
    bestbuy(proxiesDict)
    print(Fore.MAGENTA,'_________')
    
