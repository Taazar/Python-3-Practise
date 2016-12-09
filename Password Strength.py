print("This function takes your password and finds its strength. Strenght is determined by the presence of uppercase, lowercase and numeric characters. (Symbols do not count!)")
def strength_checker():
    entry,strength=input("Please enter the password you wish to check: "),0
    if len(entry) < 6:
        print("Password too short. (Under 6 characters)")
    elif len(entry) > 12:
        print("Password is too long.(Over 12 characters)")
    else:
        if any(char1.isupper() for char1 in entry):
            strength = strength + 1
        if any(char2.islower() for char2 in entry):
            strength = strength + 1
        if any(char3.isdigit() for char3 in entry):
            strength = strength + 1
        if strength == 1:
            print("Password strength is weak.")
        else:
            if strength == 2:
                print("Password strength is medium.")
            else:
                if strength == 3:
                    print("Password strength is strong.")
    strength_checker()
strength_checker()
