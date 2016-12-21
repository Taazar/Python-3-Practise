print("This function will output the mean, median, mode and range of the values you enter.")
def average():
    while True:
        a,d=input("Please enter the number of values: "),[]
        try:
            a=int(a)
            if a<1:
                print("You need to have at least one value.")
                continue
            break
        except ValueError:
            print("You need to input a whole number.")
    for c in range(a):
        while True:
            temp=input("Please enter figure number {}: ".format(c+1))
            try:
                temp=int(temp)
                break
            except ValueError:
                print("You need to input a number.")
        d.append(temp)
    d.sort()
    print("Your mean is '{}'.".format((sum(float(c) for c in d))/len(d)))
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
            print("Your modes are '{}'.".format("', '".join([str(c) for c in temp])))
    else:
        print("Your mode is '{}'.".format(temp[0]))
    print("Your range is '{}'.\n".format(d[a-1]-d[0]))
    average()
average()
