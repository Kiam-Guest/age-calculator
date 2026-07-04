from datetime import date
date_of_birth = input("Please enter your date of birth in format (dd/mm/yyyy): ").strip()
day_str, month_str, year_str = date_of_birth.split("/") #Splits user input to allow calculation of age in days

birthdate = date(int(year_str), int(month_str), int(day_str))

#Calculation
today = date.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
age_in_days = (today - birthdate).days
age_in_hours = age_in_days * 24
age_in_minutes = age_in_hours * 60
age_in_seconds = age_in_minutes * 60

#print results to user
print(f"you are {age} years old")
print(f"you are {age_in_days} days old")
print(f"you are {age_in_hours} hours old")
print(f"you are {age_in_minutes} minutes old")
print(f"you are {age_in_seconds} seconds old")