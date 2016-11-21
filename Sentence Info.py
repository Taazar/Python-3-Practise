def sentence():
    a=str(input("What is your sentence? "))
    b=len(a)
    c=b-a.count(" ")
    print("Your sentence has a length of {} characters and spaces.".format(b))
    print("Your sentence has a length of {} characters.".format(c))
    print("'{}' is the first half of your sentence.".format(a[:int(b/2)]))
    print("'{}' is the second half of your sentence.".format(a[int(b/2):]))
    if"the "in a.lower()or" the "in a.lower()or" the"in a.lower():
        print("Your sentence contains the word 'the'.")
    else:
        print("Your sentence does not contain the word 'the'.")
    if a == a.upper():
        print("Your sentence contains only uppercase characters.")
        print("Your sentence does not contain only lowercase characters.")
    elif a == a.lower():
        print("Your sentence does not contain only uppercase characters.")
        print("Your sentence contains only lowercase characters.")
    else:
        print("Your sentence does not contain only uppercase characters.")
        print("Your sentence does not contain only lowercase characters.")
    print("'{}' is your sentence in uppercase characters.".format(a.upper()))
    print("'{}' is your sentence in lowercase characters.".format(a.lower()))
    print("'{}' is the unchanged sentence you inputted.\n".format(a))
    sentence()
sentence()
