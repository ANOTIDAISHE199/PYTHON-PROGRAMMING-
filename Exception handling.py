# exception = an event that interrupts the flow of a program #

try:
    number = int(input("enter a number"))
    print(1/number)
except ZeroDivisionError:
    print("mf")
except ValueError:
    print("ff")
except Exception:
    print("f")

finally:
    print("DONE")