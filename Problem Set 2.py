##Problem Set 2
##20150627
#balance, annualInterestRate, or monthlyPaymentRate

def balance_after_one_year(balance, annualInterestRate, monthlyPaymentRate):
    i = 0
    total_paid = 0
    while i<12:
        Minimum_Payment = balance * monthlyPaymentRate
        Interest = (balance - Minimum_Payment)*(annualInterestRate/12)
        balance = balance - Minimum_Payment + Interest
        i = i + 1
        total_paid = total_paid + Minimum_Payment
        print "Month: " + str(i)
        print "Minimum monthly payment: " + str(round(Minimum_Payment,2))
        print "Remaining balance: " + str(round(balance,2))
    print "Total paid: "+str(round(total_paid,2))
    print "Remaining balance: " + str(round(balance,2))
    
balance_after_one_year(5000.00, 0.18, 0.02)