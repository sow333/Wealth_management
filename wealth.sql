create database wealthmanagement; 
use wealthmanagement; 

Create table CustAccount   
( 
	CustAccNum integer,
    CustName varchar(2000),
    Email varchar(100),
    Address integer, 
    curr_balance integer
    );   
    
alter table CustAccount add constraint CustAccount PRIMARY key (CustAccNum);

Create table Bonds   
( 
    Bond_id integer,
    Bond_name char(100),
    Min_amt integer,  
    Max_amt integer,
    interest decimal(10,2),
    duration integer
    );   
    
alter table Bonds add constraint Bonds PRIMARY key (Bond_id); 

Create table CustomerTransactions   
( 
    TnxId integer,
    CustAccNum integer,
    amt integer, 
    tnx_type integer,  
    bond_id integer,
    tnx_date date, 
    status char, 
    message char
    ); 
    
alter table CustomerTransactions add constraint CustomerTransactions PRIMARY key (tnxid);   
ALTER TABLE CustomerTransactions ADD CONSTRAINT FK_CustAccNum FOREIGN KEY (CustAccNum) REFERENCES CustAccount(CustAccNum);  

Create table CustomerBonds   
( 
    CustomerBondId integer,
    CustAccNum integer,
    Bond_id integer, 
    start_date date, 
    end_date date, 
    invested_amt integer 
    );    
    alter table CustomerBonds add constraint CustomerBonds PRIMARY key(CustomerBondId); 
    ALTER TABLE CustomerBonds ADD CONSTRAINT FK_CustomerBonds_CustAccNum FOREIGN KEY (CustAccNum) REFERENCES CustAccount (CustAccNum ); 
ALTER TABLE CustomerBonds ADD CONSTRAINT FK_CustomerBonds_Bond_id FOREIGN KEY (Bond_id) REFERENCES Bonds(Bond_id); 

select * from Bonds;
