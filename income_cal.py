def calculate_income_tax(income):
   
    tax_brackets = [(0, 10000), (10001, 50000), (50001, 100000)]
    tax_rates = [0.10, 0.20, 0.30] 
    tax_owed = 0
    for i in range(len(tax_brackets)):
        min_income, max_income = tax_brackets[i]
        rate = tax_rates[i]
        
        if income <= min_income:
            break
        elif income <= max_income:
            tax_owed += (income - min_income) * rate
            break
        else:
            tax_owed += (max_income - min_income) * rate

    return tax_owed


income = float(input("Enter your annual income: "))

income_tax = calculate_income_tax(income)

print(f"Your income tax is: Rs {income_tax:.2f}")
