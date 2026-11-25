# 1. Given words = ["apple", "kiwi", "banana", "fig"], create a list of the lengths of only the words longer than 3 characters.#


words = ["apple", "kiwi", "banana", "fig"]

words_3 = [word for word in words if len(word) > 3]

print(words_3)

# 2. Use a nested comprehension to flatten [[1, 2], [3, 4], [5, 6]] into [1, 2, 3, 4, 5, 6] #

A  = [[1,2],[3,4],[5,6]]
list_1 = [j for i in A for j in i]

print(list_1)

# 3. Create a list of tuples (x, y) for all x in range(1, 4) and y in range(1, 4) where x != y.#

list = [(x,y)for x in range(1,4) for y in range(1,4) if x!=y ]

print(list)

#4. Given nums = [1, 2, 3, 4, 5, 6], produce ["even", "odd", "even", ...] using a conditional expression inside the comprehension.#

nums = [1,2,3,4,5,6]
nums_list =  ["even" if num%2==0 and "odd" else num%2==1 for num in nums ]
print(nums_list)

#5. Convert a list of strings like ["1", "x", "3", "y"] into a list of ints, skipping anything that isn’t a digit (hint: str.isdigit()).#

mixed =  ["1", "x", "3", "y"]
fixed = [mixeds  for mixeds in mixed if str.isdigit(mixeds)]

print(fixed)


#6. Using a dict comprehension, build {word: len(word)} for each word in a list, and keep only the entries with length of 4 or more.#
list = ["ANOE","BLESSED","ZHOU"]
dict_comp = {word :len(word)  for word in list}
print(dict_comp)

