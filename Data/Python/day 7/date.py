import re

pattern = r'(0[1-9]|[12][0-9]|3[01])/(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/\d{4}'

date = input("Enter date (dd/mon/yyyy): ")

if re.fullmatch(pattern, date):
    print("Valid date format")
else:
    print("Invalid date format")
