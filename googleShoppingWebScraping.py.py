import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import date
import os
import csv





def googleShoppingSearch(product_to_search):

    url =    f'https://www.google.com/search?tbm=shop&hl=it&psb=1&ved=2ahUKEwiy55Sqg5f8AhVRHAYAHZ4nDXMQu-kFegQIABAK&q={product_to_search}&oq={product_to_search}&gs_lcp=Cgtwcm9kdWN0cy1jYxADUABYAGAAaABwAHgAgAEAiAEAkgEAmAEA&sclient=products-cc'
    browser =webdriver.Chrome()
    browser.get(url)
    time.sleep(2)
# accept the cookies
    browser.find_element(By.XPATH ,'//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/div[1]/div[1]/form[2]/div/div/button').click()
# Get the list of all the Google Shopping research    
    results= browser.find_elements(By.CLASS_NAME,'sh-dgr__content')

# create the list containing the final results
    product_descprition_list=[]
    product_price_list=[]
    product_seller_list=[]
    shippment_conditions_list=[]
    product_img_url_list=[]
    product_searched_list=[]
    search_date_list=[]
    product_seller_url_list=[]

# get the necessary information from each result
    for items in results:
        product_descprition= items.find_element(By.CLASS_NAME,'C7Lkve').find_element(By.CLASS_NAME,'EI11Pd').find_element(By.CLASS_NAME,'tAxDx').get_attribute('innerHTML')
        product_price = items.find_element(By.CLASS_NAME,'XrAfOe').find_element(By.CLASS_NAME,'kHxwFf').find_element(By.CLASS_NAME,'QIrs8').find_element(By.TAG_NAME,'span').get_attribute('innerHTML')
        product_price=product_price.replace('&nbsp;','')
        product_seller= items.find_element(By.CLASS_NAME,'aULzUe.IuHnof').get_attribute('innerHTML')
        shippment_conditions= items.find_element(By.CLASS_NAME,'bONr3b').find_element(By.CLASS_NAME,'vEjMR').get_attribute('innerHTML')
        shippment_conditions=shippment_conditions.replace('&nbsp;','')
        product_img_url = items.find_element(By.CLASS_NAME,'ArOc1c').find_element(By.TAG_NAME,'img').get_attribute('src')
        product_seller_url= items.find_element(By.CLASS_NAME,'eaGTj.mQaFGe.shntl').find_element(By.TAG_NAME,'div').find_element(By.TAG_NAME,'a').get_attribute('href')
        

# add the information found to each list
        product_searched_list.append(product_to_search)
        product_descprition_list.append(product_descprition)
        product_price_list.append(product_price)
        product_seller_list.append(product_seller)
        shippment_conditions_list.append(shippment_conditions)
        product_img_url_list.append(product_img_url)
        product_seller_url_list.append(product_seller_url)
        search_date_list.append(date.today())

    product_search_df = pd.DataFrame({"product searched":product_searched_list,"product found description":product_descprition_list,
                    "product found price":product_price_list,"product found seller":product_seller_list,
                    "product found shippment conditions":shippment_conditions_list,
                    "product found seller url":search_date_list,
                    "product found shippment img URL":product_img_url_list})


    return product_search_df


def writeResults(resultsList):

    fileName='results_search.csv'
# check if results CSV file exitst and if not create it with the headers
    if not(os.path.exists(fileName)): 
          
          with open(fileName, 'w') as f:
                # using csv.writer method from CSV package
                write = csv.writer(f)
                write.writerow(resultsList.head())
# Write the DF in CSV    
    with open(fileName, 'a', newline='') as f:
                # using csv.writer method from CSV package
                write = csv.writer(f)
                write.writerows(resultsList.values)


searchResults=googleShoppingSearch('Iphone 6 italy')
writeResults(searchResults)

       