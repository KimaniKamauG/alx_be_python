monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your monthly expenses: '))
monthy_savings = float(monthly_income) - float(monthly_expenses)
annual_interest_rate = 0.05
projected_savings = int(monthy_savings * 12 + (monthy_savings * 12 * annual_interest_rate))
print(f'Projected savings after one year, with interest, is: ${projected_savings}')
