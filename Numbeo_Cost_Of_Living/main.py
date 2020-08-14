import json
import os
import pandas as pd
from Variables.variables import *
from Functions.functions import *
from Setup.setup import *

Last_Time_Updated_In_Source()


Items()
Prices()

#MarketsItems()
#print(Markets_Items)
#print(items_list)
print(prices_list)

def Make_Excel():
    for i in range(0,5):
        print("\n")
    print("Making Excel File with Prices from "+city+"\n")
    City = {'Items': items_list,
        'Price': prices_list,
        'Currency': currency,
            }
    df = pd.DataFrame(City, columns = ['Items', 'Price','Currency'])
    df.to_excel (r'Numbeo_City.xlsx', index = False, header=True)
    print(df)

Make_Excel()