#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sophie Bernstein
10/23 
Intensive Data Science 2
Project - CYOA Game
Text-Based game where the user has to make decisions to try to escape a room.
"""

from random import randint
from time import sleep


def print_slow(text):
    for x in text:
        print(x, end='', flush = True)
        sleep(0.02)
    print()
    sleep(0.5)


# this function gets called when the user makes a wrong decision and the game ends
def bad_ending():
    print_slow(f"You did not survive, {name} :(")
    
# this function gets called when they user reaches the end of a path without making
# any wrong choices, so they win
def good_ending():
    print_slow(f"You survived, {name} :)")
    

# this function checks if the user input is valid
def is_invalid(choice):
    if choice != '1' and choice != '2':
        print()
        print_slow(f"That's not an option, {name}! Try again!")
        print()
        
# this function print text with spaces on each surrounding row
def print_space(text):
    print()
    print(text)
    print()
   
points = 0
def my_points():
    if points >= 3:
        print_slow(f"You got {points} points! Congrats, you won!")
    else:
        print_slow(f"You got {points} points. You did not win.")

first = True    
first_correct = False
venting = False
chips = False
lock = False
random = False


name = input("Welcome to the game! What is your name? ")
print_slow(f"Hi, {name}!")
print_slow("You wake up in an empty room with no decorations or windows, just a fleurescent light above you. You immediately attempt to open the door, but discover it is locked.")
print_slow(f"If you are able escape with three points, you win the game! (points = {points})")


# first question every user gets, if they choose to try to escape (1), they move 
# on to the next question. if they choose to give up (2) they are stuck and have a bad ending
while first:
    first_choice = input("Do you: 1. try to escape (press 1 key) or 2. immediately give up (press 2 key): ")
    if first_choice == '1':
        points += 1
        print_slow(f"Good choice, {name}!")
        print_space(f"| +1 points! (points = {points}) |")
        first = False
        first_correct = True
    elif first_choice == '2':
        print_slow("You are stuck there forever!")
        print_space(f"| +0 points! (points = {points}) |")
        first = False
        bad_ending()
        my_points()
    else: 
       is_invalid(first_choice)
        
# question if they try to escape. if they choose to vent (1), they get asked left 
# or right, if they choose lock (2), they get asked crying or guessing
while first_correct:
    second_choice = input("You look around the room for any ways to get out, and you spot a vent. Do you: 1. climb through the vent (press 1 key) or 2. try to pick the lock on the door (press 2 key): ")
    if second_choice == '1':
        points += 1
        print_slow("You made it into the vent!")
        print_space(f"| +1 points! (points = {points}) |")
        first_correct = False
        venting = True
    elif second_choice == '2':
        print_slow("You fail at picking the lock.")
        print_space(f"| +0 points! (points = {points}) |")
        first_correct = False
        lock = True
    else: 
        is_invalid(second_choice)


# question if they choose to vent. if they choose to go left (1), they get a bad ending
# if they choose to go right (2), they get asked about chips
while venting:
    vent_choice = input("You've been successfully crawling for a few minutes, but you don't really know where you're headed. Them, the path diverges! Do you crawl left (press 1 key) or right? (press 2 key): ")
    if vent_choice == '1':
        print_slow("You get attacked by a feral mouse!")
        print_space(f"| +0 points! (points = {points}) |")
        venting = False
        bad_ending()
        my_points()
    elif vent_choice == '2':
        print_slow("You continue crawling, and see a bag of potato chips. You feel your stomach growl and wonder if you should take the chance and eat it.")
        venting = False
        chips = True
    else: 
        is_invalid(vent_choice)
        
     
# question if they choose to go right in the vent. if they choose to eat the chips (1),
# they get good ending. if they choose not to (2), they get bad ending
while chips:
    chip_choice = input("Do you eat one: 1. Yes (press 1 key) or 2. No (press 2 key): ")
    if chip_choice == '1':
        points += 1
        print_slow("The chips are super delicious, and a few minutes later you reach the exit!")
        print_space(f"| +1 points! (points = {points}) |")
        chips = False
        good_ending()
        my_points()
    elif chip_choice == '2':
        print_slow("You collapse from hunger.")
        print_space(f"| +0 points! (points = {points}) |")
        chips = False
        bad_ending()
        my_points()
    else: 
        is_invalid(chip_choice)
       

# question if they choose to try to pick the lock. if they choose to cry (1), tey get a bad
# ending. if they choose to guess random numbers (2), they get random number generator
while lock:
    lock_choice = input("Do you: 1. Start crying (press 1 key) or 2. Try to guess the code on the door (press 2 key): ")
    if lock_choice == '1':
        print_slow("You are too sad to keep trying, so you give up.")
        print_space(f"| +0 points! (points = {points}) |")
        lock = False
        bad_ending()
        my_points()
    elif lock_choice == '2':
        points += 1
        print_slow("You use a number generator for guesses.")
        print_space(f"| +1 points! (points = {points}) |")
        lock = False
        random = True
    else: 
       is_invalid(lock_choice)
    
   
# WHY ISNT THIS WHILE LOOP WORKING???

# question if they choose to guess random numbers. if the randomly generated number is even,
# they get a good ending. if its odd, they get a bad ending
while random:
    random_choice = input("Return to get a randomly generated guess (you have five guesses): ")
    x = 1
    while x <= 4:
        random_number = randint(1000,9999)
        print(f"Guess {x} is: {random_number}")
        if random_number%2 == 0:
            points += 1
            print_slow("Wow, you guessed correctly!")
            print_space(f"| +1 points! (points = {points}) |")
            good_ending()
            my_points()
            break
        else:
            try_again = input("That number is incorrect! Return to generate again: ")
            x += 1
    else:
        fifth_number = randint(1000,9999)
        print(f"Guess 5 is: {fifth_number}")
        if fifth_number%2 == 0:
            points += 1
            print_slow("Phew, you guessed correctly!")
            print_space(f"| +1 points! (points = {points}) |")
            good_ending()
            my_points()
        else:
            print_slow("That number is incorrect!")
            print_space(f"| +0 points! (points = {points}) |")
            bad_ending()
            my_points()
    random = False