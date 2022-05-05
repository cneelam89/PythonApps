import random

ladder={1:38, 4:14, 8:30, 21:42, 28:76, 50:67,0:92}
snake={32:10, 34:6, 48:26, 62:18, 88:24, 97:78}

pos1=0
pos2=0

def move(pos):
    dice=random.randint(1,6)
    print(f" Dice: {dice}")
    pos += dice
    if pos in ladder:
        print("climbed by ladder ")
        pos=ladder[pos]
        print(f"Position :{pos}")
    elif pos in snake:
        print("bitten by snake ")
        pos=snake[pos]
        print(f"Position :{pos}")
    else:
        print(f"Position :{pos}")
    return pos

while True:
    A:input ("Player1 Enter to throw dice :")
    pos1 =move (pos1)
    if pos1 >=100:
        print("Player1 wins")
    B:input ("Player2 Enter to throw dice :")
    pos2 =move (pos2)
    if pos2 >=100:
        print("Player2 wins")
        break
