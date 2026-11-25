dict2  = {"NAME" : "ANOTIDAISHE" , "AGE": 22, "COURSE" : "BCA","YEAR": 2025}

operation_choice = int(input( "SELECT OPERATION: "))
print("-----------------------")

if operation_choice == 1 :
    print("UPDATING THE DICTIONARY")
    print("-----------------------")
    Key = input("SELECT THE KEY TO UPDATE\n ¬NAME \n ¬AGE \n ¬COURSE \n ¬YEAR \n :")
    print()

    value = input( "ENTER THE VALUE: ")
    print("-----------------------")
    if Key== "NAME":
        dict2.update({"NAME": value})
    elif Key == "AGE":
        dict2.update({"AGE": value})
    elif Key == "COURSE":
        dict2.update({"COURSE": value})
    elif Key == "YEAR":
        dict2.update({"YEAR": value})
    else:
        print("invalid input")

elif operation_choice == 2:
    print("DELETING VALUES")
    key = input("ENTER ELEMENT TO DELETE")
    del dict2[key]


elif operation_choice == 3:
    print("ADDING NEW ELEMENT")
    key = input("ENTER KEY")
    value = input("ENTER VALUE")
    dict2["GRADE"] = "PASS"

elif operation_choice == 4:
    print("POPPING ELEMENT")
    Key = input("ELEMENT TO POP")
    dict2.pop(Key)


else:
    print("INVALID INPUT")  
    operation_choice = int(input( "SELECT OPERATION"))



for k,v in dict2.items():
    print(f"{k}: {v}")
        
 #  del dict2["YEAR"]
 #  dict2["GRADE"]="PASS"