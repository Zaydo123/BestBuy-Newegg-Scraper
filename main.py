import time,random,proxies,threading,requests
from colorama import Fore, Back,init
from bs4 import BeautifulSoup
from twilio.rest import Client
from threading import Lock
from discord_webhook import DiscordWebhook
from BrowserAgents import possibleBrowserAgents
from os import system

s_print_lock = Lock()
init(convert=True)
system(f"title BestBuy Scraper - Zayd#1234 = Active Threads: {threading.activeCount()}")
neweggLinks = []
bbylinks = []
webhook_urls = []
#read configs
#discord

with open('phonenumber.txt','r') as f:
    phonenumber = f.readlines(0)
    if phonenumber == []:
        phoneYN = False
        print('SMS Disabled')
    else:
        phoneYN = True
        plus = '+'
        phonenumbers = plus + phonenumber[0]
        print("SMS Enabled")
if phoneYN == True:
    with open('twilio.txt','r') as f:
        info = f.read()
        if info == []:
            phoneYN = False
            print("SMS Disabled")
        else:
            info = info.split('\n')
            accountSID = info[0]
            authToken = info[1]
            Pnumber = info[2]

with open('discord_webhook_links.txt','r') as discordVar:
    tempList = []
    try:
        discordList = discordVar.readlines()
        for _ in discordList:
            try:
                tempitem = _.strip('\n')
                tempList.append(tempitem)
            except:
                pass
        discordList = tempList
        if len(discordList) == 0:
            webhooksQuestion = False 
            print("Discord Disabled")
        else:
            for _ in discordList:
                webhook_urls.append(_)
            webhooksQuestion = True
            print('Discord Enabled') 
    except:
        print("Discord Disabled")
        webhooksQuestion = False
#links
with open ('urls.txt','r') as f:
    allURLs = f.read().split('\n')
    for _ in allURLs:
        neweggLinksSearch = _.find('newegg.com')
        if neweggLinksSearch == -1:
            bbylinks.append(_)
        else:
            neweggLinks.append(_)             
def discord(name, url, price):
    webhook = DiscordWebhook(url=webhook_urls, content=f'PRODUCT: {name}\nPrice:{price}\n{url}')
    response = webhook.execute()
    return

#twilio
def twilio(number, MessageBODY):
  #twilio messaging
    account_sid = accountSID
    auth_token = authToken
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                  body=MessageBODY,
                                  from_=Pnumber,
                                  to=number
                              )

#bestbuy
class Counter():
    def __init__(self):
        self.count = 0
    def plusOne(self):
        self.count +=1
        system(f"title BestBuy Scraper : Threads = {threading.activeCount()} : Sent = {self.count} : BestBuy = {len(bbylinks)} : Newegg = {len(neweggLinks)}")

a = Counter()
def bestbuy(proxiesDict,productLink,productName):
    while True:
        time.sleep(5)
        browserAgent = possibleBrowserAgents[random.randrange(len(possibleBrowserAgents))]
        bbylinks = productLink
        headers = {'User-Agent': browserAgent}

        try:
            requestBby = requests.get(bbylinks,headers=headers,proxies=proxiesDict,timeout=15)
            soup = BeautifulSoup(requestBby.text, 'html.parser') 

        except (requests.exceptions.ConnectionError) as err:
            print(f'[R]{err}')
            print('fail, new proxy')
            proxiesDict = proxies.newproxy()
            print(proxiesDict)
            return
        except Exception as e:
            try:
                print(str(e))
                browserAgent = possibleBrowserAgents[random.randrange(len(possibleBrowserAgents))]
                proxiesDict = proxies.newproxy()
                print("New browser agent and proxy")
                print(proxiesDict)
            except:
                return
        try:
            prodName = soup.find('div',{'class':'sku-title','itemprop':"name"}).text
            inStockBBY = soup.find('div',{'class':'fulfillment-add-to-cart-button'}).text
            priceProd = soup.find('div',{'class':'priceView-hero-price priceView-customer-price'}).text.split('Your')[0]
            if inStockBBY == "Check Stores" or 'Coming Soon' or 'Sold Out':
                #with s_print_lock:
                    #print('[B]',Fore.RED,inStockBBY,Fore.BLUE,prodName, Fore.WHITE, priceProd, Fore.RESET)
                a.plusOne()
            if inStockBBY == 'Add to Cart':
                #print(inStockBBY)
                inStockConfirmed = True
                print('[B]',Fore.BLUE,inStockBBY,Fore.GREEN,prodName,Fore.WHITE, priceProd, Fore.RESET)
                if webhooksQuestion == True:
                    discord(prodName,bbylinks,priceProd)
                if phoneYN == True:
                    twilio(phonenumbers,f'{productName} IS IN STOCK :: URL = {bbylinks}')
                time.sleep(600)
        except Exception as e:
            print(str(e))
            with s_print_lock:
                print(Back.RED,'Error',Back.RESET)

def newegg(proxiesDict,productLink,productName):
    currentThread = threading.currentThread()
    proxiesEgg = proxiesDict
    while True:
        time.sleep(5)
        try:
            neweggLinks = productLink
            browserAgent = possibleBrowserAgents[random.randrange(len(possibleBrowserAgents))]
            headers = {'User-Agent': browserAgent}
            requestNewegg = requests.get(neweggLinks,headers=headers,proxies=proxiesEgg,timeout=15)
            eggSoup = BeautifulSoup(requestNewegg.text, 'html.parser') 
        except (requests.exceptions.ConnectionError) as err:
            print(err)
            print('fail, new proxy')
            proxiesEgg = proxies.newproxy()
            print(proxiesEgg)
            return
        except:
            browserAgent = possibleBrowserAgents[random.randrange(len(possibleBrowserAgents))]
            proxiesEgg = proxies.newproxy()
            print("New browser agent and proxy")
        try:
            NeweggName = eggSoup.find('h1',{'class' : 'product-title'}).text
            NeweggPrice = eggSoup.find('span',{'class':'price'}).text
            NeweggPrice = '$'+ NeweggPrice
            try:
                NeweggStock = eggSoup.find('span',{'class':'btn btn-message btn-wide'})
                if NeweggStock == None:
                    NeweggStock = eggSoup.find('div',{'class':'flags-body has-icon-left fa-exclamation-triangle'})
                if NeweggStock == None:
                    NeweggStock = eggSoup.find('button',{'class':'btn btn-primary btn-wide'}) 
                NeweggStock = NeweggStock.text
            except Exception as e:
                with s_print_lock:
                    print('Error')          
            #with s_print_lock:
                #print('[N]',Fore.GREEN,NeweggStock,Fore.GREEN,NeweggName,Fore.WHITE, NeweggPrice, Fore.RESET)
            a.plusOne()
            if NeweggStock == 'Add to cart ':
                #print(Back.RED,'[N]',Fore.BLUE,NeweggStock,Fore.GREEN,NeweggName,Fore.WHITE,NeweggPrice,Fore.RESET,Back.RESET)
                if webhooksQuestion == True:
                    discord(NeweggName,neweggLinks,NeweggPrice)
                if phoneYN == True:
                    twilio(phonenumbers,f'{NeweggName} IS IN STOCK :: URL = {neweggLinks}')
                time.sleep(600)
                print('slept')               
        except Exception as e:
            print(e)
            try:
                if NeweggStock == "Sold Out" or "CURRENTLY SOLD OUT":
                    #print('[N]',Fore.BLUE,NeweggStock,Fore.GREEN,NeweggName,Fore.WHITE, NeweggPrice, Fore.RESET)
                    return
                else:
                    #print('[N]',Back.RED,NeweggStock,NeweggName,NeweggPrice,Back.RESET)
                    if webhooksQuestion == True:
                        discord(NeweggName,neweggLinks,NeweggPrice)
                    if phoneYN == True:
                        twilio(phonenumbers,f'{NeweggName} IS IN STOCK :: URL = {neweggLinks}')
                

                    time.sleep(600)
                    print('slept')
            except:
                with s_print_lock:
                    print(Back.WHITE,Fore.BLACK,'Error',Fore.RESET,Back.RESET)             

proxies.formatProxy()
proxies.newproxy()
proxiesDict = proxies.proxiesDict
print(proxiesDict)

def threadingMulti(name,link,productName):
    with s_print_lock:
        print('Thread',name, 'is starting')
    x = threading.Thread(target=bestbuy, args=(proxiesDict,link,productName))
    system(f"title BestBuy Scraper / Threads = {threading.activeCount()} / Sent = 0 / BestBuy = {len(bbylinks)} / Newegg = {len(neweggLinks)}")
    x.start()

def threadingNewegg(name,link,productName):
    with s_print_lock:
        print('Thread',name, 'is starting')
    x1 = threading.Thread(target=newegg, args=(proxiesDict,link,productName))
    system(f"title BestBuy Scraper / Threads = {threading.activeCount()} / Sent = 0 / BestBuy = {len(bbylinks)} / Newegg = {len(neweggLinks)}")
    x1.start()

def bby():
    for _ in bbylinks:
        indexLinks = bbylinks.index(_)
        threadingMulti(f'B{indexLinks}',bbylinks[indexLinks],'ONE OR MORE ITEMS')

def newG():
    for _ in neweggLinks:
        indexNewegg = neweggLinks.index(_)
        threadingNewegg(f'N{indexNewegg}',neweggLinks[indexNewegg],'ONE OR MORE ITEMS')

if len(bbylinks) >= 1:
    bby()
if len(neweggLinks) >= 1:
    newG()

