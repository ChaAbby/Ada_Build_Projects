import random

def choose_rps():
    "output: randomly returns rock, paper, or scissors"
    r = random.randint(0,2)
    
    if r == 0:
        return "rock"
    elif r == 1:
        return "scissors"
    else:
        return "paper"

# complete the program here
player1 = choose_rps()
player2 = choose_rps()
# rock paper scissors outcome selector
print("Welcome to Rock Paper Scissors!")
def rps(player1, player2):
    """
    input: player1 and player2 should each be 'rock', 'paper', or 'scissors'
    output: the outcome of the game
    """
    if (player1 == "rock" and player2 == "paper") or (player1 == "scissors" and player2 == "rock") or (player1 == "paper" and player2 == "scissors"):
      print("Player 2 Wins!")
    elif (player1 == "paper" and player2 == "rock") or (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper"):
      print("Player 1 Wins!")
    elif player2 == player1:
      print("Tie!")
    else:
      print("Please enter rock, paper, or scissors")
# runs full program
def play():
    """output: randomly returns True or False"""
    b = random.randint(0,4)
    while b <= 5:
          b += 1
          play1 = choose_rps()
          play2 = choose_rps()
          print("Player 1 chose "  + play1)
          print("Player 2 chose " + play2)
          rps(play1, play2)
          print("-------------------------------")
          
    else:
        print("Thank you for playing!")
play()