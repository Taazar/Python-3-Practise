def namefinder():
    name,a="alan",0
    while a==0:
        b=input("Say my name! ")
        if b.lower()==name:
            print("Congrats, you guessed correctly! ")
            a=1
        else:
            print("That's not my name!")
namefinder()
