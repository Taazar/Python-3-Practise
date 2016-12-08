def odd_even():
    while True:
        b=input("Please enter the number you would like to check: ")
        try:
            b=int(b)
            break
        except:
            print("That was not a number.")
    while True:
        c=input("Please enter the number you would like to check it with: ")
        try:
            c=int(c)
            break
        except:
            print("That was not a number.")
    if b%4==0 and b!=0:
        print("The number {} is a multiple of 4.".format(b))
    elif b%2==0:
        print("The number {} is even.".format(b))
    else:
        print("The number {} is odd.".format(b))
    if b%c==0:
        print("The number {} is divisible by {}.\n".format(b,c))
    else:
        print("The number {} isn't divisible by {}.\n".format(b,c))
    odd_even()
odd_even()
