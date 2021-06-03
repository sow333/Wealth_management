# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 12:44:17 2021

@author: sowmya
"""

import csv
from faker import Faker 
import pymysql  
import random

filename = "customer_data.csv"
  
# initializing the titles and rows list
headers = ["Bond_id","Bond_name","min_amt","max_amt","interest", "duration"]
s_row = {}

fake = Faker() 

with open("bond_info", 'wt',encoding="UTF8",newline='') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=headers)
    writer.writeheader()
            
    for Bond_id in range(0,10000): 
        s_Bond_id = Bond_id + 1
        s_Bond_name = fake.name()
        s_min_amt = 1000 
        s_max_amt = 100000
        s1 = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
        s_interest = s1[random.randint(0,25)] 
        s2= [3,6,12]
        s_duration = s2[(random.randint(0,2))]
            
        s_row = {"Bond_id": s_Bond_id+1,
                 "Bond_name": s_Bond_name,
                 "min_amt": s_min_amt,
                 "max_amt": s_max_amt,
                 "interest":s_interest,
                 "duration":s_duration}  
        writer.writerow(s_row) 

        mydb = pymysql.connect(host='localhost',user='root', passwd='123456', db='wealthmanagement') 
        cursor=mydb.cursor()
        csv_data = csv.reader(open('C:/Python37/Python_recent_projects/Wealth management/bond_info.csv'))
        l_ins_stmt = ""
        
        ctr = 0
        for row in csv_data:
           ctr += 1
           if ctr > 1:
               l_ins_stmt = """INSERT INTO customerbonds(Bond_id,Bond_name,min_amt,max_amt,interest,duration)
               VALUES({0},'{1}',{2},{3},{4},{5});""".format(row[0],row[1],row[2],row[3],row[4],row[5]);
               
               print(l_ins_stmt)
              
           
               cursor.execute(l_ins_stmt) 
               cursor.commit() 
               cursor.close()
        #close the connection to the database.
           print("CSV Loaded",ctr,"Rows Complete!")
           print("CSV generation complete!")