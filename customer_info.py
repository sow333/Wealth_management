# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
from faker import Faker 
import pymysql 
# csv file name
filename = "C:/Python37/Python_recent_projects/Wealth/custData.csv"
  
# initializing the titles and rows list
headers = ["CustAccNum","CustName","Email","Address","curr_balance"]
s_row = {}

fake = Faker() 

with open("customer_data.csv", 'w',encoding="UTF8",newline='') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=headers)
    writer.writeheader()
            
    for CustAccNum in range(0,10000): 
        s_CustAccNum = CustAccNum + 1
        s_CustName = fake.name()
        s_Email = fake.email()  
        s_Address = fake.street_address() 
        s_curr_balance= 0  
               
                
        s_row = {"CustAccNum" : s_CustAccNum,
                 "CustName" : s_CustName,
                 "Email": s_Email,
                 "Address" : s_Address,
                 "curr_balance" : s_curr_balance,
                } 
        writer.writerow(s_row)
        print(s_row)
"""
# Load CSV Process Start
# ##################################################
mydb = pymysql.connect(host='localhost',user='root', passwd='123456', db='wealthmanagement') 
cursor=mydb.cursor()
csv_data = csv.reader(open('C:/Python37/Python_recent_projects/Wealth management/cust_det.csv'))
l_ins_stmt = ""

ctr = 0
for row in csv_data:
   ctr += 1
   if ctr > 1:
       l_ins_stmt = "-"-"INSERT INTO custaccount(CustAccNum,Name,Email,Address,curr_balance)
       VALUES({0},'{1}','{2}','{3}',{4});"-"-".format(row[0],row[1],row[2],row[3],row[4]);
       
       print(l_ins_stmt)
       # break
   
       cursor.execute(l_ins_stmt) 
       cursor.commit()
#close the connection to the database.
   print("CSV Loaded",ctr,"Rows Complete!")
"""

  