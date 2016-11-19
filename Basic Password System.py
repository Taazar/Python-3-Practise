def pass_check():
    attempts = 3
    password = "Password"
    while attempts > 0:
        entry = input("Password: ")
        if entry == password:
            print("Password Confirmed. Welcome Back User!")
            attempts = 0
        else:
            attempts = attempts - 1
            if attempts == 0:
                print("Password Denied. You Have Used All 3 Attempts. Account Locked!")
            else:
                print("Password Denied. You Have {} Attempts Left!".format(attempts))
pass_check()


