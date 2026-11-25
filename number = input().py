number =  input()

if  len(number) > 10:
   print("NUMBER IS INVALID ")
elif len(number) < 10:
    print("NUMBER IS INVALID(2)")
else:
    pass

if number.isdigit():
    print("VALID NUMBER")

else:
    print("INVALID NUMBER")


