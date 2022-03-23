#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
#%%
'''
df = pd.read_csv("Equity Data (1 Jan 2020).csv")

df[" DATE1"] = df[" DATE1"].apply(lambda x : datetime.strptime(x,'%d-%m-%Y'))
    
final = pd.DataFrame()
shares = df["SYMBOL"]
shares = shares.drop_duplicates()
#shares = shares
count = 0
for share in shares:
    print(count)
    count+=1
    one_stock = pd.DataFrame()
    temp = df.loc[df["SYMBOL"]==share]
    one_stock = one_stock.append(temp)
    
    b = []
    d = []
    for i in [2020,2021,2022]:
        for j in range(1,13):
            mindate = datetime.max 
            maxdate = datetime.min
            for k in range(len(one_stock)):
                temp = one_stock.iloc[k][" DATE1"]
                if temp.year == i and temp.month == j:
                    if temp>maxdate:
                        maxdate = temp
                    if temp<mindate:
                        mindate = temp
            if mindate!=datetime.max:
                b.append(mindate)
            if maxdate!=datetime.min:
                d.append(maxdate)

    min_dates = pd.DataFrame()
    max_dates = pd.DataFrame()
    for j in b:
        for i in range(len(one_stock)):
            if one_stock.iloc[i][" DATE1"]==j:
                min_dates = min_dates.append(one_stock.iloc[i])
    
    for j in d:
        for i in range(len(one_stock)):
            if one_stock.iloc[i][" DATE1"]==j:
                max_dates = max_dates.append(one_stock.iloc[i])
    
    one_stock_final = pd.DataFrame()
    #one_stock_final.columns = ["Date", "Prev_close", "Close"]
    for i in [2020,2021,2022]:
        for j in range(1,13):
            temp = []
            for k in range(len(min_dates)):
                #print(k)
                if min_dates.iloc[k][" DATE1"].month == j and min_dates.iloc[k][" DATE1"].year == i:
                    temp.append(min_dates.iloc[k]["SYMBOL"])
                    temp.append(min_dates.iloc[k][" DATE1"])
                    temp.append(min_dates.iloc[k][" PREV_CLOSE"])
                    
            for k in range(len(max_dates)):
                if max_dates.iloc[k][" DATE1"].month == j and max_dates.iloc[k][" DATE1"].year == i:
                    temp.append(max_dates.iloc[k][" CLOSE_PRICE"])
                    
            if temp:
                temp = temp[-4:]
                #print(temp)
                temp.append(((temp[3]-temp[2])/temp[2])*100)
                one_stock_final = one_stock_final.append([temp])
    
    final = final.append(one_stock_final)


final.columns = ["Name","Date", "Prev_close", "Close", "Per_diff"]
final.to_csv("final.csv")
'''
final = pd.read_csv("final.csv")
final["Date"] = final["Date"].apply(lambda x : datetime.strptime(x,'%d-%m-%Y %H:%M'))

month = int(input("enter month (1-12):\n"))
year  = int(input("enter year (2020-2022):\n"))


query = pd.DataFrame()

for i in range(len(final)):
    if final.iloc[i]["Date"].month == month and final.iloc[i]["Date"].year == year:
        query = query.append(final.iloc[i,:])

query = query.sort_values("Per_diff")

top_performing = query.tail()["Name"][::-1]
worst_performing = query.head()["Name"]

print(f"The top performing stocks are : \n{top_performing}")
print(f"The worst performing stocks are : \n{worst_performing}")
























