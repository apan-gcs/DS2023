
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Itai Komoroff
Intensive Data Science II
October 26, 2023

Q1 Project CYOA
Mob Money Mayhem\

"""

import random
import sys
from time import sleep


def print_slow(text):
    # A function that prints one character at a time.
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
        choice = input("Enter  choice now: ")
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please try again.")
    else:  # Prompt for if user runs out of attempts
        print("Maximum attempts. GAME OVER!")
        sys.exit()


print_slow("Welcome to Mob Money Mayhem: The World's "
           "greatest Heist Video game! "
           "Would you like to begin playing?")
print_slow("1: Begin Playing")
print_slow("2: Do Not Play")

choice = choose(["1", "2"])

if choice == "1":  # They have decided to play
    print("Welcome to Mob Money Mayhem. We will now begin.")
    print_slow("You owe 40 grand to the New York City "
               "Mafia. You must pay "
               "them back by the end of the "
               "month or they will murder you. You Must devise a plan "
               "to make the 40 grand and pay them back "
               "by the end of the month. How will you make back the money?")
    print("1: Steal Watches and sell them for a profit.")  # 1 path of game
    print("2: Become an online media guru...")             # 2nd path of game

    choice = choose(["1", "2"])

    if choice == "1":  # Decide to steal watches
        print_slow("Good Choice! Which type of watches do you"
                   " plan on stealing?")
        print_slow("1: Luxury watches: Harder to steal, but you will not "
                   "have to steal as many "
                   "because they sell for more.")
        print_slow("2: Cheaper watches: Easier to steal, but "
                   "you will have to steal many.")

        choice = choose(["1", "2"])  # User decides which they steal

        if choice == "1":  # Decide to steal luxury watches
            print_slow("So you have chosen the path of luxury...")
            print_slow("You can either steal watches from a Cartier store "
                       "in NYC or drive to the "
                       "Hamtpons and steal from there. It is less work to"
                       " steal from the city, "
                       "but there is less security in the Hamptons. Where "
                       "will you steal?")
            print_slow("1: Steal from Cartier in NYC")
            print_slow("2: Steal from a boutique in the Hamptons")

            choice = choose(["1", "2"])  # User decides where to steal from
   
            if choice =="1":  # Decide to steal from NYC
                print_slow("You successfully break into the Cartier shop. However, you were "
                           "unaware that the employees phoned the police. As "
                           "you are leaving"
                           ", you hear sirens. The police are about to "
                           "enter the building. What "
                           "do you do? ")
                print_slow("1: Hide in the building and hope "
                           "they leave after being unable to find you.")
                print_slow("2: Engage in a ferocious shootout with the police!")
       
                choice = choose(["1", "2"])  # Decide how to proceed
             
                if choice =="1":  # Decide to hide in building
                    print_slow("Somehow, your disguise as a mannequin works. The"
                               " cops are unable to locate you"
                               "and they leave. You leave the shop with 50 grand worth of "
                               "watches. Congratulations! ")
                    print_slow("You now have a decision to make. Do you flee with the watches, "
                               "or do you sell them and return to the money to the mob safely?")
                    print_slow("1: Flee with the watches and take the risk!")
                    print_slow("2:Return the money safely to the mafia and continue with your life.")
                
                
                    choice = choose(["1", "2"])  # Decide whether to flee or return money to mafia
                    
                    if choice == "1":  # Decide to flee
                        print_slow("THE MOB CATCHES YOU FLEEING. They kidnap "
                                   "you and bring you to "
                                   "their store room, where they kill"
                                   " you. BAD ENDING! ")
                        
                        sys.exit()
                        
                    elif choice == "2":  # Decide to return money to mafia
                        print_slow("The mafia accepts your money and the debt it paid. You "
                                   "are safe and continue with your life. SAFE!")
                        
                        sys.exit()
                        
                elif choice == "2":  # Decide to engage in shootout
                    print_slow("FUN CHOICE. But which gun will you pull from your bag?")
                    print_slow("1: RPG: ROCKET LAUNCHER")
                    print_slow("2: PISTOLS")
                
                    choice =  choose(["1", "2"])
                
                    if choice == "1":  # Decide to use RPG
                        print_slow("YOU FOOL! You forgot the rockets at home. What do you do now?")
                        print_slow("1: Charge at the police without a gun???")
                        print_slow("2: Throw empty RPG at police!")
                    
                        choice = choose(["1", "2"])
                    
                        if choice == "1":  # Decide to charge at police
                            print_slow("WHAT WAS YOUR THOUGHT PROCESS? The police shoot "
                                       "you 32 times and you die. HORRIBLE ENDING!")
                        
                                
                            sys.exit()
                            
                        elif choice == "2":  # Decide to throw RPG at police
                         print_slow("Since you have devised this plan to rob a Cartier shop, you"
                                   "have not been to the gym and are consequently very weak. "
                                   "The RPG does not reach any policemen, and they arrest you. "
                                   "10 YEARS IN JAIL: BAD ENDING! ")
                         
                         sys.exit()
                         
                    elif choice == "2":  # Decide to grab pistols
                        print_slow("Do you grab both pistols or only one?")
                        print_slow("1: Both")
                        print_slow("2: One")
                    
                        choice = choose(["1", "2"]) 
                    
                        if choice == "1":  # Decide to use both pistols
                            print_slow("Despite watching all the John Wick movies and two from the "
                                       " Equalizer franchise, you cannot handle two pistols."
                                       "The Police shoot you dead! HORRIBLE ENDING! ")
                            
                            sys.exit()
                            
                        elif choice == "2":  # Decide to use only one pistol
                            print_slow("Somehow, you kill all the cops and are able to flee! "
                                       "Will you pay back the mob or run away?")
                            print_slow("1: Pay the mob")
                            print_slow("2: Flee to ""Mexico")
                        
                            choice = choose(["1", "2"])
                        
                            if choice == "1":  # Return money to mafia 
                                print_slow("They accept your watches and you are safe. GOOD ENDING!")
                                
                                sys.exit()
                                
                            elif choice == "2":  # Flee to Mexico
                                print_slow("Because the mob did not expect your "
                                           "plan to work, they do not catch you as you"
                                           " flee to Mexico."
                                           "In Mexico, you sell the watches and "
                                           "become a very rich man. CONGRATULATIONS, GREAT ENDING! ")
                                
                            sys.exit()
                 
            elif choice == "2":  # Decide to drive and steal watches in the Hamptons
                print_slow("You drive out to the Hamptons. First you relax at "
                           "the beach and mentally prepare for the heist. You can "
                           "either go rob the store now,"
                           " when it is daytime or wait until night. "
                           "When will you "
                           "rob the shop?")
            print_slow("1: Nighttime")
            print_slow("2: Daytime")

            choice = choose(["1", "2"])

            if choice == "2":  # Rob in Nighttime
                print_slow("Uh oh! The alarms sound as you try to sneak into the shop at night."
                           "You have to flee. What car "
                           "will you flee in? ")
                print_slow("1: 2022 Porsche 911")
                print_slow("2: 1993 Toyota Corolla")
                
                
                choice = choose(["1", "2"])
                
                if choice == "1":  # Flee in Porsche
                    print_slow("Now, it is time for luck to determine your "
                               "fate. A coin will be flipped to determine if "
                               "the Porsche has or does not have gas. ")
                    import random 
                    coin = random.randint(1, 2) # Function- 50/50 to determine outcome
                    
                    if coin == 1:  # 50/50 determines that car has gas
                        print_slow("HEADS!The car has gas! You flee to Mexico and "
                                   "are safe but you never stole any watches, so you"
                                   " don't have a lot of money. ALRIGHT ENDING")
                        
                        sys.exit()
                        
                    elif coin == 2:  # 50/50 determines that car has no gas
                        print_slow("TAILS...The car does not have any gas. The police"
                                   "catch you and arrest you for breaking and "
                                   "entering. ARRESTED FOR 6 YEARS: BAD ENDING!")
                        
                        sys.exit()
                        
                elif choice == "2":  # Decide to drive in Corolla
                    print_slow("Interesting choice.. The police catch "
                               "you as you drive off because the gar is not very"
                               " fast. You are arrest for both reckless driving and breaking"
                               "and entering. ARRESTED 15 YEARS: HORRIBLE ENDING!")
                    
                    sys.exit()
                    
                    
            elif choice == "1":  # Rob in daytime
                print_slow("Now, luck will determine your fate. A "
                           "coin will be flipped to determine if the shop's inventory"
                           "is full or empty ")
            
                import random
                
                coin2 = random.randint(1, 2)
                if coin2 == 1:
                    print_slow("The shop is empty. MILD ENDING. You may restart the game.")
                    
                    sys.exit()
                
                elif coin2 == 2:  # Coin determines that shop is full
                    print_slow("The shop is filled with Rolex and AP, "
                               "and luckily as you walk into the shop, the owner is in"
                               "the bathroom. You steal 10 Rolex and 5 Audemars Piguet! "
                           "What do you do next?")
                print_slow("1: Return to NYC and pay the mob")
                print_slow("2: Flee")
                
                choice = choose(["1", "2"])
                
                if choice == "1":  # Decide to pay back mafia
                    print_slow("They accept the watches and the debt is paid. You "
                               " are safe. Congratulations: GOOD ENDING!")
                    
                    sys.exit()
                    
                elif choice == "2":  # Decide to flee to Canada
                    print_slow("You flee north to Canada. You sell your watches "
                               "and get a huge profit. You live in "
                               "Canada as a Millionaire! GREAT ENDING!")
                    
                    sys.exit()
                    
                
        elif choice == "2":  # Decide to steal cheap watches
            print_slow("I see that you do not want to take risk."
                       " At times, that is a good trait. We will see...")
            print_slow("You go to a Macy's in midtown New York and try to stuff"
                       "as many watches as you can into your backpack")
            print_slow("Unfortunately, the alarms sound and you are in"
                       " serious trouble. Do you turn yourself in or try to get away? ")
            print_slow("1: Try to get away")
            print_slow("2: Turn yourself in")
        
            choice == choose(["1", "2"])
        
            if choice == "1":  # Decide to escape
                print_slow("How will you try to escape")
                print_slow("1: Run away")
                print_slow("2: Disguise and hide")
                print_slow("3: Jog away avoid attention")
        
                choice == choose(["1", "2", "3"])
            
                if choice == "1":  # Decide to  run away
                    print_slow("Unfortunately, you trip on a bottle of Dior Sauvage. You "
                               "break your wrist and are caught and "
                               "arrested. BAD ENDING 2 YEARS IN JAIL!")
                    
                    sys.exit()
                    
                elif choice == "2":  # Decide to hide and disguise 
                    print_slow("You disguise as a mannequin. Thought"
                               " you thought this would work, it does"
                               " not. You are found and arrested. "
                               " Bad ENDING, ARRESTED 4 YEARS.")
                    
                    sys.exit()
                    
                elif choice == "3":  # Decide to calmly jog away
                    print_slow("You are tazed, suffer a heart attack and die."
                               "HORRIBLE ENDING")
                    
                    sys.exit()
            
                
        if choice =="2":  # Decide to run away
           print_slow("You are found, but since you turned yourself in, a"
                      "re sentenced to 50 hours community service."
                      "DECENT ENDING!")
           
           sys.exit()
                    
                
    elif choice == "2":  # Decide to be online guru
        print_slow("Being an online guru is "
                   "very risky and I am not"
                   " sure why this was your choice.")
        print_slow("Gaining popularity on social media"
                   " is mosty luck. A coin"
                   " will be flipped to determine if"
                   " you are able to gain popularity. ")    



        coinmedia = random.randint(1, 2)
               
        if coinmedia == 1:  # Coin determines that you gain popularity
            print_slow("CONGRATULATIONS. You went extremely viral and"
                       " started an online course, by which you made 100k")
            print_slow("However, the mob fears that your popularity"
                       " will draw them unwanted "
                       "attention. They decide you must be dealth with."
                       " MOB KILLS YOU. HORRIBLE ENDING.")

            sys.exit()
            
        if coinmedia == 2:  # Coin determines that you do not gain popularity
            print_slow("Unfortunately, your scheme failed. You fail to gain enough"
                       "money to pay back the mob. What will you do?")
            print_slow("1: Tell the mob and hope they understand")
            print_slow("2: Try to take out the entire mob family yourself")
            
            choose = choice(["1", "2"])
            
            if choice == "1": # Decide to tell mob about failure
                print_slow("Luckily, they understand your "
                           "failure and give you another month, though it is"
                           " your LAST month. RESTART GAME.")
                sys.exit()
                
            if choice == "2": # Decide to attempt to kill mafia
                print_slow("Your 'best friend' Joseph, who was actually an "
                           "undercover foot solider for the mob, hears"
                           "of you plan and 'pops' you. DEAD HORRIBLE ENDING.")
 
                sys.exit()
        
        
        
elif choice == "2": # Decide not to play
    print_slow("Be gone before me at once and never return to my glorious game!")
else:
    print("Invalid Response. Try Again")
    
    sys.exit()
    

    
    



















