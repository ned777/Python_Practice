def palindrome_Recursive(user_Input, index, reverseWord=None):
    if reverseWord is None:
        reverseWord = []
        
        
    if index<0:
        reservedString = "".join(reverseWord)
        if  reservedString == user_Input:
            print("It is palindrome!")
        else:
            print("It is not palindrome!")
    else:
        reverseWord.append(user_Input[index])
        return palindrome_Recursive(user_Input, index-1, reverseWord)
    
    
user_Input=input("Type of your word: ").lower()
result = palindrome_Recursive(user_Input, len(user_Input)-1)

