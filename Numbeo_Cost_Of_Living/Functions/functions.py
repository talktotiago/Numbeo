from Variables.variables import *

def Items():
    for i in range(0, 163, 3):
        #f = open(r"numbeo/json/MarketsItems.json", "w+")
        table = soup.find("table", {"class": "data_wide_table"})
        all_items = table.findAll("td")
        save_to_Items = all_items[i].get_text()
        items_list.append(save_to_Items)
    print(items_list)

def Prices():
    for i in range(0, 55, 1):
        table = soup.find("table", {"class": "data_wide_table"})
        all_prices = table.findAll("td", {"class": "priceValue"})
        save_to_Prices = all_prices[i].get_text()
        prices_list.append(save_to_Prices)
    for idx, ele in enumerate(prices_list): 
        prices_list[idx] = ele.replace('\xa0€', '')
    for idx, ele in enumerate(prices_list): 
        prices_list[idx] = ele.replace(',', '.')
    print("Values are being shown in: "+currency) 
    print(prices_list)

def Last_Time_Updated_In_Source():
    lastupdate = soup.find("div", {"class": "align_like_price_table"})
    save_to_Last_Update= lastupdate.get_text()
    Last_Update.insert(0,save_to_Last_Update)
    print(save_to_Last_Update)
    for idx, ele in enumerate(Last_Update): 
        Last_Update[idx] = ele.replace('\n', '')
    print (Last_Update[0])