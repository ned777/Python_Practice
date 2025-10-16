def palindrome():
    i=len(inputWord)-1
    reversedWord=""
    
    while i>=0:
        reversedWord+=inputWord[i]
        i-=1
    
    if reversedWord == inputWord:
        print("Same")
    else:
        print("Different")
        

       
inputWord=input("Type a text:").strip().lower()        
palindrome()