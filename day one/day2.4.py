# 🚨 calculate number of days left to live 👇



age = input("What is your current age? ")
newAge = int(age)
max_year = 90
years_in_days = 365 * max_year
years_in_weeks = 52 * max_year
years_in_months = 12 * max_year

age_in_days = newAge * 365
age_in_weeks = newAge * 52 
age_in_months = newAge * 12

print(f"You have {years_in_days - age_in_days} days, {years_in_weeks - age_in_weeks}, and {years_in_months - age_in_months} Months left")

