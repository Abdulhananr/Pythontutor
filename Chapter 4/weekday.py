import sys
import datetime

try:
    input_year = int(input("Enter the year: "))
    input_month = int(input("Enter the month: "))
    input_day = int(input("Enter the day: "))
except ValueError:
    print('Year, month, and day must be integers')
    sys.exit(1)

# Check if month is within valid range (1 to 12)
if input_month < 1 or input_month > 12:
    raise ValueError('Month must be between 1 and 12')

# Check if day is within valid range (1 to 31)
if input_day < 1 or input_day > 31:
    raise ValueError('Day must be between 1 and 31')

# List of days of the week
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Calculate the day of the week
day_index = datetime.date(input_year, input_month, input_day).weekday()

# Print the corresponding day of the week
print("The day of the week for {}-{}-{} is: {}".format(input_year, input_month, input_day, days_of_week[day_index]))
