def years_to_100():
    import datetime
    a=datetime.datetime.now()
    a,b,c,d=a.year,input("Please enter your name: "),int(input("Please enter your age: ")),int(input("Please enter the number of times you want the result printed: "))
    print(d*("You will turn 100 years old in {} years and in the year {} {}.\n".format(100-c,100-c+a,b)))
    years_to_100()
years_to_100()
