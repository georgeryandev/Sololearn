import random
#The mathFunction is an optional argument, default is set to "+"
def encrypt(string, key,mathFunction="+"):
    words=[]
    for char in string:
        #This gets the unicode value for each character in the string.
        unicode=ord(char)
        if mathFunction is "+":
            #The encrypt function does the opposite to the character than the decrypt function.
            #It then appends the character to an array.
            words.append(chr(unicode+key))
        if mathFunction is "-":
            words.append(chr(unicode-key))
        if mathFunction is "*":
            words.append(chr(unicode*key))
        if mathFunction is "/":
            words.append(chr(unicode/key))
            #This converts the array to a string.
        wordsString="".join(words)
    return wordsString
#The mathFunction is an optional argument, default is set to "+"
def decrypt(string, key, mathFunction="+"):
    words=[]
    for char in string:
        unicode=ord(char)
        if mathFunction is "+":
            #The decrypt function does the opposite to the character than the encrypt function.
            words.append(chr(unicode-key))
        if mathFunction is "-":
            words.append(chr(unicode+key))
        if mathFunction is "*":
            words.append(chr(int(unicode/key)))
        if mathFunction is "/":
            words.append(chr(int(unicode*key)))
        wordsString="".join(words)
    print(wordsString)
#If you do not know the seed or what math function was used than this will print out all possible outcomes
#within a given range.
def bruteForce(string, numRange):
    keyGuess=0
    tries=0
    print("Addition \n")
    for i in range(numRange):
        keyGuess=keyGuess+1
        decrypt(string,keyGuess, "+")
    keyGuess=0
    print("Subtraction \n")
    for i in range(numRange):
        keyGuess=keyGuess+1
        decrypt(string,keyGuess, "-")
    keyGuess=0
    print("Multiplication \n")
    for i in range(numRange):
        keyGuess=keyGuess+1
        decrypt(string,keyGuess, "*")
    keyGuess=0
    print("Division \n")
    for i in range(numRange):
        keyGuess=keyGuess+1
        decrypt(string,keyGuess, "/")
def passwordSalt():
    x=random.randint(1, 10)
    print(x)
bruteForce("H", 10)