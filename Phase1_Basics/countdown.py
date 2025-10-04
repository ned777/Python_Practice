def countdown(n):
    if n==0:
        print("That is it!")
    else:
        print(n)
        countdown(n-1)

user_Input=int(input("Type a number: "))
countdown(user_Input)dd
    
