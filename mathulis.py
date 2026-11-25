#Create mathutils.py with functions square(n) and cube(n). 
#Import it in another file and use both, first with import mathutils, then with from mathutils import square.

def square(z):
    return z ** 2

def cube(z):
    return z ** 3



#Add an if __name__ == "__main__": block to your module that runs a few test calls. Explain why those calls don’t run when the module is imported.#
if __name__ == "__main__":
    print(square(4))   # 16
    print(cube(3))     # 27
    print(square(-2))  # 4


for i in range(1,5):
    for j in range(i+1):
        print(j+1)