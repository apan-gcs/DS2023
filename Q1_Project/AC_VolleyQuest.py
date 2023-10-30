'''
Angel Colin
10/24/23
Intensive Data Science 2
Project #1 - VolleyQuest
'''

import random
from time import sleep

# Slow Text Function
def typewriter(text):
    for x in text:                    # Cycle through the text
        print(x, end='', flush=True)  # Print character, no new line
        sleep(0.02)                   # Delay between characters
    print()                           # New line
    sleep(0.5)                        # Delay after finishing the line
 
# Team Class
class Team:  
    def __init__(self, name):
        self.name = name
        self.score = 0                # Score Attribute

# Player Class
class Player:
    def __init__(self, name):
        self.name = name

# Team Name Function
def team_name_function(team):
    typewriter("Team: " + team.name)

# Match Logic For Hit/Block/Vitamins/Quit
def choice():                                                       
    option = input("Enter your action (hit/block/vitamins/quit): ")
    return option

# Match Logic For Hit/Block/Vitamins/Quit
def play_match(player_team, opponent_team):                        
    player_score = 0
    opponent_score = 0

    typewriter(f"Match starts between {player_team.name} and {opponent_team.name}!\n")

    while player_score < 5 and opponent_score < 5:

        player_input = choice()                                        # Checks for player choice

        if player_input == "hit":                                      # Hit Logic
            
            player_number = random.randint(1, 100)
            opponent_number = random.randint(1, 100)

            typewriter(f"Player's power: {player_number}")
            typewriter(f"Opponent's power: {opponent_number}")

            if player_number > opponent_number:
                player_score += 1
                typewriter(f"{player_team.name} scores a point!\n")
            else:
                opponent_score += 1
                typewriter(f"{opponent_team.name} scores a point!\n")
                
        elif player_input == "block":                                   # Block Logic
            player_number = random.randint(1, 100)
            opponent_number = random.randint(1, 100)

            typewriter(f"Player's power: {player_number}")
            typewriter(f"Opponent's power: {opponent_number}")

            if player_number > opponent_number:
                player_score += 1
                typewriter(f"{player_team.name} scores a point!\n")
            else:
                opponent_score += 1
                typewriter(f"{opponent_team.name} scores a point!\n")
        
        elif player_input == "vitamins":                                  # Vitamins Logic
           player_number = random.randint(1, 100)
           opponent_number = random.randint(1, 100)
           
           vitamin_number = player_number + random.randint(-10,10)   
           
           typewriter(f"Player's number: {vitamin_number}")
           typewriter(f"Opponent's number: {opponent_number}")
         
           
           if vitamin_number > opponent_number:
               player_score += 1
               typewriter(f"{player_team.name} scores a point!\n")
               
           else:
               opponent_score += 1
               typewriter(f"{opponent_team.name} scores a point!\n")

        elif player_input == "quit":                                        # Quit Logic
            typewriter("Match quit.")
            return False

        else:                                                               # What to do in case of invalid response
            typewriter("Invalid input. Try again.\n")

        typewriter(f"Score: {player_team.name} - {player_score} | {opponent_team.name} - {opponent_score}") # Scoreboard

# Win Logic
    if player_score == 5:
        games_won = 0
        typewriter(f"{player_team.name} wins the match!")
        games_won = games_won + 1
        return True
    else:
        typewriter(f"{opponent_team.name} wins the match.")
        return False

# Interaction Function
def interact_with_teammates(player_team):
    typewriter(f"You and the {player_team.name} are preparing for an important volleyball match against a tough opponent.")
    typewriter("Before the match, you have a chance to interact with your teammates.\n")
    typewriter("What do you wish to do?")
    
    typewriter("motivate/provoke")                                                          # Motivate/Provoke Options
    choice_team = input()
    
    if choice_team == "motivate":                                                           # What to do if motivate selected
        typewriter("You give a motivational speech. The team is amped up for the game.\n")
        
    elif choice_team == "provoke":                                                          # What to do if provoke selected
        typewriter("Your team is irritated. They're amped up to play but hate you.\n")
        
    else:
        typewriter("Invalid input. You gave no speech before the game\n")                   # What to do if neither selected
        
# Game Narrative Code
def main():
    typewriter("Welcome to VolleyQuest!")
    typewriter("You are in the state tournament and must win 3 games in a row to become champion.")
    typewriter("You have two teammates, and the game is up to 5 points.")
    typewriter("You can hit or block by typing hit or block, take a risk and take vitamins by typing vitamins, or quit by typing quit\n")
    typewriter("Have Fun!\n")
    team_name = input("Enter your team name: ")
    typewriter("Your Teammates are Ethan the Libero and JonJon the Setter!")

    # Generates Players On The Team
    player1 = Player("Player1")
    player2 = Player("Player2")
    player3 = Player("Player3")

    player_team = Team(team_name)
    player_team.players = [player1, player2, player3]

    # Defines Opponent Team
    opponent_team = Team("Grace Church School Varsity Volleyball")

    games_won = 0                                                       # Base wins that get added to

    # Main Game Loop
    while games_won < 3:                                                # Loop until the player has won 3 games
        if games_won == 0:
            typewriter("You are in the Quarter Finals. Get Ready !\n")
        elif games_won == 1:
            typewriter("You are now in the Semi Finals. Get Ready !\n")
        elif games_won == 2:
            typewriter("You reached Finals. Don't mess up !\n")

        interact_with_teammates(player_team)                            # Interaction before game function

        team_name_function(player_team)

        if play_match(player_team, opponent_team):                      # Continues Game
            games_won += 1
            typewriter("You advance!\n")
            opponent_team = Team("Opponent Team")
        else:
            typewriter("You lost. Try again.")
            break

    # Check if the player has won 3 games
    if games_won == 3:
        typewriter("Congratulations! You won the entire tournament!")

if __name__ == "__main__":
    main()