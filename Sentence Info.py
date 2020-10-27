def sentence():
    inText = str(input("What is your sentence? "))
    lenText = len(inText)
    charLength = lenText - inText.count(" ")
	
    print("Your sentence has a length of {} characters and spaces.".format(lenText))
    print("Your sentence has a length of {} characters.".format(charLength))
    print("'{}' is the first half of your sentence.".format(inText[:int(lenText / 2)]))
    print("'{}' is the second half of your sentence.".format(inText[int(lenText / 2):]))
	
    if "the " in inText.lower() or " the " in inText.lower() or " the" in inText.lower():
        print("Your sentence contains the word 'the'.")
    else:
        print("Your sentence does not contain the word 'the'.")
    if inText == inText.upper():
        print("Your sentence contains only uppercase characters.")
        print("Your sentence does not contain only lowercase characters.")
    elif inText == inText.lower():
        print("Your sentence does not contain only uppercase characters.")
        print("Your sentence contains only lowercase characters.")
    else:
        print("Your sentence does not contain only uppercase characters.")
        print("Your sentence does not contain only lowercase characters.")
	
    print("'{}' is your sentence in uppercase characters.".format(inText.upper()))
    print("'{}' is your sentence in lowercase characters.".format(inText.lower()))
    print("'{}' is the unchanged sentence you inputted.\n".format(inText))
    sentence()

sentence()
