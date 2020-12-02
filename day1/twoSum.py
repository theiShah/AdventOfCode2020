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
    for val in expenseReport:
        if val in remainderDict:
            answer = val * remainderDict[val]
            print(answer)
            return
    print("No value found!") 

if __name__ == "__main__":
    main()
