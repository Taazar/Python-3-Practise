print("This function will output the mean, median, mode and range of the values you enter.")
def average():
    while True:
        valCount, valList = input("Please enter the number of values: "), []
        try:
            valCount = int(valCount)
            if valCount < 1:
                print("You need to have at least one value.")
                continue
            break
        except ValueError:
            print("You need to input a whole number.")
	
    for i in range(valCount):
        while True:
            temp = input("Please enter figure number {}: ".format(i + 1))
            try:
                temp=int(temp)
                break
            except ValueError:
                print("You need to input a number.")
        valList.append(temp)
    valList.sort()
    print("Your mean is '{}'.".format((sum(float(i) for i in valList)) / len(valList)))
	
    temp = len(valList) / 2
    if temp - int(temp) == 0:
        temp = (valList[int(temp)] + valList[int(temp - 1)]) / 2
    else:
        temp = valList[int(temp)]
    print("Your median is '{}'.".format(temp))
	
    temp = [valList[0]]
    for i in range(1, valCount):
        if valList.count(valList[i]) > valList.count(temp[0]):
            temp = [valList[i]]
        elif valList.count(valList[i]) == valList.count(temp[0]) and valList[i] != temp[len(temp) - 1]:
            temp.append(valList[i])
	
    if len(temp) > 1:
        if len(temp) == valCount or len(temp) * valList.count(temp[0]) == valCount:
            print("There is no real mode, all your values appear an equal amount of times.")
        else:
            print("Your modes are '{}'.".format("', '".join([str(i) for i in temp])))
    else:
        print("Your mode is '{}'.".format(temp[0]))
    print("Your range is '{}'.\n".format(valList[valCount - 1] - valList[0]))
    average()

average()
