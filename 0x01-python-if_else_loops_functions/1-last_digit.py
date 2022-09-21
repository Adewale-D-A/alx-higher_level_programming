#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
convertedDigit = int(str(number)[len(str(number))-1]) 
if convertedDigit > 5 and number > 0:
    print(f"Last digit of {number} is {convertedDigit} greater than 5")
elif convertedDigit == 0:    
    print(f"Last digit of {number} is {convertedDigit} and is 0")
else:    
    print(f"Last digit of {number} and is -{convertedDigit} less than 6 and not 0")
