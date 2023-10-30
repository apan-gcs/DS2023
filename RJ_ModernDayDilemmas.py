#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:10:20 2023

@author: ronanjohnson
"""
#Modern Day Dilemmas
#In this game, you have to deal with common day modern dilemmas. As an airline pilot with 
#a lot of responsibility on your shoulders, how will you handle the pressure?

#Ronan Johnson
#Data Science 2
#10/26/23"












from time import sleep
import random

def print_slow(text):
    """A function that prints one character at a time."""
    for x in text:                    # Cycle through the text
        print(x, end='', flush=True)  # Print character, no new line
        sleep(0.02)                   # Delay between characters
    print()                           # New line
    sleep(0.5)                        # Delay after finishing the line


def choose(valid_choices):
    """
    Prompts the user to enter one of several valid choices,
    where valid_choices is a list of desired values.
    e.g. choose(["1", "2"])
    """
    
    for i in range(5):
        choice = input("Enter your choice: ")
        if choice in valid_choices: 
            return choice 
        else:
            print("You're choice was not an acceptable answer")


name = input("Firstly, simple question, what is your name?  ")

print_slow(f"Hello {name}, right now you are flying a plane that has THE president on it."
           " You recieved a phone call from Putin, saying he has 100 million dollars,"
           " with your name on it. If you simply crash the plane, you get the money, but it also has FBI secret agents on it."
           " Are you crashing the plane, or telling the offcicers? enter one of the following numbers")
print_slow("1: Crash it")
print_slow("2: Tell the police")


choice = choose(["1", "2"])





if choice == "1":
        print_slow("You choose to crash the plane.")
        print_slow("Quick! You have to make a vital decision towards your survival!"
                  " You are currently flying over Ukraine, an ally of the president. Or...do"
                 " you change courses to Russia, who will support your escape...however you "
                 "take the risk of the FBI onboard of finding out.")
        print_slow("1: Ukraine")
        print_slow("2: Russia")           
        
        choice = input("Enter your choice.")
        
        if choice == "1":
                print_slow(f"you crash the plane in Ukraine, yet somehow everyone survives. {name} You're now running from the FBI and President. Go in a cave or forest to escape.")
                print_slow("1: Cave")
                print_slow("2: Forest") 
            
                choice = input("Enter your choice.")
                
                if choice == "1":
                    print_slow(f" Sorry, {name}, looks like its your time to die :(. You got caught in"
                               " the cave and shot to death. The end. :( :(")
                elif choice == "2":
                    coinflip = random.randint(1, 2)
                    if coinflip == "1":
                        print_slow(" Wow, you made it into the forest! uh oh! you come across a bear! Fight or Flight?")
                        print_slow("1: fight")
                        print_slow("2: flight")    
                        choice = input("Enter your choice.")
                        if choice == "1":
                            print_slow("you didnt know about the power inside of you! YHou beat the crap out of the bear.You"
                                       " have now esacped! congratulations! you're 100 million dollars richer now.")
                        elif choice == "2":
                            print_slow("you slip on a banana peel and split your head open 😮. The end. :(")
        
        
        elif choice == "2":
            print_slow("You crashed it! Now Putin can hook you up. Congratulatoins! You won!.")
       
        
        
        
elif choice == "2":
    print_slow("You choose to tell the FBI")
    print_slow("After telling the agents aboard, they immediately tell you to make a u turn back towards america.")
    print_slow("Putin learns of your treachery and starts shooting missiles at you, taking out your left engine! With the plain spinning down, do you aim for water near or land in the forest.")
    print_slow("1: water")
    print_slow("2: land")
    
    choice = input("enter your choice.")
    if choice == "1":
        print_slow("By landing in the water, you have survived. However, there are now russian infantry hunting you down. In Ukrainian territory...")
        print_slow("You need to alert ukrainian forces of your location. Use a flair or seek them out?")
        print("1: Flair")
        print("2: seek them out")
        if choice == "1":
                print_slow("By using a flair, you have now also attracted the attention of the russians. They beat the ukrainians and killed you and the president. The end" )
        elif choice == "2":
                print_slow("By deciding to find your allies, you stumble across the Ukranian exploration party of the crash! They save you of your predicament and you can now make it home safe.")
    elif choice == "2":
        print_slow("Oh no! the tress are unable to slow down the fall of the plane, and it explodes!!! You die...The end :(")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    