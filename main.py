import tkinter
from tkinter import*
import random
from tkinter import messagebox
from random import shuffle

answers = ['apple', 'banana', 'orange', 'cherry', 'strawberry']

words = []

for i in answers:
    word = list(i)
    shuffle(word)
    words.append(word)

num = random.randint(0, len(words)-1)


def reset():
    global words, num, answers
    num = random.randint(0, len(words)-1)
    lbl1.configure(text=words[num])
    e1.delete(0, END)


def ans_check():
    global words, num, answers
    user_input = e1.get()
    if user_input == answers[num]:
        messagebox.showinfo('Success', 'Correct')
        reset()
    else:
        messagebox.showinfo('Error', 'Try Again')
        e1.delete(0, END)


def initial():
    global words, num
    lbl1.configure(text=words[num])


root = tkinter.Tk()
root.geometry('300x300')
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
