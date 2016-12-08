def namefinder():
    name="alan"
    while True:
        b=input("Say my name! ")
        if b.lower()==name:
            print("Congratulations, you guessed correctly! ")
            break
        else:
            print("That's not my name!")
namefinder()
