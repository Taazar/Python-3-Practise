def tower():
    while True:
        rings = input("Please enter the number of rings: ")
        try:
            rings = int(rings)
            break
        except:
            print("That wasn't a number.")
    print("It will take a minimum of {} moves to complete this tower.\n".format((2**rings) - 1))
    tower()

tower()
