numbers  =[-2,3,-3,8,11]
posetive_num = [ num for num in numbers if num >= 0]
negative_num = [ num for num in numbers if num < 0]
even_num = [ num for num in numbers if num % 2 == 0 ]
odd_num = [ num for num in numbers if num % 2 == 1 ]

print(even_num)

grades = [85,42,79,90,56,61,30]
passing_grades  = [grade for grade in grades if grade >= 50 ]

print(passing_grades)
