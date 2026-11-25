"""Create a student dictionary containing name, roll number, and marks. Calculate the student’s
 total and average marks."""

student = { "name":"ANOE", "roll_number": "102", "marks": [90,88,70,89,98]}

def student_total():
    total = sum(student["marks"])
    print(total)

def student_avg():
    avg = sum(student["marks"])/len(student["marks"])
    print(avg)
    return avg

def student_grade():

    avg = student_avg()

    if avg >= 90:
        print("A")
    elif avg >= 80:
        print("B")
    elif avg >= 70:
        print("C")
    elif avg >= 60:
        print("D")
    else:
        print("E")

student_total()
student_grade()