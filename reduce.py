import functools


"""example 1:
   reduce works like a recyle process , it iterate 
   till we get one result. for example
   the hello word given bellow ...the reduce function first
   adds first two elements as shown bellow(concatenation).
   
   step1: ["HE","L","L","O"]
   step2: ["HEL","L","O"]
   step3: ["HELL","O"]
   step4: ["HELLO"]
   so the final result is HELLO
    """

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y: x+y, letters)
print(word)

"""example 2:
   this function can be used to find a factorial of a number:
   step1: 5*4
        : [20,3,2,1]
   step2: 20*3
          [60,2,1]
   step3: 60*2
          [120,1]
   step4: 120*1
          120
   final result:: 120"""


factorial = [5,4,3,2,1]
word = functools.reduce(lambda x,y: x*y, factorial)
print(word)

