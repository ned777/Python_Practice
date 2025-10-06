def uniqueWords():
    
    list_Of_Words=[]
    
    for i in user_Input:
        if i not in list_Of_Words:
            list_Of_Words.append(i)
    print(list_Of_Words)

user_Input=input("Type a sentence and I will display unique words (no dups): ").split()

uniqueWords()