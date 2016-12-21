def fibonacci():
    while True:
        user = input("Please enter the number of fibonacci numbers you want outputted: ")
        try:
            user = int(user)
            break
        except:
            print("That was not a number.")
    a,b,c = 1,0,0
    for i in range(user):
        if i<2:
            print(i)
            continue
        if i%2==0:
            c,b = a+b,a
            print(c)
            continue
        a,b = b+c,c
        print(a)
