""" Store student names and marks in a dictionary and display students who scored above 75"""

students = {"NAME":[ "ANOE","BLESSED","ZHOU"],"MARKS": [80,90,75]}

def diplay_student():
    for i in range(len(students["NAME"])):
        if students["MARKS"][i] > 75:
            print(students["NAME"][i])

diplay_student()



def view_student():
    for i in len(students["NAME"]):
        if students["MARKS"][i] > 78:
                               print(students["NAME"][i])