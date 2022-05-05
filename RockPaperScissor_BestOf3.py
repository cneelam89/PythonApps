import random
player1_win=player2_win = 0
a=["scissors", "rock", "paper"]
while player1_win<=2 and player2_win<=2:
    player1= input("Player 1 choice:   ")
    player2= random.choice(a)
    print(f"Player 2 choice:  {player2}")
#conditional logic for player1 to win
    if((player1=="rock" and player2 == "scissors")or (player1=="paper" and player2 == "rock")or (player1=="scissors" and player2 == "paper")):
        player1_win +=1
        print(f"player 1 win time {player1_win}")
#conditional logic for player2 to win
    elif((player2=="rock" and player1 == "scissors")or (player2=="paper" and player1 == "rock")or (player2 =="scissors" and player1 == "paper")):
        player2_win +=1
        print(f"player 2 win time {player2_win}")
#conditional logic for a tie
    elif(player1==player2):
        print("its a tie")
    else:
        print("something gone wrong")


if player1_win<player2_win:
    print("player2 wins")
else:
    print("player1 wins")


