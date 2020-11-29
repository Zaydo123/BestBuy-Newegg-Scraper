from colorama import Fore
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
import random
import proxies

#global variables
def initialize(phonenuminput):
    global phonenumbers
    global CodeError
    phonenumbers = str('+'+ phonenuminput)
    CodeError = 0

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

possibleBrowserAgents = ['Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550)',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]'
]

#bestbuy
def bestbuy(proxiesDict):
    browserAgent = possibleBrowserAgents[random.randrange(len(possibleBrowserAgents))]
    bbylinks = 'https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324'
    headers = {'User-Agent': browserAgent}
    
    try:
        requestBby = requests.get(bbylinks,headers=headers,proxies=proxiesDict,timeout=20)
        CodeError = 200
        soup = BeautifulSoup(requestBby.text, 'html.parser') 
    except (requests.exceptions.ConnectionError) as err:
        print(err)
        print('fail, new proxy')
        proxiesDict = proxies.newproxy()
        print(proxiesDict)
        CodeError = 404
        return
    except:
        browserAgent = possibleBrowserAgents[random.randrange(len(possibleBrowserAgents))]
        proxiesDict = proxies.newproxy()
    
    try:
        inStockBBY = soup.find('div',{'class':'fulfillment-add-to-cart-button'}).text
        if inStockBBY == 'Sold Out':
            print(Fore.RED,'SOLD OUT',Fore.RESET)
            #print(inStockBBY)
        else:
            print(Fore.BLUE,"IN STOCK",Fore.RESET)
            twilio(phonenumbers,f'XBOX SERIES X IS IN STOCK :: URL = {bbylinks}')
    except:
        pass

        



initialize(input('phone number:'))
proxies.formatProxy()
proxies.newproxy()
proxiesDict = proxies.proxiesDict
print(proxiesDict)
while True:
    bestbuy(proxiesDict)
    print(Fore.MAGENTA,'_________')
    time.sleep(10)
    
