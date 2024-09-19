task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: high is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: high is a {priority} priority task. Consider completing it when you have free time.")
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: medium is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: medium is a {priority} priority task. Consider completing it when you have free time.")
    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: low is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: low is a {priority} priority task. Consider completing it when you have free time.")