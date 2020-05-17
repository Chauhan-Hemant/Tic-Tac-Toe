from random import randint
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

ActivePlayer = 1
player1 = []
player2 = []
move = 0


def Set_the_Layout(id, player_symbol):
    if id == 1:
        button1.config(text=player_symbol)
        button1.state(['disabled'])
    elif id == 2:
        button2.config(text=player_symbol)
        button2.state(['disabled'])
    elif id == 3:
        button3.config(text=player_symbol)
        button3.state(['disabled'])
    elif id == 4:
        button4.config(text=player_symbol)
        button4.state(['disabled'])
    elif id == 5:
        button5.config(text=player_symbol)
        button5.state(['disabled'])
    elif id == 6:
        button6.config(text=player_symbol)
        button6.state(['disabled'])
    elif id == 7:
        button7.config(text=player_symbol)
        button7.state(['disabled'])
    elif id == 8:
        button8.config(text=player_symbol)
        button8.state(['disabled'])
    elif id == 9:
        button9.config(text=player_symbol)
        button9.state(['disabled'])


def Check_for_Win():
    global move
    winner = -1

    if (1 in player1) and (2 in player1) and (3 in player1):
        winner = 1
    if (1 in player2) and (2 in player2) and (3 in player2):
        winner = 2

    if (4 in player1) and (5 in player1) and (6 in player1):
        winner = 1
    if (4 in player2) and (5 in player2) and (6 in player2):
        winner = 2

    if (7 in player1) and (8 in player1) and (9 in player1):
        winner = 1
    if (7 in player2) and (8 in player2) and (9 in player2):
        winner = 2

    if (1 in player1) and (4 in player1) and (7 in player1):
        winner = 1
    if (1 in player2) and (4 in player2) and (7 in player2):
        winner = 2

    if (2 in player1) and (5 in player1) and (8 in player1):
        winner = 1
    if (2 in player2) and (5 in player2) and (8 in player2):
        winner = 2

    if (3 in player1) and (6 in player1) and (9 in player1):
        winner = 1
    if (3 in player2) and (6 in player2) and (9 in player2):
        winner = 2

    if (1 in player1) and (5 in player1) and (9 in player1):
        winner = 1
    if (1 in player2) and (5 in player2) and (9 in player2):
        winner = 2

    if (3 in player1) and (5 in player1) and (7 in player1):
        winner = 1
    if (3 in player2) and (5 in player2) and (7 in player2):
        winner = 2

    if winner == 1:
        Label(root, text="Player 1 is the winner...!!!").grid(row=0, column=0)
        messagebox.showinfo(title="Congratulations.", message="Player 1 is the winner...!!!")

    elif winner == 2:
        Label(root, text="Player 2 is the winner...!!!").grid(row=0, column=0)
        messagebox.showinfo(title="Congratulations.", message="Player 2 is the winner...!!!")

    elif move == 9:
        Label(root, text="It's a Draw...!!!").grid(row=0, column=0)
        messagebox.showinfo(title="Draw", message="It's a Draw...!!!")


def Button_Clicked(id):
    global ActivePlayer
    global player1, player2
    global move

    if (ActivePlayer == 1):
        Set_the_Layout(id, "X")
        player1.append(id)
        move += 1
        Label(root, text="\t\tPlayer 2 turn :\t\t").grid(row=0, column=0)
        ActivePlayer = 2

    elif (ActivePlayer == 2):
        Set_the_Layout(id, "O")
        player2.append(id)
        move += 1
        Label(root, text="\t\tPlayer 1 turn :\t\t").grid(row=0, column=0)
        ActivePlayer = 1
    Check_for_Win()


def Switch_Player():
    global player1
    global player2
    Empty = []
    for cell in range(9):
        if (not ((cell + 1 in player1) or (cell + 1 in player2))):
            Empty.append(cell + 1)
    try:
        Random_Index = randint(0, len(Empty) - 1)
        Button_Clicked(Empty[Random_Index])
    except:
        pass


def Enable_All_Buttons():
    button1.config(text=" ")
    button1.state(['!disabled'])
    button2.config(text=" ")
    button2.state(['!disabled'])
    button3.config(text=" ")
    button3.state(['!disabled'])
    button4.config(text=" ")
    button4.state(['!disabled'])
    button5.config(text=" ")
    button5.state(['!disabled'])
    button6.config(text=" ")
    button6.state(['!disabled'])
    button7.config(text=" ")
    button7.state(['!disabled'])
    button8.config(text=" ")
    button8.state(['!disabled'])
    button9.config(text=" ")
    button9.state(['!disabled'])


def Restart():
    global player1, player2, move, ActivePlayer
    player1.clear()
    player2.clear()
    move, ActivePlayer = 0, 1
    Label(root, text="\t\tPlayer 1 turn :\t\t").grid(row=0, column=0)
    Enable_All_Buttons()


root = Tk()
root.title("Tic Tac toe")
Label(root, text="\t\tPlayer 1 turn :\t\t").grid(row=0, column=0)
st = ttk.Style()
st.configure("my.TButton", font=('arial', 24, 'bold'))

button1 = ttk.Button(root, text=" ", style="my.TButton")
button1.grid(row=1, column=0, sticky="nwse", ipadx=50, ipady=50)
button1.config(command=lambda: Button_Clicked(1))

button2 = ttk.Button(root, text=" ", style="my.TButton")
button2.grid(row=1, column=1, sticky="snew", ipadx=50, ipady=50)
button2.config(command=lambda: Button_Clicked(2))

button3 = ttk.Button(root, text=" ", style="my.TButton")
button3.grid(row=1, column=2, sticky="snew", ipadx=50, ipady=50)
button3.config(command=lambda: Button_Clicked(3))

button4 = ttk.Button(root, text=" ", style="my.TButton")
button4.grid(row=2, column=0, sticky="snew", ipadx=50, ipady=50)
button4.config(command=lambda: Button_Clicked(4))

button5 = ttk.Button(root, text=" ", style="my.TButton")
button5.grid(row=2, column=1, sticky="snew", ipadx=50, ipady=50)
button5.config(command=lambda: Button_Clicked(5))

button6 = ttk.Button(root, text=" ", style="my.TButton")
button6.grid(row=2, column=2, sticky="snew", ipadx=50, ipady=50)
button6.config(command=lambda: Button_Clicked(6))

button7 = ttk.Button(root, text=" ", style="my.TButton")
button7.grid(row=3, column=0, sticky="snew", ipadx=50, ipady=50)
button7.config(command=lambda: Button_Clicked(7))

button8 = ttk.Button(root, text=" ", style="my.TButton")
button8.grid(row=3, column=1, sticky="snew", ipadx=50, ipady=50)
button8.config(command=lambda: Button_Clicked(8))

button9 = ttk.Button(root, text=" ", style="my.TButton")
button9.grid(row=3, column=2, sticky="snew", ipadx=50, ipady=50)
button9.config(command=lambda: Button_Clicked(9))

Button(text="Reset", font=('arial', 22, 'bold'), bg='lightgrey', fg='black',
       border=5, width=4, command=lambda: Restart()).grid(row=4, column=1, sticky="we")
root.resizable(0, 0)
root.mainloop()
