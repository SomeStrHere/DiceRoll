# Program to simulate the role of dice and output a random number between a range from 1 to x

import random

def userInput() :

    maxInt = int(input('How many number of sides does the dice have? '))

    return(diceRoll(maxInt))

def diceRoll(maxInt) :

    diceResult = random.randint(1, maxInt)

    return(diceResult)

def main() : 

    output = userInput()

    print("This is the result: ", output )

if __name__ == "__main__" :
    main()



