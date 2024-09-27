from datetime import datetime,timedelta
current_date = datetime.now()
print(f"Current date and time: {current_date}")
def calculate_future_date():
    future_date = int(input("Enter the number of days to add to the current date: "))
    duration = timedelta(days=future_date)
    new_date = duration + current_date
    return new_date
print(f"Future date: {calculate_future_date()}")