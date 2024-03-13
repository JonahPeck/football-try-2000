import datetime

def day_of_week():
    date_str = input("Enter a date (YYYY-MM-DD): ")
    try:
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%A')
    except ValueError:
        return "Invalid date format. Please provide the date in YYYY-MM-DD format."

# Example usage:
print("Let's find out the day of the week!")
print(f"The day of the week for the entered date is: {day_of_week()}")

# comment