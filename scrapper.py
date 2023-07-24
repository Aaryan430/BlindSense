
# import module 
import requests 
import pandas as pd 
from bs4 import BeautifulSoup 
import json
  
# link for extract html data 
def getdata(url): 
    r = requests.get(url) 
    return r.text 

def getproduct(barcode :str):
    htmldata = getdata("https://www.google.com/search?q="+barcode) 
    soup = BeautifulSoup(htmldata, 'html.parser') 
    product_name = '' 
    product_price = ''
    product = []
    product_num = 0
    for data in soup.find_all("h3"): 
        product_name = data.get_text()
        paren = data.parent
        i = 0
        while i <= 4:
            paren = paren.parent
            i+=1
        for price in paren.div.find_all("span"):
            product_price = price.get_text()
            if product_price.find('$')==0 and product != '' and product !=' ':
                product.append(product_price)
            if product_price.find('₹')==0 and product != '' and product !=' ':
                break

        if product_price.find('₹') == 0:
            break
    return {"product_name" : product_name, "product_price" : product_price}


# getproduct(str(9780141346847))
