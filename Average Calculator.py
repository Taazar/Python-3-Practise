print("This function will find the mean, median, mode and range of the values you enter.")
def average():
    b,d=1,[]
    while b==1:
        a,b=input("Please enter the number of values: "),0
        try:
            a=int(a)
            if a<1:
                print("You need to have at least one value.")
                b=1
        except ValueError:
            print("You need to input a whole number.")
            b=1
    b=1
    for c in range(a):
        while b==1:
            temp,b=input("Please enter figure number {}: ".format(c+1)),0
            try:
                temp=int(temp)
            except ValueError:
                print("You need to input a number.")
                b=1
        b=1
        d.append(temp)
    d.sort()
    temp = sum(float(c) for c in d)
    print("Your mean is '{}'.".format(temp/len(d)))
    temp=len(d)/2
    if temp-int(temp)==0:
        temp=(d[int(temp)]+d[int(temp-1)])/2
    else:
        temp=d[int(temp)]
    print("Your median is '{}'.".format(temp))
    temp=[d[0]]
    for c in range(1,a):
        if d.count(d[c])>d.count(temp[0]):
            temp=[d[c]]
        elif d.count(d[c])==d.count(temp[0]) and d[c]!=temp[len(temp)-1]:
            temp.append(d[c])
    if len(temp)>1:
        if len(temp)==a or len(temp)*d.count(temp[0])==a:
            print("There is no real mode, all your values appear an equal amount of times.")
        else:
            temp = [str(c) for c in temp]
            print("Your modes are '{}'.".format("', '".join(temp)))
    else:
        print("Your mode is '{}'.".format(temp[0]))
    print("Your range is '{}'.\n".format(d[a-1]-d[0]))
    average()
average()
