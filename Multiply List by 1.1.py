def multiply():
    a=[150,46,69,120,36]
    print(a)
    for b in range(len(a)):
        a[b]*=1.1
    print(a)
def multiply2():
    a=(150,46,69,120,36)
    print(a)
    a=[b*1.1 for b in a]
    print(a)
multiply2()
