'''
Two friends Anna and Brian, are deciding how to split the bill at a dinner. 
Each will only pay for the items they consume. Brian gets the check and calculates Anna's 
portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2, 4, 6]. 
Anna declines to eat item 'k=bill[2]' which costs 6. If Brian calculates the bill correctly, 
Anna will pay '(2+4)/2= 3'. If he includes the cost of bill[2], he will calculate (2+4+6)/2 = 6 . 
In the second case, he should refund 3 to Anna.

Output should be:

It should print Bon Appetit if the bill is fairly split. Otherwise, it 
should print the integer amount of money that Brian owes Anna.

'''

def bonAppetit(bill, anna_pays, anna_declines):
    # Iterate over array or bill items to find the accurate division
    accurate_price_to_pay = 0
    for bill_price in range(len(bill)):
        if bill_price == anna_declines:
            continue                    # Anna Decline by skip the iterate
        accurate_price_to_pay += bill[bill_price]
        
    # Divide accurate_price_to_pay to 2 persons
    accurate_price_to_pay = int(accurate_price_to_pay / 2)
    
    if accurate_price_to_pay == anna_pays:
        return "Bon Appetit"
    else:
        return anna_pays - accurate_price_to_pay       # refund  to Anna
    
    
    
    
if __name__ == "__main__":
    
    bill = [3, 10, 2, 9]
    anna_declines = 1         # bill[1] = 10
    anna_pays = 12
    
    print(bonAppetit(bill, anna_pays, anna_declines))
    
    