from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tkinter import filedialog
import os

# % Create a window
root = Tk()
root.title('Group 3 finalterm AI')
var = StringVar()
label = Label(root, textvariable=var, bg="WHITE", font=(
    None, 13), bd=10, justify=CENTER, padx=5, pady=5)
var.set("Application apply algorithms to games")
label.pack()

# %Crate a frame: Application
frame1 = LabelFrame(root, text='Application')
frame1.pack(fill=BOTH, side='bottom', padx=5, pady=5, ipadx=5, ipady=5)


def Run_GUI_Eight_Puzzle():
    os.system('python GUI_Eight_Puzzle.py')


def Run_GUI_N_Queens():
    os.system('python GUI_N_Queens.py')


# %bt 8 Puzzle
button_Puzzle = Button(frame1, text='Aplly IDS to 8_Puzzles',
                       command=Run_GUI_Eight_Puzzle, bg='#008E89', fg='white', width=27)
button_Puzzle.pack(ipadx=15, ipady=15)
# %bt N Queen
button_NQueens = Button(frame1, text='Aplly Simulated Annealing to N_Queens',
                        command=Run_GUI_N_Queens, bg='#C1F4C5', width=27)
button_NQueens.pack(pady=5, ipadx=15, ipady=15)

# %btquit
button_quit = Button(frame1, text='Exit Program',
                     command=root.destroy, bg='#EF6D6D', width=27)
button_quit.pack(pady=5, ipadx=15, ipady=15)


root.mainloop()
