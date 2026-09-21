#############################################
# Name: Your name
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################

# THIS IS WHERE YOU CODE
#name of the first team
print("What's first team name?")
team_1_name = input()
#first team's wins
print("How many wins does first team have?")
team_1_wins: int = int(input())
#first team's ties
print("How many ties does first team have?")
team_1_ties = int(input())
#frist team's loses
print("How many losses does first team have?")
team_1_losses = int(input())
#wins are multiplied by 2,
#Ties by multiplied 1 (not multiplied if easier)
#And loses doesn't count.
#Wins, ties and loses are adding on each other.
print(team_1_name,"'s score is", team_1_score)
team_1_score = team_1_wins * 2 + team_1_ties * 1