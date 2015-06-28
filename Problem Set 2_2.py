##Problem Set 2-2
##20150627
#balance, annualInterestRate

def fixed_monthly_payment(balance, annualInterestRate):
    result = 0
    rest = balance
    while rest>0: 
        result = result + 10       
        rest = balance
        i = 0
        while i < 12:
            Interest = (rest - result)*(annualInterestRate/12)
            rest = rest - result + Interest
            i = i + 1
        
    print "Lowest Payment: "+str(result)
    
fixed_monthly_payment(9, 0.18)
    