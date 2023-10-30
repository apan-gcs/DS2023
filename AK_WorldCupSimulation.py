#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:51:26 2023

World Cup Final Simulation

 Throughout this simulation, you will play in the World Cup final. The decisions
you make in the game will impact the final result. Thank you for playing the game,
and good luck!

TODO
@author: alistairkiernan
"""


# Creating the print_slow function
from time import sleep
import random


def print_slow(text):
    "A function that prints one character at a time."
    for x in text:                    # Cycle through the text
        print(x, end='', flush=True)  # Print character, no new line
        sleep(0.02)                   # Delay between characters
    print()                           # New line
    sleep(0)                        # Delay after finishing the line
 
    
# Establishing the choose function to ensure that the user enters a valid input
def choose(valid_choices):
    for i in range(5):
        choice = input("Enter your choice: ")

        if choice in valid_choices:
            return choice
        else:
            print("That is not a valid input.")
    else:
        print("You are not permitted to continue playing this game.")


# Beginning of the game!
print_slow("Welcome to the World Cup Final Simulation!")

# User inputs
print_slow("What Country would you like to play for?")
country = input("Enter Country here: ")

print_slow("What Country would you like to play against?")
country_opposition = input("Enter Country here: ")


print_slow("What position would you like to play?")

print_slow("1:Attacker")
print_slow("2:Midfielder")
print_slow("3:Defender")
print_slow("4:Goalkeeper")


choice = choose(["1", "2", "3", "4"])


# Attacker Code
if choice == "1":
    
    print_slow("You start on the bench as a substitute.")
    print_slow("MINUTE 90: You are subbed on and your team are awarded a" 
               " penalty kick. The score is 1:1. Where do you shoot it?")
               
    print_slow("1:Left")
    print_slow("2:Right")
    print_slow("3:Middle")
   
    choice = choose(["1", "2", "3"])
    
    if choice == "1":
        print_slow(f"GOAL! You score and {country} wins the World Cup!")

    if choice == "2":
        print_slow(f"GOAL! You score and {country} wins the World Cup!")
    
    if choice == "3": 
        print_slow("SAVED BY THE GOALIE! The manager is pissed and" 
                   f"you are substituted back off of the field.")
        print_slow(f"{country} loses to {country_opposition} 2-1!")


# Midfielder Code
elif choice == "2":
    print_slow("MINUTE 8:You get injured due to a nasty tackle from"
               f" {country_opposition}'s center back. You are forced"
               " to watch the game from the sidelines, but you are victorious"
               f" as {country} wins 4-2!")

# Defender Code
elif choice == "3":
    print_slow(f"MINUTE 21: An {country_opposition} attacker is dribbling"
               " your way. Do you want to slide tackle him or try to"
               " push him off of the ball?")

    print_slow("1:Risky Slide Tackle")
    print_slow("2:Push him off of the ball")

    choice = choose(["1", "2"])

    # Random aspect of the game. 50-50 Tackle.
    if choice == "1":
        random.randint(1, 2)
        roll= random.randint(1, 2)
        if roll == 1:
            print_slow("You lunge in with a poorly timed tackle and it goes to a"
                        f" penalty kick. {country_opposition} scores")
            
            print_slow("The manager is furious and subs you off of the field."
                       f" {country} loses to {country_opposition} 1-0.") 
        
        if roll == 2:
            print_slow("You successfully slide tackle him off of the ball."
                   " The manager applauds the precision of your tackle.")

            print_slow("MINUTE 33: You are given the ball near half field."
                       " Would you like to play a through ball into the wingers?"
                       " Or, Cross the ball into the box?")
                       
            print_slow("1:Play a throughball into the Wingers")
            print_slow("2:Cross the ball into the box")

            choice = choose(["1", "2"])

            if choice == "1":
                print_slow("You play a ball to the wingers but it is not a good pass."
                           " The ball goes out of bounds and the manager subs you out"
                           " and you witness your team lose 3:1")

            if choice == "2":
                print_slow("You play a fantastic ball into the box resulting"
                           f" in a goal for {country}. You continue to play well and"
                           f" {country} beats {country_opposition} 2-0")
    
    if choice =="2":
        print_slow("You try to push him off of the ball but he" 
                    " accelerates and dribbles past you. He shoots from"
                    f" inside the box and scores. {country}:0 {country_opposition}: 1")

        print_slow("MINUTE 33: You are given the ball near half field."
                   " Would you like to play a through ball into the wingers?"
                   " Or, Cross the ball into the box?")
 
        print_slow("1:Play a throughball into the Wingers")
        print_slow("2:Cross the ball into the box")


        choice = choose(["1", "2"])


        if choice == "1":
            print_slow(f"You play a ball to the wingers but it is not a"
                       " good pass. The ball goes out of bounds and the manager"
                       f" subs you out and you witness {country} lose"
                       f" to {country_opposition} 3:1")

        if choice == "2":
            print_slow(" You cross the ball in but it is a poor cross"
                       " and the ball goes out of bounds. The manager subs"
                       " you out and you witness your team lose 2:1")

# Goalkeeper Code
elif choice == "4":
    print_slow(f"MINUTE 5: {country_opposition}'s striker takes a shot on goal."
               "Do you want to dive left or right for the ball?")
            
    print_slow("1:Dive Left")

    print_slow("2:Dive Right")

    choice = choose(["1", "2"])

if choice == "1": 
    print_slow("You pick the correct direction and save the shot")
        
    print_slow("MINUTE 30:The ball goes out for a goal kick. Do you want to play it long or short?")
        
    print_slow("1:Play it long")
    print_slow("2:Play it short") 

    choice = choose(["1","2"])

        
    if choice == "1":
        print_slow(f"You play the ball long and your striker scores. {country} leads 1-0")
        print_slow(f"MINUTE 65: The striker for {country} scores again. {country} leads 2-0")
        print_slow(f"MINUTE 90: {country_opposition} is awarded a penalty."
                       "Which way would you like to dive to save it?")
            
        print_slow("1:Dive Left")
        print_slow("2:Dive Middle")
        print_slow("3:Dive Right")

        choice = choose(["1", "2", "3"])

        if choice == "1":
            print_slow(f"You dived the wrong way! But {country} still wins 2-1")
        
        if choice == "2": 
            print_slow(f"You dived the wrong way! But {country} still wins 2-1")

        if choice == "3":
                print_slow(f"You Save it. {country} wins 2-0!")
        
    if choice == "2":
         
        print_slow("You decide to play it short and your team loses possession" 
                       f" in a dangerous area. {country_opposition} scores. The score is 1-0")
                   
        print_slow(f"MINUTE 65: The striker for {country} scores. The game is tied at 1:1")
        
        print_slow(f"{country_opposition} is awarded a penalty in the 90th minute."
                       " Which way would you like to dive to save it?")

        print_slow("1:Dive Left")
        print_slow("2:Dive Middle")
        print_slow("3:Dive Right")

        choice = choose(["1", "2", "3"])

        if choice == "1":
            print_slow(f"You dived the wrong way! {country_opposition} wins 2-1")
        
        if choice == "2": 
            print_slow(f"You dived the wrong way! {country_opposition} wins 2-1")
            
        if choice == "3": 
            print_slow(f"You saved it!. {country} counterattacks and scores. "
                           "You win 2-1!")
    
        if choice == "2": 
            print_slow(f"You dive the wrong way and {country_opposition} leads 1-0")
            print_slow("MINUTE 30:The ball goes out for a goal kick. Do you want to "
                   "play it long or short?")
        
            print_slow("1:Play it long")
            print_slow("2:Play it short")
        
            choice = choose(["1","2"])
        
            if choice == "1":
                print_slow ("You play the ball long and your striker scores." 
                        "The game is now tied at 1-1")
                print_slow(f"MINUTE 65: The striker for {country} scores again."
                       "{country} leads 2-1")
                print_slow("The game ends and {country} has won.The final score is"
                       F"{country}: 2 {country_opposition}: 1")

            if choice == "2":
                print_slow("You decide to play it short and your team loses possession"
                      f" in a dangerous area. {country_opposition} scores. The score is now 2-1")
                      
                print_slow(f"MINUTE 90: {country_opposition} is awarded a penalty." 
                      " Which way would you like to dive to save it?") 
                     
                print_slow("1:Dive Left")
                print_slow("2:Dive Middle")
                print_slow("3:Dive Right")

                choice = choose(["1", "2", "3"])


                if choice == "1":
                    print_slow(f"You dived the wrong way! {country_opposition} wins 3-1")
                      
                if choice == "2":
                    print_slow(f"You dived the wrong way! {country_opposition} wins 3-1")
                          
                if choice == "3":
                    print_slow(f"You saved it! But {country_opposition} still wins 2-1!")