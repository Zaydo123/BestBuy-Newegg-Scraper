from colorama import Fore
import requests
from bs4 import BeautifulSoup
from twilio import rest

#global variables
phonenumbers = ['+16302473767']


#funcs
def twilio(number, MessageBODY):
  #twilio messaging
  account_sid = 'AC07f855462959468deb84c800f18fd36f'
  auth_token = 'cdb79ec2a3e8cee9205e39e25a525a0b'
  client = Client(account_sid, auth_token)

  message = client.messages.create(
                                body=MessageBODY,
                                from_='+16505294223',
                                to=number
                            )

  print(message.sid)

#bestbuy
def bestbuy():
    bbylinks = ['https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324']
    soup = BeautifulSoup(bbylinks[0].text, 'html.parser')
    requestBby = requests.get(bbylinks[0])
    try:
        inStockBBY = soup.find('button',{'class' : 'btn btn-disabled btn-lg btn-block add-to-cart-button'})
        print(inStockBBY)
    except:
        print('nope')
        return




bestbuy()