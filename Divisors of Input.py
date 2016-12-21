def divisors():
    while True:
        b=input("Please enter your number: ")
        try:
            b=int(b)
            break
        except:
            print("That wasn't a number.")
    print("Your number is exactly divisible by '{}'.\n".format("', '".join([str(i) for i in range(1,b+1) if b%i==0])))
    divisors()
divisors() 
