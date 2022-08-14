from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import time
os.system('cls')

url="https://etestbank.net/shop/"
result=requests.get(url).text
result=BeautifulSoup(result,'html.parser')
pages=result.find('ul', class_="page-numbers")
last_page=int(pages.find_all('a', class_="page-numbers")[-2:-1][0].text)

product_row=result.find('div', class_="products products-grid")
items=product_row.find_all('div', class_="product-block grid")

names=[]
prices=[]
links=[]
for  num in range(1,last_page+1):
    print(num)
    try:
        time.sleep(5)
        url=f"https://etestbank.net/shop/page/{num}/"
        result=requests.get(url).text
        result=BeautifulSoup(result,'html.parser')
        product_row=result.find('div', class_="products products-grid")
        items=product_row.find_all('div', class_="product-block grid")
        for item in items:
            h3_tag=item.find('h3', class_="name").a
            link =h3_tag['href']
            name=h3_tag.text
            price=item.find('span', class_="woocommerce-Price-amount amount").text
            names.append(name)
            prices.append(price)
            links.append(link)
        print('done')
    except:
        print(f"page {num}  not done")

scrap={"Name":names,'Price':prices,"Link":links}

df = pd.DataFrame(scrap)
df.to_excel(f"resullt.xlsx")

print("completed data scraping check now")
