def countup(i,n):
  
    if i>n:
        print("That is the end!")
    else:
        print(i)
        countup(i+1,n)
        
userInput=int(input("Type the number and I will count up to that number: "))
countup(0, userInput)
