from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from N_Queens import *
import time
listButton = []

size = 0


def createTable():
    global size
    if (entrySize.get().isdigit()):  # check input is a number
        size = int(entrySize.get())
    global listButton
    listButton = []
    for i in range(size):
        li = []
        for j in range(size):
            bt = tk.Button(frame, bg='white')  # create button
            if ((i+j) % 2 == 0):
                bt['bg'] = 'gray'
            bt.place(relx=j/size, rely=i/size,
                     relwidth=1/size, relheight=1/size)
            bt['state'] = 'disable'
            li.append(bt)  # append in the temp list
        listButton.append(li)  # append in the list button


def Click_Simulated_Annealing():
    for i in range(size):
        for j in range(size):
            listButton[i][j]['image'] = ''  # set default image
    no_of_queens = size
    problem1 = NQueensProblem(size)  # create N Queen Problem
    start = time.time()  # start time
    solution = simulated_annealing(problem1)  # find solution
    end = time.time()  # end time
    lbTime['text'] = "{:.12f}".format(
        float(end-start))  # print time to label time
    for i in range(size):
        if (solution[i] != -1):
            # state is normal to show image
            listButton[i][solution[i]]['state'] = 'normal'
            if ((i+solution[i]) % 2 == 0):  # background is gray
                # image with background is gray
                listButton[i][solution[i]]['image'] = photo_gray
            else:
                # image with background is white
                listButton[i][solution[i]]['image'] = photo_white


root = tk.Tk()
root.title('N Queens Using Simulated Annealing Algorithms')
var = StringVar()
label = Label(root, textvariable=var, bg="WHITE", font=(
    None, 13), bd=10, justify=CENTER, padx=5, pady=5)
var.set("SOLVE N_QUEEN ")
label.pack()


canvas = tk.Canvas(root, height=550, width=650)
canvas.pack()
frame = tk.Frame(root, bg='gray')
frame.place(relwidth=0.8, relheight=1)


rightFrame = tk.Frame(root, bg='#8ad4e1')
rightFrame.place(relwidth=0.2, relheight=1, relx=0.8, rely=0)


lbEnterSize = tk.Label(rightFrame, text='Enter size: ', bg="#EF6D6D", width=15)
lbEnterSize.place(relx=0.085, rely=0.05)

entrySize = tk.Entry(rightFrame)
entrySize.place(relx=0.085, rely=0.09, width=110, height=30)

# click to create NxN button

btSetUp = tk.Button(rightFrame, text='Set Up',
                    command=createTable, bg='#C1F4C5', width=15)
btSetUp.pack(pady=5, ipadx=15, ipady=15)
btSetUp.place(relx=0.085, rely=0.145)

# click to run the game
btsimulated_annealing = tk.Button(
    rightFrame, text='Simulated Annealing', command=Click_Simulated_Annealing, bg='#FFBED8', width=15)
btsimulated_annealing.place(relx=0.085, rely=0.25)


lbTime1 = tk.Label(rightFrame, text="Time: ",
                   bg="#008E89", fg='white', width=15)
lbTime1.place(relx=0.085, rely=0.40)

lbTime = tk.Label(rightFrame, bg='#8ad4e1')  # show time
lbTime.place(relx=0.085, rely=0.44)

image = Image.open("images_nqueen/queen_white.png")
image = image.resize((50, 50), Image.ANTIALIAS)
photo_white = ImageTk.PhotoImage(image)  # queen with white background
image2 = Image.open("images_nqueen/queen_gray.png")
image2 = image2.resize((50, 50), Image.ANTIALIAS)
photo_gray = ImageTk.PhotoImage(image2)  # queen with gray background


root.mainloop()
