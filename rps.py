user = "rock"
comp = "paper"

if (user == "rock" and comp == "paper") or (user == "scissors" and comp == "rock") or (user == "paper" and comp == "scissors"):
    print("Computer Wins!")
elif (user == "paper" and comp == "rock") or (user == "rock" and comp == "scissors") or (user == "scissors" and comp == "paper"):
    print("User Wins!")
elif comp == user:
    print("Tie!")
else:
    print("Please enter rock, paper, or scissors")
