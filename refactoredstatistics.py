# This is a Python program for performing simple statistical operations on a 
# list of numbers.
# 
# This class is part of ISE (ISAD1000/5004) Modularity worksheet.
# 
# Make sure you're up-to-date with your programming unit!
#
# (Note: yes, Python has built-in shortcuts for a lot of the code here, 
# like sum(), min() and max(), but just say for the sake of the exercise that 
# we want to implement these operations ourselves.)

import math
from statisticsclass import Statistics

def mySum(sumList):
    """Calculates the sum of the numbers in the sumList variable."""
    result = 0.0
    for i in range(sumLength):
        result += sumList[i]
        
    return result

    
def mean(sumList):
    """Calculates the mean (average) of the numbers in the sumList variable."""
    theSum = mySum(sumList)
    return theSum / len(sumLength)


def variance(dataList):    
    """
    Calculates the variance of a list of numbers. Stores the result in the 
    varianceResult variable.
    """
    sumSquares = 0.0
    average = mean(dataList)
        
    for i in range(len(dataList)):
        difference = dataList[i] - average
        sumSquares += difference * difference
        
    varianceResult = sumSquares / (len(dataList) - 1)
    return varianceResult
    

def stddev(dataList):    
    """Calculates the standard deviation of a list of numbers."""
    varianceResult = variance(dataList)        
    return math.sqrt(varianceResult)


def minmax(dataList, calcMax):
    """
    Determines either the lowest or highest of a list of numbers. The calcMax 
    parameter says whether to calculate the maximum or minimum. If calcMax is 
    True, the maximum is found; otherwise, the minimum is found.
    """
    result = dataList[0]
        
    if calcMax:
        # Find the highest value in the list.
        for i in range(len(dataList)):
            element = dataList[i]
            if result < element:
                # If the next element is higher than the maximum so far, 
                # update the maximum.
                result = element
    else:
        # Find the lowest value in the list.
        for i in range(len(dataList)):
            element = dataList[i]
            if result > element:
                # If the next element is lower than the minimum so far, 
                # update the minimum.
                result = element

    return result
    
    
    
def product(op, dataList):
    """
    Calculates the product of a list of numbers, and optionally performs an
    additional operation. If op is 1, we calculate the "geometric mean". If op 
    is 2, we find the log of the product. Otherwise, we just return the raw 
    product.
    """

    product = 1.0
    for i in range(len(dataList)):
        product *= dataList[i]

    if op == 1:
        result = pow(product, 1.0 / len(dataList))

    elif op == 2:
        result = math.log(product)

    else:
        result = product            

    return result

        
if __name__ == "__main__":
    # Input list length
    listLength = int(input("Enter length of list: "))
    
    # Create new list and input each element
    dataList = []
    for i in range(listLength):
        nextNumber = float(input("Enter real number: "))
        dataList.append(nextNumber)
    
    operation = input("Select a calculation to perform: ")
    
    # Determine which operation was chosen, and perform it.
    if operation == "min":
        result = minmax(dataList, False)
        
    elif operation == "max":
        result = minmax(dataList, True)
        
    elif operation == "sum":
        result = mySum(dataList)
        
    elif operation == "mean":
        result = mean(dataList)
        
    elif operation == "variance":
        result = variance(dataList)
        
    elif operation == "stddev":
        result = stddev(dataList)
        
    elif operation == "product":
        result = product(0, dataList)        
        
    elif operation == "geommean":
        result = product(1, dataList)
        
    else:
        print("Unrecognised operation \"" + operation + "\".")
        result = 0.0
        
    print("Result = " + str(result))

