import random
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

