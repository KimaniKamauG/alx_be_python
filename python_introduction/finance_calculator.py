monthly_income = float(input('Enter your monthly income: '))
monthly_expenses = float(input('Enter your monthly expenses: '))
monthly_savings = int(float(monthly_income) - float(monthly_expenses))
annual_interest_rate = 0.05
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate))
print(f'Your monthly savings are ${monthly_savings}.')
print(f'Projected savings after one year, with interest, is: ${projected_savings}.')
