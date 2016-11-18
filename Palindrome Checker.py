def palindrome():
    s=input("Please enter the string you would like to test: ")
    if s[::-1] == s:
        print("The string '{}' is a palindrome.\n".format(s))
    else:
        print("The string '{}' is not a palindrome.\n".format(s))
    palindrome()
palindrome()
