def tower():
    while True:
        r=input("Please enter the number of rings: ")
        try:
            r=int(r)
            break
        except:
            print("That wasn't a number.")
    print("It will take a minimum of {} moves to complete this tower.\n".format(2**r-1))
    tower()
tower()
