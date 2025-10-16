def vowelCounter():
    vowel="aeiou"
    counter=[i for i in userInput if i in vowel]
    print(len(counter))

userInput=input("Type a word or sentence and I will count how many vowels are there:").lower()
vowelCounter()