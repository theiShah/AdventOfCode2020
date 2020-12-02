#!/usr/bin/python
import sys

# This is definitely naive
# Assuming properly formatted input here, probably shouldn't do that 
def validatePassword(line):
    # The following min/maxes are inclusive 
    dashSplitLine = line.split('-')
    spaceSplitLine = dashSplitLine[1].split(' ')

    minCharCount = int(dashSplitLine[0])
    maxCharCount = int(spaceSplitLine[0])
    specialChar = spaceSplitLine[1][0] 
    password = spaceSplitLine[2]

    specialCharCount = 0
    for c in password: 
        if c == specialChar:
            specialCharCount += 1
    if specialCharCount >= minCharCount and specialCharCount <= maxCharCount: 
        return 1
    return 0 

def main():
    numValidPasswords = 0; 
    fileName = sys.argv[1]
    with open(fileName) as f:
        for line in f:
            numValidPasswords += validatePassword(line) 
    print(numValidPasswords)
    return 

if __name__ == "__main__":
    main()
