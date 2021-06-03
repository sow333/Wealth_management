Wealth management is an investment advisory service that combines other financial services to address the needs of affluent clients. Using a consultative process, the advisor gleans information about the client's wants and specific situation, and then tailors a personalized strategy that uses a range of financial products and services. It can encompass all parts of a person's financial life. Instead of attempting to integrate pieces of advice and various products from multiple professionals, high net worth individuals may be more likely to benefit from an integrated approach. In this method,  a wealth manager coordinates the services needed to manage their clients’ assets, along with creating a strategic plan for their current and future needs—whether it is will and trust services or business succession plans. 
Data used in Wealth management 
CustAccount 100000
    CustAccNum (PK)
    Name
    Email
    Address
    curr_balence       800
    
Bonds 10000
    Bond_id   (PK)  1
    Bond_name
    Min_amt       1000
    max_amt       100000
    interest      value range (10 - 35)
    duration_mons value range (3,6,12)


CustomerTransactions
    TnxId      (PK)
    CustAccNum (FK)
    amt
    tnx_type   (deposit/withdrawal/buy_bond/sell_bond/interest)
    bond_id    (FK)
    tnx_date 
    status    (failed/success)
    message


CustomerBonds
    CustomerBondId  (PK)
    CustAccNum      (Fk)
    Bond_id         (FK)  1
    start_date
    end_date
