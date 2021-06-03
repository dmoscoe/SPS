# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:44:24 2021

@author: dmosc

Prompt: Write a simulation for a simple game of chance. Run the simulation 1000 times and interpret the outcome. Post your code here, and discuss what might be done to improve it.

Game: See the History section at https://en.wikipedia.org/wiki/Gambler%27s_ruin.

Two players take turns throwing 3 dice. Player A scores a point whenever 11 is thrown. Player B scores a point whenever 14 is thrown. If the opponent's score is 0, the point is added to the player's score. If the opponent's score is greater than 0, the point is subtracted from the opponent's score. "It is as if opposing points form pairs, and annihilate each other, so that the trailing player always has zero points. The winner is the first to reach 12 points."
"""
import random

def throw(): #Returns the value of a 3-dice throw
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    
    return d1 + d2 + d3

def score_updater(scores, throws, throw): #Returns a list containing Player A's score and Player B's score when given initial scores, the number of throws conducted so far, and the value of the current throw.
    if ((throw == 11) and (throws % 2 == 1)): #It's A's turn and A won
        if scores[1] == 0:
            scores[0] += 1
        else:
            scores[1] -= 1
            
    if ((throw == 14) and (throws % 2 == 0)): #It's B's turn and B won
        if scores[0] == 0:
            scores[1] += 1
        else:
            scores[0] -= 1
    
    return scores

def game(): #Returns the winner of a game.
    scores = [0,0]
    throws = 0
    
    while max(scores) < 12:
        throws += 1
        scores = score_updater(scores,throws,throw())
    
    if scores[0] > scores[1]:
        return "A"
    else:
        return "B"
    
winners = [0,0] #The number of games won by A and B in 1000 games.
for i in range(1000):
    if game() == "A":
        winners[0] += 1
    else:
        winners[1] += 1

print(winners)

#Note that A almost always wins all the games. The probability of rolling 11 is 12.5%, and the probability of rolling 14 is 7%. This difference is enough for it to be almost impossible for B to win.
