def tower():
    a=1
    while a==1:
        r,a=input("Please enter the number of rings: "),0
        try:
            r=int(r)
        except:
            print("That wasn't a number.")
            a=1
    print("It will take a minimum of {} moves to complete this tower.\n".format(2**r-1))
    tower()
tower()
