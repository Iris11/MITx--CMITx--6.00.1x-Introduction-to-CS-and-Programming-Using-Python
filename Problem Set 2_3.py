##Problem Set 2-2
##20150627
#balance, annualInterestRate

epsilon = 0.01
lower = balance / 12
upper = balance * ((1 + annualInterestRate / 12.0) ** 12) / 12.0
result = (lower + upper) / 2.0

def rest(monthlyPayment):
    rest_balance = balance
    for m in range(12):
        interest = (rest_balance - monthlyPayment) * annualInterestRate / 12.0
        rest_balance = rest_balance + interest - monthlyPayment
    return rest_balance

while abs(rest(result)) >= epsilon:
    if rest(result) < 0:
        upper = result
    else:
        lower = result
    result = (lower + upper) / 2.0
    
print ("Lowest Payment: " + str(round(result, 2)))