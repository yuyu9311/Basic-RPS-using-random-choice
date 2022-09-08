# importing wait time module
from multiprocessing.connection import wait
from time import sleep

# printing intro
wait_time=1
print("Rock...")
sleep(wait_time)
print("...paper...")
sleep(wait_time)
print("...scissors...")
sleep(wait_time)
print("SHOOT!")
sleep(wait_time)
print("\n* * *\n")

# choose random from list for each player
from random import choice
player1 = choice(['Rock', 'Paper', 'Scissors'])
player2 = choice(['Rock', 'Paper', 'Scissors'])

# logic for each choice: prints all player1 win conditions, else player 2 wins
if player1 == player2:
    print ("Tie!")
elif player1 == "Rock" and (player2 == "Scissors"):
    print ("Player 1 Wins!")
elif player1 == "Scissors" and (player2 == "Paper"):
    print ("Player 1 Wins!")
elif player1 == "Paper" and (player2 == "Rock"):
    print ("Player 1 Wins!")
else: 
    print ("Player 2 Wins!")
  
# prints the players random choice
print (player1)
print (player2)