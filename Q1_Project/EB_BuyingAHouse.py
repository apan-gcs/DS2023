#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ethan Buery
Intensive Data Science 2
Q1 Project: Text-Based Game
10/26/23
"""
import sys


from time import sleep
import random

def print_slow(text):
    for x in text:                    
        print(x, end='', flush=True)  
        sleep(0.04)                   
    print()                           
    sleep(1)                        

def choose(valid_choices):
   
    for i in range(2):
        choice = input("What do you choose? ")
        if choice in valid_choices: 
            return choice 
        else:
            print("Hmmmm... That wasnt a choice. ")




name = input ("Good day future home Owner! Would you mind giving me your name? ")

print_slow(f"Good day {name}! In order to buy a house today . . . You will have to play a game!"
           "The number you role dictates which house you are allowed to buy. You will roll a 9 sided die. "
           "Roll 1-3, you can buy the inexpenisve house. Roll 4-6, you can buy the middle priced house. Roll 7-9, you can buy the most expensive house.")

print_slow(f"{name}, Are you ready to roll?" )

print_slow("1: Yes")
print_slow("2: No")


choice = choose(["1", "2"])

if choice == "1":
        
        dice_roll = random.randint(1, 9)
        
        print(f"You rolled a {dice_roll}!")
# First Roll Group
        if dice_roll in [1, 2, 3]:
            
            print_slow("You get to pick out of the worst houses.")
            print_slow("Do you want a barn or a Haunted House?")
            print_slow("1: Barn")
            print_slow("2: Haunted House")
            choice = input("What would you like?")
#   Barn
            if choice == "1":
                print_slow("Do you want a Roof or a Door? ")
                print_slow("1:Roof")
                print_slow("2:Door")
                choice = input("What would you like? ")
#       Roof                
                if choice == "1":
                    print_slow(f"Congratulations {name} on your new Barn! ")
                    sys.exit()
#       Door                     
                elif choice == "2":
                    print_slow(f"Congratulations {name} on your new Barn! ")
                    sys.exit()


#   Haunted House
            elif choice == "2":
                print_slow("Do you want a Roof or a Door?")
                print_slow("1:Roof")
                print_slow("2:Door")
                choice = input("What would you like? ")
#       Roof                
                if choice == "1":
                    print_slow(f"Congratulations {name} on your new home! ")
                    sys.exit()
#       Door                    
                elif choice == "2":
                    print_slow(f"Congratulations {name} on your new home! ")
                    sys.exit()
                    
       
        
       
        
       
        
# Second Roll Group       
        elif dice_roll in range (4,7):
            
            print_slow("You get to pick out of the medium houses.")
            print_slow("Do you want a Suburban home, Mobile Home or Apartment?")
            print_slow("1: Suburban Home")
            print_slow("2: Mobile Home")
            print_slow("3: Apartment")
            choice = input("What would you like? ")
#   Suburban Home
            if choice == "1":
                print_slow("Do you want a Roof or a Door?")
                print_slow("1:Roof")
                print_slow("2:Door")
                choice = input("What would you like? ")
#       Roof                
                if choice == "1":
                    print_slow("Do you want a Backyard or a Porch?")
                    print_slow("1:Backyard")
                    print_slow("2:Porch")   
                    choice = input("What would you like? ")
                
#           Backyard                    
                    if choice == "1":
                        print_slow(f"Congratulations {name} on your new Suburban home! ")
                        sys.exit()
#           Porch                        
                    elif choice == "2":
                            print_slow(f"Congratulations {name} on your new Suburban home! ")
                            sys.exit()
                        
#       Door                     
                elif choice == "2":
                    print_slow("Do you want a Backyard or a Porch?")
                    print_slow("1:Backyard")
                    print_slow("2:Porch")
                    choice = input("What would you like? ")
                    
#            Backyard                    
                    if choice == "1":
                        print_slow(f"Congratulations {name} on your new Suburban home! ")
                        sys.exit()
#           Porch                        
                    elif choice == "2":
                            print_slow(f"Congratulations {name} on your new Suburban home! ")
                            sys.exit()    
                        


#   Mobile Home
            if choice == "2":
                print_slow("Do you want a Roof or a Door?")
                print_slow("1:Roof")
                print_slow("2:Door")
                choice = input("What would you like? ")
#       Roof                
                if choice == "1":
                    print_slow("Do you want a Backyard or a Porch?")
                    print_slow("1:Backyard")
                    print_slow("2:Porch")   
                    choice = input("What would you like? ")
                
#           Backyard                    
                    if choice == "1":
                        print_slow(f"Congratulations {name} on your new Mobile home! ")
                        sys.exit()
#           Porch                        
                    elif choice == "2":
                            print_slow(f"Congratulations {name} on your new Mobile home! ")
                            sys.exit()
                        
#       Door                     
                elif choice == "2":
                    print_slow("Do you want a Backyard or a Porch?")
                    print_slow("1:Backyard")
                    print_slow("2:Porch")
                    choice = input("What would you like? ")
                    
#            Backyard                    
                    if choice == "1":
                        print_slow(f"Congratulations {name} on your new Mobile home! ")
                        sys.exit()
#           Porch                        
                    elif choice == "2":
                            print_slow(f"Congratulations {name} on your new Mobile home! ")
                            sys.exit()    
        


#   Apartment
            if choice == "3":
                print_slow("Do you want a Roof or a Door?")
                print_slow("1:Roof")
                print_slow("2:Door")
                choice = input("What would you like? ")
#       Roof                
                if choice == "1":
                    print_slow("Do you want a Backyard or a Porch?")
                    print_slow("1:Backyard")
                    print_slow("2:Porch")   
                    choice = input("What would you like? ")
                
#           Backyard                    
                    if choice == "1":
                        print_slow(f"Congratulations {name} on your new Mobile home! ")
                        sys.exit()
#           Porch                        
                    elif choice == "2":
                            print_slow(f"Congratulations {name} on your new Mobile home! ")
                            sys.exit()
                        
#       Door                     
                elif choice == "2":
                    print_slow("Do you want a Backyard or a Porch?")
                    print_slow("1:Backyard")
                    print_slow("2:Porch")
                    choice = input("What would you like? ")
#            Backyard                    
                    if choice == "1":
                        print_slow(f"Congratulations {name} on your new Mobile home! ")
                        sys.exit()
#           Porch                        
                    elif choice == "2":
                            print_slow(f"Congratulations {name} on your new Mobile home! ")
                            sys.exit()    














# Third Roll Group            
        
        elif dice_roll in range (7,10):
             new_roll = random.randint(1, 2)
             print("In order to buy the most expensive house, you must guess the correct number. The number is either 1, or 2. You have one guess")
             guess = input("What's your guess?: ")
             if guess != new_roll:
                 print_slow("GAME OVER. Sorry!")
             else:
                 print("You guessed correct!")
                 print_slow("You get to pick out of the expensive houses.")
                 print_slow("Do you want a Mansion, Castle or Skyscraper?")
                 print_slow("1: Mansion")
                 print_slow("2: Castle")
                 print_slow("3: Skyscraper")
                 choice = input("What would you like? ")    
#   Mansion
                 if choice == "1":
                     print_slow("Do you want a Pool or a Sauna?")
                     print_slow("1:Pool")
                     print_slow("2:Sauna")
#       Pool                
                     if choice == "1":
                         print_slow("Do you want a Beach View or a Lake View?")
                         print_slow("1:Beach")
                         print_slow("2:Lake")   
                         choice = input("What would you like? ")
                     
#           Beach                    
                         if choice == "1":
                             if choice == "1":
                                 print_slow("Do you want Speakers or LED lights?")
                                 print_slow("1:Speakers")
                                 print_slow("2:LED lights")   
                                 choice = input("What would you like? ")           
 #Speakers                         
                                 if choice == "1":
                                     print_slow("Its time to throw a party at your new home! What music do you want to play?")
                                     print_slow("1:Jazz")
                                     print_slow("2:Heavy Metal")
                                     if choice == "1":
                                         print_slow("The party was great! Everyone loved the music! Enjoy your new homw!")
                                         sys.exit()
                                     elif choice == "2":
                                         print_slow("Oh no!! the Neighbors thought the music was too loud and called the police."
                                                    " Now you have to move out. GAME OVER!!")
                                         sys.exit()
# LED
                                 elif choice == "2":
                                     print_slow(f"Congratulations {name} on your new Mansion! ")
                                     sys.exit()
                                        
                                     
                                
                                     
#           Lake                        
                         elif choice == "2":
                                 if choice == "2":
                                     print_slow("Do you want Speakers or LED lights?")
                                     print_slow("1:Speakers")
                                     print_slow("2:LED lights")   
                                     choice = input("What would you like? ")           
     #Speakers                         
                                     if choice == "1":
                                         print_slow("Its time to throw a party at your new home! What music do you want to play?")
                                         print_slow("1:Jazz")
                                         print_slow("2:Heavy Metal")
                                         if choice == "1":
                                             print_slow("The party was great! Everyone loved the music! Enjoy your new homw!")
                                             sys.exit()
                                         elif choice == "2":
                                             print_slow("Oh no!! the Neighbors thought the music was too loud and called the police."
                                                        " Now you have to move out. GAME OVER!!")
                                             sys.exit()
    # LED
                                     elif choice == "2":
                                         print_slow(f"Congratulations {name} on your new Mansion! ")
                                         sys.exit()
#               LED lights                                     
                             
#       Sauna                     
                     elif choice == "2":
                         print_slow("Do you want a Beach View or a Lake View?")
                         print_slow("1:Beach")
                         print_slow("2:Lake")
                         choice = input("What would you like? ")
                         
#            Beach                    
                         if choice == "1":
                             print_slow(f"Congratulations {name} on your new Mansion! ")
                             sys.exit()
#           Lake                        
                         elif choice == "2":
                                 print_slow(f"Congratulations {name} on your new Mansion! ")
                                 sys.exit()    
                             
    
    
# #  Castle
                 if choice == "1":
                     print_slow("Do you want a Pool or a Sauna?")
                     print_slow("1:Pool")
                     print_slow("2:Sauna")
#       Pool                
                     if choice == "1":
                         print_slow("Do you want a Dungeon or a Tower?")
                         print_slow("1:Dungeon")
                         print_slow("2:Tower")   
                         choice = input("What would you like? ")
                     
# #          Dongeon                    
                         if choice == "1":
                             if choice == "1":
                                 print_slow("Do you want Speakers or LED lights?")
                                 print_slow("1:Speakers")
                                 print_slow("2:LED lights")   
                                 choice = input("What would you like? ")           
 #Speakers                         
                                 if choice == "1":
                                     print_slow("Its time to throw a party at your new home! What music do you want to play?")
                                     print_slow("1:Jazz")
                                     print_slow("2:Heavy Metal")
                                     if choice == "1":
                                         print_slow("The party was great! Everyone loved the music! Enjoy your new Castle!")
                                         sys.exit()
                                     elif choice == "2":
                                         print_slow("Oh no!! the Neighbors thought the music was too loud and called the police."
                                                    " Now you have to move out. GAME OVER!!")
                                         sys.exit()
# LED
                                 elif choice == "2":
                                     print_slow(f"Congratulations {name} on your new Castle! ")
                                     sys.exit()
                                        
                                     
                                
                                     
#           Tower                        
                         elif choice == "2":
                                 if choice == "2":
                                     print_slow("Do you want Speakers or LED lights?")
                                     print_slow("1:Speakers")
                                     print_slow("2:LED lights")   
                                     choice = input("What would you like? ")           
     #Speakers                         
                                     if choice == "1":
                                         print_slow("Its time to throw a party at your new home! What music do you want to play?")
                                         print_slow("1:Jazz")
                                         print_slow("2:Heavy Metal")
                                         if choice == "1":
                                             print_slow("The party was great! Everyone loved the music! Enjoy your new homw!")
                                             sys.exit()
                                         elif choice == "2":
                                             print_slow("Oh no!! the Neighbors thought the music was too loud and called the police."
                                                        " Now you have to move out. GAME OVER!!")
                                             sys.exit()
    # LED
                                     elif choice == "2":
                                         print_slow(f"Congratulations {name} on your new Mansion! ")
                                         sys.exit()
#               LED lights                                     
                             
#       Sauna                     
                     elif choice == "2":
                         print_slow("Do you want a Dungeon or a Tower?")
                         print_slow("1:Dungeon")
                         print_slow("2:Tower")
                         choice = input("What would you like? ")
                         
#            Dungeon                    
                         if choice == "1":
                             print_slow(f"Congratulations {name} on your new Castle! ")
                             sys.exit()
#           Tower                        
                         elif choice == "2":
                                 print_slow(f"Congratulations {name} on your new Castle! ")
                                 sys.exit()        
             
    
    
#   Skyscraper
                 if choice == "1":
                     print_slow("Do you want a Pool or a Sauna?")
                     print_slow("1:Pool")
                     print_slow("2:Sauna")
#       Pool                
                     if choice == "1":
                         print_slow("Do you want it in Shanghai or in New York?")
                         print_slow("1:Shanghai")
                         print_slow("2:New York")   
                         choice = input("What would you like? ")
                     
# #          Shanghai                    
                         if choice == "1":
                             if choice == "1":
                                 print_slow("Do you want Speakers or LED lights?")
                                 print_slow("1:Speakers")
                                 print_slow("2:LED lights")   
                                 choice = input("What would you like? ")           
 #Speakers                         
                                 if choice == "1":
                                     print_slow("Its time to throw a party at your new home! What music do you want to play?")
                                     print_slow("1:Jazz")
                                     print_slow("2:Heavy Metal")
                                     if choice == "1":
                                         print_slow("The party was great! Everyone loved the music! Enjoy your new Skyscraper!")
                                         sys.exit()
                                     elif choice == "2":
                                         print_slow("Oh no!! the Neighbors thought the music was too loud and called the police."
                                                    " Now you have to move out. GAME OVER!!")
                                         sys.exit()
# LED
                                 elif choice == "2":
                                     print_slow(f"Congratulations {name} on your new Skyscraper! ")
                                     sys.exit()
                                        
                                     
                                
                                     
#           New York                        
                         elif choice == "2":
                                 if choice == "2":
                                     print_slow("Do you want Speakers or LED lights?")
                                     print_slow("1:Speakers")
                                     print_slow("2:LED lights")   
                                     choice = input("What would you like? ")           
     #Speakers                         
                                     if choice == "1":
                                         print_slow("Its time to throw a party at your new home! What music do you want to play?")
                                         print_slow("1:Jazz")
                                         print_slow("2:Heavy Metal")
                                         if choice == "1":
                                             print_slow("The party was great! Everyone loved the music! Enjoy your new Skyscraper!")
                                             sys.exit()
                                         elif choice == "2":
                                             print_slow("Oh no!! the Neighbors thought the music was too loud and called the police."
                                                        " Now you have to move out. GAME OVER!!")
                                             sys.exit()
    # LED
                                     elif choice == "2":
                                         print_slow(f"Congratulations {name} on your new Skyscraper! ")
                                         sys.exit()
#               LED lights                                     
                             
#       Sauna                     
                     elif choice == "2":
                         print_slow("Do you want it in Shanghai or in New York")
                         print_slow("1:Shanghai")
                         print_slow("2:New York")
                         choice = input("What would you like? ")
                         
#            Shanghai                    
                         if choice == "1":
                             print_slow(f"Congratulations {name} on your new Skyscraper! ")
                             sys.exit()
#           New York                        
                         elif choice == "2":
                                 print_slow(f"Congratulations {name} on your new Skyscraper! ")
                                 sys.exit()









elif choice == "2":
    print("GAME OVER.")
    sys.exit()

             
             
             
             
             
             
             
             
             
             
             
             