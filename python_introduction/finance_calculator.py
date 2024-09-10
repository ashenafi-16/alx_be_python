mon_income = int(input("Enter your monthly income: "))
mon_expenses = -(int(input("Enter your total monthly expenses: ")))
mon_savings = mon_expenses + mon_income
Projected_Savings = round(mon_savings * 12 + (mon_savings * 12 * 0.05))

print(f"Your monthly savings are ${mon_savings}.")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings}.")