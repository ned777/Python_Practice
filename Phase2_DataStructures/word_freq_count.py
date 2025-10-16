def word_freq_count():
    list_Of_Words = {}
    
    for word in user_Input:
        if word in list_Of_Words:
            list_Of_Words[word]+=1
        else:
            list_Of_Words[word]=1
            
    print(list_Of_Words)
    
    

user_Input = input("Type a sentence: ").lower().split()
word_freq_count()
