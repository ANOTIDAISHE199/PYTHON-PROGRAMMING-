from datetime import datetime 

birth_day = input("Enter your birth date (YYYY-MM-DD): ")
birth_day = datetime.strptime(birth_day, "%Y-%m-%d")

current_year = datetime.now()

age = current_year.year - birth_day.year

print(f"YOUR AGE IS {age}")



