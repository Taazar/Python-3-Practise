def factorial():
    total=1
    while True:
        user=input("Please enter your value: ")
        try:
            user=int(user)
            if user<0:
                print("You cannot get a factorial of a negative number.")
                continue
            elif user==0:
                print("The factorial of '0' is '0'.")
                continue
            break
        except:
            print("You must enter a number.")
    for a in range(user):
        total *= a+1
    print("The factorial of '{}' is '{}'.".format(user,total))
    factorial()

def factorial2():
    while True:
        user=input("Please enter your value: ")
        try:
            user=int(user)
            if user<0:
                print("You cannot get a factorial of a negative number.")
                continue
            elif user==0:
                print("The factorial of '0' is '0'.")
                continue
            elif user>993:
                print("Stack overflow occured. The maximum factorial this program can calculate is 993.")
                continue
            break
        except:
            print("You must enter a number.")
    print("The factorial of '{}' is '{}'.".format(user,factorial2_sub(user)))
    factorial2()

def factorial2_sub(a):
    if a==1:
        return 1
    else:
        return a*factorial2_sub(a-1)
