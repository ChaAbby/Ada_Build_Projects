p1 = input("Player 1 > ")
p2 = input("Player 2 > ")
def rps(player1, player2):
    """
    input: player1 and player2 should each be 'rock', 'paper', or 'scissors'
    output: the outcome of the game
    """
    if (player1 == "rock" and player2 == "paper") or (player1 == "scissors" and player2 == "rock") or (player1 == "paper" and player2 == "scissors"):
      print("Player 1 Wins!")
    elif (player1 == "paper" and player2 == "rock") or (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper"):
      print("Player 2 Wins!")
    elif player2 == player1:
      print("Tie!")
    else:
      print("Please enter rock, paper, or scissors")

rps(p1,p2)
