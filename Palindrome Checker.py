import string
def palindrome():
    s=input("Please enter the string you would like to test: ")
    transtable={ord(c): None for c in string.punctuation}
    a=s.translate(transtable).lower().replace(' ', '')
    if a[::-1]==a:
        print("The string '{}' is a palindrome.\n".format(s))
    else:
        print("The string '{}' is not a palindrome.\n".format(s))
    palindrome()
palindrome()
