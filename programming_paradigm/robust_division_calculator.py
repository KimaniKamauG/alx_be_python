def safe_divide(numerator, denominator):

    try:
        num = float(numerator)
        denom = float(denominator)
    
        result = num / denom
        return f'The result of the division result is {result:.1f}'
    
    except ZeroDivisionError:
        print(f'Error: Cannot divide by zero.')

    except ValueError:
        print(f'Error: Please enter numeric values only.')