monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your monthly expenses: '))
annual_interest_rate = 0.05
monthly_savings = (monthly_income - monthly_expenses or float(monthly_income) - float(monthly_expenses))
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate))
print(f'Your monthly savings are ${str(monthly_savings)}.')
print(f'Projected savings after one year, with interest, is: ${str(projected_savings)}.')
