import random
def list_overlap():
    a,b=random.sample(range(0, 100), 20),random.sample(range(0, 100), 15)
    print("The first list is {} and the second list is {}.\nThe numbers that appear in both those lists are {}.".format(sorted(a),sorted(b),sorted([x for x in a if x in b])))
list_overlap()
