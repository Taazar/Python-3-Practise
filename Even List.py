import random
def even_list():
    a=random.sample(range(0,100),20)
    print("The even numbers in the list {} are {}.".format(sorted(a),sorted([x for x in a if x%2==0])))
even_list()
