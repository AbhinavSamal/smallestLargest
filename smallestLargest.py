num = [1,4,7,10,17,13,18,15,30,45,19,79,58,87,194,907,721.34,56,4,7,10,0]

def smallestNumber():
    minNumber = num[0]
    for i in range(0, len(num)):
        if num[i] < minNumber:
            minNumber = num[i]
    print(minNumber)

def largestNumber():
    maxNumber = num[0]
    for i in range(0, len(num)):
        if num[i] > maxNumber:
            maxNumber = num[i]
    print(maxNumber)

smallestNumber()
largestNumber()
