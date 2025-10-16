def reverseWords():
    listOfWords = inputSentence.split()
    i=len(listOfWords)-1
    reverseSentence=[]
    
    while i>=0:
        reverseSentence.append(listOfWords[i])
        i-=1
    
    print(" ".join(reverseSentence))

inputSentence=input("Please type a sentence and I will reverse the sentence. Not the letters:")
reverseWords()