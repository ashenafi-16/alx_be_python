from datetime import datetime,timedelta
def display_current_datetime():
    """Display the current date and time."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S") 
    print("Current Date and Time:", formatted_date)
    print(f"Future date: {calculate_future_date(current_date)}")
def calculate_future_date(current_date):
    future_date = int(input("Enter the number of days to add to the current date: "))
    duration = timedelta(days=future_date)
    new_date = duration + current_date
    return new_date.strftime("%y-%m-%d")
if __name__ == "__main__":
    display_current_datetime()
