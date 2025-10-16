def maxminNum():

    numList=[int(i) for i in userInput]
    numList.sort()
    minmax = {"min": numList[0], "max": numList[len(numList)-1]}
        
        
    print("Max is: ", minmax["max"], " and min is ", minmax["min"])
    


userInput=input("Please type 5 numbers: ").split()
maxminNum()