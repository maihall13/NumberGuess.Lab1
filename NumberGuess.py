import random

#Have user pick a min number and validate
startNum = input("Enter a minimum number: ")
while startNum.isnumeric() == False:
    startNum = input("Please enter a minimum number: ")

#have user pick a max number and validate
endNum = input("Enter a maximum number: ")
while endNum.isnumeric() == False:
    endNum = input("Please enter a maximum number: ")

#convert strings to integers
startNum = int(startNum)
endNum = int(endNum)

#Computer picks random number
randNum = random.randrange(startNum, endNum)
randNum = int(randNum)
#print(randNum)

#Ask usere to guess a random number
guessNum = input("Guess the random number: ")
while guessNum.isnumeric() == False:
    guessNum = input("Please guess the random number: ")
guessNum = int(guessNum)


#While the answer is not correct loop and give user clues
#until correct answer is guessed
while guessNum != randNum:
    if guessNum > randNum:
        guessNum = input("The number is too high. Guess again: ")
    else:
        guessNum = input("The number is too low. Guess again: ")

    while guessNum.isnumeric() == False:
        guessNum = input("Please guess the random number: ")
    guessNum = int(guessNum)

print("Congrats you got the number correct")