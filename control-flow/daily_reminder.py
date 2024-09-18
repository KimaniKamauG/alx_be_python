task_variable = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task_variable}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task_variable}' is a high priority task.")
    case 'medium':
        print(f"Note: '{task_variable}' is a medium priority task.")
    case 'low':
        print(f"Note: '{task_variable}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority.")
    
    
