from datetime import datetime,timedelta
def display_current_datetime():
    """Display the current date and time."""
    current_date = datetime.now()
    print("Current Date and Time:", current_date)
    print(f"Future date: {calculate_future_date(current_date)}")
def calculate_future_date(current_date):
    future_date = int(input("Enter the number of days to add to the current date: "))
    duration = timedelta(days=future_date)
    new_date = duration + current_date
    return new_date
if __name__ == "__main__":
    display_current_datetime()
