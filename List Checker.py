def list_checker():
    a,b=1,[1,1,2,3,5,8,13,21,34,55,89]
    while a==1:
        a,c=0,input("Please enter the number you want all outputs to be smaller than: ")
        try:
            c=int(c)
        except:
            print("That was not a number.")
            a=1
    print("The values less than 5 in the list are {}.".format([d for d in b if d<5]))
    print("The values less than {} in the list are {}.\n".format(c,[d for d in b if d<c]))
    list_checker()
list_checker()
