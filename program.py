inventory = []

from time import sleep
import sys


def printFancy(text):
    printText = ""

    print("\n\n--------------------\n\n")

    for letter in text:
        printText += letter
        #print("---------------------------")
        print(letter, end='', flush=True) 
        #sys.stdout.flush()
        #print("---------------------------")
        sleep(0.035)
    print("\n\n--------------------")

    GoFurther = input("Continue ➡️   ")

"""def printFancy(text):
    printText = ""

    for letter in text:
        printText += letter
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n---------------------------")
        print(printText)
        print("---------------------------\n\n\n\n\n")
        sleep(0.025)

    GoFurther = input("input enter to continue... ")
"""

printFancy("You awake after a long nights restful sleep 😐.")
printFancy("Mysteriously, you find yourself in a hamsters body, whereas you're leaping over fields in the hunt for de golden dandilion")
printFancy("You flinch and freeze in your thought, do you decide to look at the [Dandilion] or take a closer look at your mystical [Hamster] body?")
choice = input("What do you choose? ").lower()

if "hamster" in choice:
    print("In this moment you decide to admire your fascinatingly stunning new fluffy body as you feel your desire for grass to grow stronger")
elif "dandilion" in choice:
    print("You scream on the inside, that being because you have a dandilion allergy.. Regardless you put it into your designated hamster bag")
    inventory.append("Dandilion")
else:
    print("You realize you aren't the best of spellers, but that's alright.")

print(inventory)