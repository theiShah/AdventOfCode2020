#!/usr/bin/python
import sys

twoSumValue = 2020

def main(): 
    fileName = sys.argv[1]
    expenseReport = []
    with open(fileName) as f:
        for line in f:
            expenseReport.append(int(line))
    # Now run a two sum algo
    remainderDict = {}
    for val in expenseReport:
        remainder = twoSumValue - val
        remainderDict[remainder] = val
    # Difference is we loop through twice
    # TODO Search for a more efficient way to do this 
    for firstVal in expenseReport:
        for secondVal in expenseReport:
            sumOfVals = firstVal + secondVal; 
            if sumOfVals in remainderDict:
                answer = firstVal * secondVal * remainderDict[sumOfVals]
                print(answer)
                return
    print("No value found!") 

if __name__ == "__main__":
    main()
