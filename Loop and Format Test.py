import time

def test_prog2():
    for i in range(1,101):
        print("Loading program: {}%".format(i))
        time.sleep(0.1)
    print("\n")
    time.sleep(2)
    for i in range(0,101,2):
        print("Backing up data: {}%".format(i))
        time.sleep(0.1)
    print("\n")
    time.sleep(2)
    for i in range(0,101,4):
        print("Initiating code testing: {}%".format(i))
        time.sleep(0.2)
    print("\n")
    time.sleep(2)
    print("All coding now godlike.")
test_prog2()
