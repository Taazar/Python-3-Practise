def factorial():
    a,total=1,1
    while a==1:
        a=0
        user=input("Please enter your value: ")
        try:
            user=int(user)
            if user<0:
                print("You cannot get a factorial of a negative number.")
                a=1
            elif user==0:
                print("The factorial of '0' is '0'.")
                a=1
        except:
            print("You must enter a number.")
            a=1
    for a in range(user):
        total *= a+1
    print("The factorial of '{}' is '{}'.".format(user,total))
    factorial()

def factorial2():
    a,total=1,1
    while a==1:
        a=0
        user=input("Please enter your value: ")
        try:
            user=int(user)
            if user<0:
                print("You cannot get a factorial of a negative number.")
                a=1
            elif user==0:
                print("The factorial of '0' is '0'.")
                a=1
            elif user>993:
                print("Stack overflow occured. The maximum factorial this program can calculate is 993.")
                a=1
        except:
            print("You must enter a number.")
            a=1
    print("The factorial of '{}' is '{}'.".format(user,factorial2_sub(user)))
    factorial2()

def factorial2_sub(a):
    if a==1:
        return 1
    else:
        return a*factorial2_sub(a-1)
