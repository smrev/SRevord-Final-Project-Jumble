import tkinter
from tkinter import *
import random
from tkinter import messagebox
from random import shuffle
import csv

# open and read file that contains US President names
presidents = open('us_presidents.csv', 'r')
file = csv.DictReader(presidents)

# variables to hold answers, jumbled answers,
answers = []
words = []


# add names to the list containing game answers
for column in file:
    answers.append(column['president'])


for i in answers:
    i = i.strip().lower().replace(' ', '')
    word = list(i)
    shuffle(word)
    words.append(word)

num = random.randint(0, len(words)-1)


def reset():
    global words, num, answers
    num = random.randint(0, len(words)-1)
    lbl1.configure(text=words[num])
    e1.delete(0, END)
    button2.forget()
    button1.pack(pady=40)
    button2.pack()


def ans_check():
    global words, num, answers
    user_input = e1.get()
    if user_input == answers[num]:
        messagebox.showinfo('Success', 'Correct')
        lbl1.configure(text=answers[num])
    else:
        messagebox.showinfo('Error', 'Try Again')
        lbl1.configure(text=answers[num])
    button1.pack_forget()


def initial():
    global words, num
    lbl1.configure(text=words[num])


root = tkinter.Tk()
root.geometry('500x300')
lbl1 = Label(root, font='times 20')
lbl1.pack(pady=30, ipady=10, ipadx=10)

answer12 = StringVar()
e1 = Entry(root, textvariable=answer12)
e1.pack(ipady=5, ipadx=5)

button1 = Button(root, text="Check", width=20, command=ans_check)
button1.pack(pady=40)

button2 = Button(root, text='Reset', width=20, command=reset)
button2.pack()

initial()

root.mainloop()
