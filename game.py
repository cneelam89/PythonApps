import tkinter
import random

# list of possible colors
colours = [
    "Red",
    "Blue",
    "Green",
    "Pink",
    "Black",
    "Yellow",
    "Orange",
    "White",
    "Purple",
    "Brown",
]
score = 0
timeleft = 30
# function that will start the game
def startGame(event):
    if timeleft == 30:
        countdown()
    nextColour()


# function that will shuffle and show the next colour
def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        # set focus on entry box
        e.focus_set()
        # compare the input from entrybox with colors list [1st element]
        if e.get().lower() == colours[1].lower():
            # increment the score
            score += 1
        # clear the entry box
        e.delete(0, tkinter.END)
        # shuffle the color list
        random.shuffle(colours)
        # color configuration to display foreground color, text is the 0th element
        colourLabel.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score:" + str(score))


# starts the timer
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time Left:" + str(timeleft))
        timeLabel.after(1000, countdown)


# Front-End:
root = tkinter.Tk()
root.title("Color Game")
root.geometry("500x500")
instructions = tkinter.Label(
    root, text="Type in the color of the words, not the text", font=("Calibri", 12)
)
instructions.pack()
scoreLabel = tkinter.Label(root, text="Press enter to start", font=("Helvetica", 12))
scoreLabel.pack()
timeLabel = tkinter.Label(
    root, text="Time Left: " + str(timeleft), font=("TimesNewRoman", 12)
)
timeLabel.pack()
colourLabel = tkinter.Label(root, font=("Helvetica", 12))
colourLabel.pack()
e = tkinter.Entry(root)
e.pack()
root.bind("<Return>", startGame)
e.focus_set()
root.mainloop()