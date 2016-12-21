from random import sample

def my_sorter(old_list):
    new_list = []
    for _ in range(len(old_list)):
        new_list.append(min(old_list))
        old_list.remove(min(old_list))
    return new_list
old_list = sample(range(0,100),10)
print("Starting list: {} \nFinished list: {} \n".format(list(old_list), my_sorter(old_list)))
