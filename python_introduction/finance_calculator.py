mon_income = float(input("Enter your monthly income: "))
mon_expenses = float(input("Enter your total monthly expenses: "))
mon_saving = (mon_income - mon_expenses)
Projected_Saving = (mon_saving* 12 + (mon_saving * 12 * 0.05))
mon_savings = float(mon_saving)
Projected_Savings = float(Projected_Saving)

print(f"Your monthly savings are ${mon_savings}")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings}")