def day_of_the_week(day):
    if day == 1:
        print("SUNDAY")
    elif day == 2:
        print("MONDAY")
    elif day == 3:
        print("TUESDAY")
    elif day == 4:
        print("WEDNESDAY")
    elif day == 5:
        print("THURSDAY")
    elif day == 6:
        print("FRIDAY")
    elif day == 7:
        print("SUTERDAY")
    else:
        print("INVALID INPUT")

day = int(input()) 
print(day_of_the_week(day))     


def day_of_the_week(day):
    match day:
        case 1:
            print("SUNDAY")
        case 2:
            print("MONDAY")
        case 3:
            print("TUESDAY")
        case 4:
            print("WEDNESDAY")
        case 5:
            print("THURSDAY")
        case 6:
            print("FRIDAY")
        case 7:
            print("SUTERDAY")
        case _:
            print("INVALID INPUT")

day = int(input()) 
print(day_of_the_week(day))   

def is_weekend (day):
    match day:
        case "monday" |"tuesday" |"wednesday" | "thursday"|"friday":
            return False
        case "saturday"| "sunday":
            return True
        case _:
            return "invalid input"

day = input()
print(is_weekend(day))


        