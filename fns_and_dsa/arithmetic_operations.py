def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            result = num1 + num2
        case 'subtract':
            result = num1 - num2
        case 'multiply':
            result = num1 * num2
        case 'divide':
            if num1 == 0 or num2 == 0:
                result = print('Cannot divide by zero')
            elif num1 != 0 or num2 != 0:
                result = num1 / num2
        case _:
            print('Invalid Operation')
    
    return result