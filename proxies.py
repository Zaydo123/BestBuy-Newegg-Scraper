import random
global listOfProxies
proxiesDict = {}
listOfProxies = []
def formatProxy():
    with open('proxies.txt','r') as f:
        readall = f.readlines()
    for i in readall:
        i=i.replace('	',':')
        i=i.replace('\n','')
        listOfProxies.append(i)

def newproxy():
    proxiesDict['https'] = random.choice(listOfProxies)
    return proxiesDict

