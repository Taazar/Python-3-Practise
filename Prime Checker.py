#Recursion
def check_prime_recur(number, iteration):
    if iteration <= 1:
        return True
    if number%iteration == 0:
        return False
    try:
        return check_prime_recur(number, iteration-1)
    except:
        return "Input too large to calculate using Python recursion."
def user_prog_recur():
    while True:
        number = input("\nPlease enter the number would you like to check: ")
        try:
            number = int(number)
            if number < 2:
                print("There are no prime numbers under two and you cannot have a prime number under zero.")
                continue
            break
        except:
            print("That was not a number.")
    temp = check_prime_recur(number, number/2)
    print(temp)

#Loops
def check_prime_loop():
    true = True
    while True:
        number = input("\nPlease enter the number would you like to check: ")
        try:
            number = int(number)
            if number < 2:
                print("There are no prime numbers under two and you cannot have a prime number under zero.")
                continue
            break
        except:
            print("That was not a number.")
    for i in range(2, number):
        if number%i == 0:
            true = False
            break
    print(true)
