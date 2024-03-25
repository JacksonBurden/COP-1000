salary = float(input("Enter salary: "))
numDependents = int(input("Enter number of dependents: "))
stateTaxRate = 0.065
federalTaxRate = 0.28
dependentDeductionrate = 0.025 
stateTax = salary * stateTaxRate
federalTax = salary * federalTaxRate
dependentDeduction = salary * dependentDeductionrate * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependent Deduction: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))