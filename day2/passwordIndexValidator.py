#!/usr/bin/python
import sys

# This is definitely naive
# Assuming properly formatted input here, probably shouldn't do that 
def validatePassword(line):
    # The following min/maxes are inclusive 
    dashSplitLine = line.split('-')
    spaceSplitLine = dashSplitLine[1].split(' ')

    firstIndex = int(dashSplitLine[0])
    secondIndex = int(spaceSplitLine[0])
    specialChar = spaceSplitLine[1][0] 
    password = spaceSplitLine[2]
    
    # Check the two indices and XOR them
    # Exactly one of the two indices can contain the special char
    # Note: Indices are 1-indexed, so subtract 1 from them 
    indexOneSpecialChar = password[(firstIndex - 1)] == specialChar
    indexTwoSpecialChar = password[(secondIndex - 1)] == specialChar 
    return indexOneSpecialChar ^ indexTwoSpecialChar

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
