def sum_And_Average():
    total=0
    
    for i in user_Input:
        total+=int(i)
        
    avg=total/(len(user_Input))
    print("Sum: ", total, " Average: ", avg)
        
        
        
          
      
user_Input=(input("Please type a few numbers to calculate the sum and average: ")).split()
sum_And_Average()