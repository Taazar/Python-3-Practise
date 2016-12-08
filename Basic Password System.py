def pass_check():
    password, attempts = "Password", 3
    while attempts > 0:
        entry = input("Password: ")
        if entry == password:
            print("Password Confirmed. Welcome Back User!")
            break
        else:
            attempts = attempts - 1
            if attempts == 0:
                print("Password Denied. You Have Used All 3 Attempts. Account Locked!")
            else:
                print("Password Denied. You Have {} Attempts Left!".format(attempts))
pass_check()
