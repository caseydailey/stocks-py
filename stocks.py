#Create a simple dictionary with ticker symbols and company names.
stockDict = { 
 'GM': 'General Motors',
 'CAT':'Caterpillar', 
 'GE':"General Electric" }


#Create a simple list of blocks of stock. 
#These could be tuples with ticker symbols, number of shares, dates and price.
purchases = [ 
 ( 'GE', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'GE', 200, '1-jul-1998', 56 ) ]

#Create a purchase history report that computes the full purchase price 
#(shares * dollars) for each block of stock 
portfolio = dict()
for purchase in purchases:
    ticker = purchase[0]
    full_company_name = stockDict[ticker]
    number_of_shares = purchase[1]
    purchase_price = purchase[3]
    full_purchase_price = number_of_shares * purchase_price

#Create a second purchase summary that which accumulates 
#total investment by ticker symbol. 
    try:
        portfolio[ticker].append(purchase)#append the purchase (tuple) to the ticker list
    except KeyError:
        portfolio[ticker] = list()#If the key doesn't exist yet, create it
        portfolio[ticker].append(purchase)

    #print("I purchase {} stock for ${}".format(full_company_name, full_purchase_price))

#iterate through portfolio 
#(a dictionary with ticker purchase pairs where purchases are list of tuples)    
for ticker,purchases in portfolio.items():
    print("--------{}----------".format(ticker))
    total_portfolio_stock_value = 0
    for purchase in purchases:
        total_portfolio_stock_value += purchase[1] * purchase[3]
        print("   {}".format(purchase))
    print("Total value of stock in portfolio: ${}\n\n".format(total_portfolio_stock_value))









