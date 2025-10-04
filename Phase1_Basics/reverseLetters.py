def reverseLetters():
    i=len(inputPhrase)-1
    reverseSentence=[]
    
    while i>=0:
        reverseSentence.append(inputPhrase[i])
        i-=1
    print("".join(reverseSentence))
    
inputPhrase = input("Type a sentence:")
reverseWords()