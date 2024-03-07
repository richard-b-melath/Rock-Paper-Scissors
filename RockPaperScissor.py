import random
import getpass
print("Enter:\n 1.Single Player 2.Multi Player")
choice = int(input("Enter your choice(1,2) : "))
maxpoint = int(input("Enter the winning point : "))
gameoptions = {
    0: "ROCK",
    1: "PAPER",
    2: "SCISSOR"
}
comp = 1
player = 0
comppoint = 0
playerpoint = 0
if choice == 1:
  while True:
    print("\nEnter \n0.Rock, 1.Paper, 2.Scissor")
    player = int(input("Enter your option(0,1,2) : "))
    comp = random.randint(0,2)
    print(f"Player = {gameoptions[player]}, Computer = {gameoptions[comp]}")
    if player == comp:
      print("Its a draw")
    elif (player == 0 and comp ==2) or (player == 1 and comp == 0) or (player == 2 and comp == 1):
      playerpoint += 1
      print("Player +1")
    else:
      comppoint += 1
      print("Computer +1")

    print(f"Player = {playerpoint}, Computer = {comppoint}")

    if playerpoint == maxpoint:
      print("\nPlayer Won!!!")
      break
    elif comppoint == maxpoint:
      print("\nComputer Won!!!")
      break

else:
  player1point = 0
  player2point = 0
  while True:
    print("\nEnter \n0.Rock, 1.Paper, 2.Scissor")
    player1 = int(getpass.getpass("Player1, enter your option : "))
    player2 = int(getpass.getpass("Player2, enter your option : "))
    print(f"Player1 = {gameoptions[player1]}, Player2 = {gameoptions[player2]}")

    if player1 == player2:
      print("Its a draw")
    elif (player1 == 0 and player2 ==2) or (player1 == 1 and player2 == 0) or (player1 == 2 and player2 == 1):
      player1point += 1
      print("Player1 +1")
    else:
      player2point += 1
      print("Player2 +1")

    print(f"Player1 = {player1point}, Player2 = {player2point}")

    if player1point == maxpoint:
      print("\nPlayer1 Won!!!")
      break
    elif player2point == maxpoint:
      print("\nCPlayer2 Won!!!")
      break



