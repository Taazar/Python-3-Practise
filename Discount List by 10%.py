from random import sample
def discount_ten():
    a=sample(range(0, 100), 10)
    print("Ten percent of all the values in the list {} is {}".format(sorted(a), sorted([x*0.9 for x in a])))
discount_ten()
