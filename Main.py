#############################################
# Name: Sasha
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament

# Project Description: See the README file
#############################################

# THIS IS WHERE YOU CODE

print("What's first team name?")
team_1_name = input()

print("How many wins does first team have?")
team_1_wins: int = int(input())

print("How many ties does first team have?")
team_1_ties = int(input())

print("How many losses does first team have?")
team_1_losses = int(input())

team_1_score: int = (team_1_wins * 2) + (team_1_ties * 1)
print(team_1_name,"score is",team_1_score)

print("It's time for second team!")

print("What's second team's name?")
team_2_name = input()

print("How many wins does second team have?")
team_2_wins: int = int(input())

print("How many ties does second team have?")
team_2_ties: int = int(input())

print("How many losses does second team have?")
team_2_losses: int = int(input())

team_2_score = (team_2_wins * 2) + (team_2_ties * 1)
print(team_2_name,"score is",team_2_score)

if (team_1_score > team_2_score):
    print(team_1_name, "wins!!!")

elif (team_1_score < team_2_score):
    print(team_2_name, "wins!!!")

elif team_1_score==team_2_score:
    print("TIE!")