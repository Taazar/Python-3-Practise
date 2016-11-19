def odd_even():
    a=1
    while a==1:
        a,b=0,input("Please enter the number you would like to check: ")
        try:
            b=int(b)
        except:
            print("That was not a number.")
            a=1
    while a==0:
        a,c=1,input("Please enter the number you would like to check it with: ")
        try:
            c=int(c)
        except:
            print("That was not a number.")
            a=0
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
