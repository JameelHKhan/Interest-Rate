# Module 2 Assignment, part 1
# Jameel H. Khan

# solicit input terms for mortgage formula and
# convert string inputs to correct type, then save to formula variable
principal = int(input("Please enter the principal amount: "))
rate = float(input("Please enter the interest rate: "))
term = int(input("Please enter the term in years: "))
accrual = int(input("Please enter the number of times interest is accrued \
per year: "))

# formula calculation; nested parans to ensure proper order of operations
amount = principal*(1+(rate/accrual))**(accrual*term)
interestPaid = amount - principal

print("Total paid after " + str(term) + " years: " + str(amount))
print("Interest paid after " + str(term) + " years: " + str(interestPaid))
