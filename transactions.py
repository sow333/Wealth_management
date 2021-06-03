# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:37:36 2021

@author: sowmya
"""
from faker import Faker   
import csv 
import pymysql 

headers = ["TnxId", "CustAccNum", "amt", "tnx_type", "bond_id", "tnx_date", "status","message"]

def transactions(TnxId, CustAccNum, amt, tnx_type, bond_id, tnx_date, status,message):   
    fake = Faker()
    s_row={} 
    with open("trans.csv", 'wt',encoding='UTF8',newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for TnxId in range(0,10001):
            TnxId = TnxId + 1
            s_CustAccNum = CustAccNum+1
            s_amt = 1000 
            s_tnx_type = ["deposit","withdrawal","buy_bond","sell_bond","interest"]
            s_bond_id = bond_id+1 
            s_tnx_date = fake.date() 
            s_status = ["failed","success"]
            
            s_row = {"TnxId": TnxId+1, 
                     "CustAccNum": s_CustAccNum+1, 
                     "amt": s_amt+1, 
                     "tnx_type": s_tnx_type+1, 
                     "bond_id": s_bond_id+1, 
                     "tnx_date": s_tnx_date, 
                     "status": s_status,
                     "message": message}  
            writer.writerow(s_row) 
                
            
    s_result_dict = {"TnxId": TnxId, 
                     "CustAccNum": CustAccNum, 
                     "amt": amt, 
                     "tnx_type": tnx_type, 
                     "bond_id": bond_id, 
                     "tnx_date": tnx_date, 
                     "status": status,
                     "message": message }

    
    return s_result_dict 


conn=pymysql.connect(host='localhost',port=3306,user='root',password=123456,db="wealthmanagement") 
cursor=conn.cursor() 
csv_data=csv.reader(open('trans.csv')) 
header = next(csv_data)
for row in csv_data: 
    cursor.execute("insert into customertransactions values(TnxId,CustAccNum,amt,tnx_type,bond_id,tnx_date,status,message)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])) 
    header=next(csv_data) 
      