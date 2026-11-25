"""Write a Python program to calculate the number of days between two given dates.
Example: (2014, 7, 2) and (2014, 7, 11) → 9 days."""


print("--------------------")
print("       YEARS       ")
print("--------------------")


print("enter first year: ")
year1= int(input())
if year1 < 1800 and year1 > 3000:
    print("Invalid Range")
    year1= int(input())

print("enter second year: ")
year2= int(input())
if year2 < 1800 and year2 > 3000 and year2 > year1:
    print("Invalid Range")
    year2= int(input())

year_diff = year1 - year2

print("--------------------")
print("       MONTHS       ")
print("--------------------")


print("enter first month: ")
month1= int(input())
if month1 < 0 and month1 > 12:
    print("Invalid Range")
    month1 = int(input())

print("enter second month: ")
month2= int(input())
if month2 < 0 and month2 > 12 :
    print("Invalid Range")
    month2 = int(input())
    
month_diff = month1 - month2

print("--------------------")
print("       DAYS       ")
print("--------------------")


print("enter first day: ")
day1= int(input())
if day1 < 0 and day1 > 30:
    print("Invalid Range")

print("enter second day: ")
day2= int(input())
if day2 < 0 and day2 > 30 :
    print("Invalid Range")

day_diff = day1 - day2
print(f"{year_diff} years {month_diff} months {day_diff} days")







 