def reverseRecursive(word, index, reverse=[]):
    
    if index<0:
        return(reverse)
        
    else:     
        reverse.append(word[index])
        return reverseRecursive(word, index-1, reverse)
    
    
    
user_Input=input("Type a word and I will reverse by using recursive: ")
result = reverseRecursive(user_Input, len(user_Input)-1)

print("".join(result))