#!/bin/python3
import random

#this dictionary contains all the jokes
jokes = {
    1: ["What did the 0 say to the 8?", "Nice belt!"],
    2: ["What do you call a pony with a sore throat?", "A little horse!"],
    3: ["what do you call somebody with no body and no nose?", "Nobody knows!"],
    4: ["How does a penguin build a house?", "Igloos it together!"],
    5: ["What does a house wear?", "A dress! (address)"],
    6: ["The shovel was a ground breaking invention!"],
    7: ["A lorry full of terrapins crashed into a van full of tortoises...", "It was a turtle disaster!"],
    8: ["How do you make antifreeze?", "Steal her blanket!"],
    9: ["My wife is on a tropical food diet so the house is full of fruit...", "It's enough to make a mango crazy!"],
    10: ["What did the buffalo say to his son when he left for school?", "Bison!"],
    11: ["Did you hear about the guy who had his left side cut off?", "He's all right now!"],
    12: ["If prisoners could take their own mug shots, they'd be called cell-fies!"],
    13: ["An invisible man married an invisible woman...", "Their kids were nothing to look at either!"],
    14: ["I heard there is a new shop called Moderation...", "They have everything in there"],
    15: ["I gave all my batteries away today...", "free of charge"],
    16: ["What did the clock say to time?", "Not on my watch you don't!"]
}

#selects a joke at random from the jokes dictionary
#the range of the random number is constrained to between 1 and the length of the joke dictionary
chosen_joke = jokes[random.randrange(1,(len(jokes)+1))]

#loops through telling each part of the chosen joke for as many parts as the chosen joke list contains
#so two parts jokes will pause for the user to press enter before revealing the punchline
#and single parts jokes will just display the whole joke and wait for the user to press enter before returning to the command prompt
count = 0
for x in chosen_joke:
     print (chosen_joke[count])
     input()
     count += 1