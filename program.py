inventory = []

from time import sleep
import sys


def fancyText(text):
    for letter in text:
        print(letter, end='', flush=True) 
        sleep(0.025)


def sarcasmText(text):
    capital = False
    for letter in text:
        if capital == False:
            letter = letter.lower()
            capital = True
            
        else:
            letter = letter.upper()
            capital = False
           
        print(letter, end='', flush=True) 
        sleep(0.025)


def printSarcasm(text):
    print("\n\n--------------------\n\n")
    sarcasmText(text)
    print("\n\n--------------------")

    GoFurther = input("Continue ➡️   ")

def printFancy(text):
    #printText = ""

    print("\n\n--------------------\n\n")
    fancyText(text)
    print("\n\n--------------------")

    GoFurther = input("Continue ➡️   ")

def inputFancy(text,question):
    print("\n\n--------------------\n\n")
    fancyText(text)
    print("\n\n--------------------")

    return input(question)

def getItem(text,item):
    print("\n\n--------------------\n\n")
    fancyText(text)
    print()
    sleep(0.5)
    inventory.append(item)
    itemText = f"// You Aquired the Item: {item}! //"
    fancyText(itemText)
    print("\n\n--------------------")



printFancy("You awake after a long nights restful sleep 😐.")
printSarcasm("Mysteriously, you find yourself in a hamsters body, whereas you're leaping over fields in the hunt for the golden dandilion")
choice = inputFancy("You flinch and freeze in your thought, do you decide to look at the [Dandilion] or take a closer look at your mystical [Hamster] body?","What do you choose? ").lower()


if "hamster" in choice:
    fancyText("In this moment you decide to admire your fascinatingly stunning new fluffy body as you feel your desire for grass to grow stronger")
elif "dandilion" in choice:
    getItem("You scream on the inside, that being because you have a dandilion allergy.. \nRegardless you put it into your designated hamster bag","Dandilion")
else:
    fancyText("You realize you aren't the best of spellers, but that's alright. \nYou move onwards...")