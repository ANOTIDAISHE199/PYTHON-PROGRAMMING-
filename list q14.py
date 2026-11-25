list = [1,2,2,3,4]

def remove_dup():
    new_list = []

    for i in list:
        if i  not in new_list:
            new_list.append(i)

    print(new_list) 

remove_dup()
