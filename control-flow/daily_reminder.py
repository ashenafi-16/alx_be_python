task = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match task_priority:
    case task_priority if time_bound:
        print(f"Reminder: {task} is a {task_priority} priority task that requires immediate attention today!")
    case _:
        print(f"Note: {task} is a {task_priority} priority task. Consider completing it when you have free time.")