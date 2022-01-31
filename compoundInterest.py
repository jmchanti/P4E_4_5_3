def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundIntrest()
 getACompoundIntrest()
 print("---")
 getACompoundIntrest()
 print("---")
 getACompoundIntrest()
 #print("Compound Interest: "+str(intrest))

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
def getACompoundIntrest():
 client_one_principal = float(input("Principle (amount): "))
 client_one_time =      float(input("Time:               "))
 client_one_rate =      float(input("Rate:               "))+100
 intrest = client_one_principal*pow((client_one_rate/100),client_one_time)
 CI = intrest-client_one_principal
 roundedIntrest = round(CI, 2)
 print("Compound Interest:",str(roundedIntrest))

#calculateCompoundInterest()