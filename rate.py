# Module 2 Assignment, part 2
# Jameel H. Khan

# solicit input terms for interest formula and
# convert string inputs to correct type, then save to formula variable
principal = int(input("Please enter the principal amount: "))
amount = float(input("Please enter the total amount paid on the loan \
including both interest and principal: "))
term = int(input("Please enter the term in years: "))
accrual = int(input("Please enter the number of times interest is accrued \
per year: "))

# formula calculation; nested parans to ensure proper order of operations
rate = (((amount/principal)**(1/(accrual*term)))-1)*accrual

print("The interest rate on a loan for " + str(principal) + " that cost " \
      + str(amount) + " over " + str(term) + " years is: " + str(rate))
