import random

'''
If you're reading this code and you want to change what proxy type you're using, let me help you.

Try to locate a bit of code that looks like this:
proxiesDict['socks5'] = random.choice(listOfProxies)
             ^^^^^^
I underlined the part you're able to change. Your two main options to change it to are https or socks4.
There are other options, although, they're not really preferred.

ALSO I'VE MADE PROXIES MANDATORY BECAUSE I'M TOO LAZY AND FOR YOUR OWN SAFTEY
if you need some good, free proxies, go to https://rsocks.net // They have some, but u need to refresh your list every so often and renew your list.

'''

global listOfProxies
proxiesDict = {}
listOfProxies = []
def formatProxy():
    with open('proxies.txt','r') as f:
        readall = f.readlines()
    for i in readall:
        try:
            i=i.replace('	',':')
            i=i.replace('\n','')
            listOfProxies.append(i)
        except:
            pass
def newproxy():
    proxiesDict['socks5'] = random.choice(listOfProxies)
    return proxiesDict

