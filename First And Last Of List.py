from random import sample

def first_and_last(old_list):
    return [old_list[0], old_list[-1]]

old_list = sample(range(0,100),10)
print("{} -> {}".format(list(old_list), first_and_last(old_list)))
