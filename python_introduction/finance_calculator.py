monthly_income = input("Enter your monthly income: ")
monthly_expenses = (input("Enter your total monthly expenses: "))
monthly_savings = float(monthly_income) - float(monthly_expenses)

Projected_Savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings}")