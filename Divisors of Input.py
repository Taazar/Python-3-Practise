def divisors():
    a,c=1,[]
    while a==1:
        a,b=0,input("Please enter you number: ")
        try:
            b=int(b)
        except:
            print("That wasn't a number.")
            a=1
    for d in range(1,b+1):
        if b%d==0:
            c.append(str(d))
    print("Your number is exactly divisible by '{}'.\n".format("', '".join(c)))
    divisors()
divisors()
