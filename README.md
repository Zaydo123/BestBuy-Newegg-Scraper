# BestBuy / Newegg Scraper
Please run setup.pyw, then fill in the files according to these directions. Leave ```phonenumber.txt``` blank if you don't want to be texted or leave ```discord_web_hook_links.txt``` if you don't want to connect it with discord. For now, those are the only two contact methods. This bot does not buy anything, rather notifies you when something you choose goes in stock. Not all BestBuy links or Newegg links/products will work, but most of the links like the XBOX and the GPU's work for the most part. This is because not all product pages are the same, srry.

# First
STAR THIS MF PROJECT I PUT LIKE 24 HOURS IN LIKE 4 DAYS TO THIS SHIT
```pip install -r requirements.txt```
and then run ```setup.pyw```
# Proxy File
All proxies should be formatted either like this:
```
5.61.58.211:4329
```
Or like this:
```
5.61.58.211 4329
```

# Twilio File
the twilio.txt file that is created should have account sid on first line, auth token on second line of text file, and your twilio number. Like this:
```
AVOJKeojgme02948588598698eae
egrf9388hfuh32fu3gfbu3QNhuwd
+12345678901
```
# URLs FIle
paste in your links to the document, separating each one with a new line:
```
https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3060-ti-eagle-oc-8g-gddr6-pci-express-4-0-graphics-card-black/6442485.p?skuId=6442485
https://www.newegg.com/p/N82E16868105273
```
like that.
# Phonenumbers File
just paste in your phone number, include the country code:
```
12453567896
```
note this code only supports one text message target, someone please finish the rest of this shit for me.

# Webhook file
prettymuch the same as the other files, same format:
```
https://discord.com/api/webhooks/782996534558094116/4ofii4mWbNOgYTgnSul10cOyXEXP4-cEoKypBLXZH17LUxE-AzUDrL2RWkwqoCD9DqD4
```
Once you have all this sorted, you should be able to run main.py. It won't print anything besides some error notifications and notifications about thread creation. If you know how to use asyncio or something, please help me out with this shit, because I can't print without segmentation faults, but I don't want to use locks because then my time.sleep at the end in order to prevent spam wont work. THANKS.
