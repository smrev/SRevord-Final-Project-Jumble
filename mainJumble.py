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
# and keep track of the score
answers = []
words = []
correct = 0
total = 0

# add names to the list containing game answers
for column in file:
    answers.append(column['president'])

#Jumble the game answers and place in a separate list
for i in answers:
    i = i.strip().lower().replace(' ', '')
    word = list(i)
    shuffle(word)
    words.append(word)

num = random.randint(0, len(words)-1)

# function to control the next button
def next():
    global words, answers, num, total, correct
    buttonNext.config(text = 'Next')
    # enable the restart button in case players want to start over
    buttonRestart.config(state='normal')
    # disable the next button so players can't skip over a turn
    buttonNext.config(state='disabled')
    # update screen to reflect the score
    labelNumCorrect.configure(text=correct)
    labelNumTotal.configure(text=total)
    # clear the entry field
    userInput.delete(0, END)
    # check to see if player has reached ten rounds
    if total >= 10:
        # at 10 rounds turn off check button
        buttonCheck.config(state = 'disabled')
        # Change label to final score
        labelCorrect.configure(text='Final Correct')
        # Ending message based on final score
        if correct == 10:
            labelTitle.configure(text='You are a Presidential Expert!')
        elif 7 <= correct < 10:
            labelTitle.configure(text='You know the Presidents Well!')
        elif 4 <= correct < 7:
            labelTitle.configure(text='At least you knew a few!')
        else:
            labelTitle.configure(text='Seems like you had some trouble!')
        #reset scores
        total = 0
        correct = 0
    # if under ten rounds, continue the game
    else:
        num = random.randint(0, len(words)-1)
        labelTitle.configure(text=words[num])
        buttonCheck.config(state='normal')


def ans_check():
    global words, num, answers, correct, total
    buttonNext.config(state='normal')
    if total == 0:
        labelCorrect.configure(text='Total Correct')
    total += 1
    # check to see if answer is correct
    user_input = userInput.get()
    if user_input == answers[num]:
        correct += 1
        messagebox.showinfo('Success', 'Correct')
        # update the message to show correct answer
        labelTitle.configure(text=answers[num])
    else:
        messagebox.showinfo('Error', 'Try Again')
        labelTitle.configure(text=answers[num])
    # disable buttons so only button is next to start next round
    buttonCheck.config(state = 'disabled')
    buttonRestart.config(state = 'disabled')

# function to restart the game
def restart():
    global correct, total
    labelTitle.configure(text='Good Luck')
    labelCorrect.configure(text='Total Correct')
    buttonNext.config(text='Get President')
    buttonNext.config(state = 'normal')
    buttonCheck.config(state = 'disabled')
    correct = 0
    total = 0
    labelNumCorrect.configure(text=correct)
    labelNumTotal.configure(text=total)

# function to initial screen
def initial():
    buttonCheck.config(state = 'disabled')
    buttonRestart.config(state = 'disabled')
    buttonNext.config(text = 'Start')
    labelTitle.configure(text='Unscramble the US President\'s name!')
    labelCorrect.configure(text='Can you get')
    labelNumCorrect.configure(text='10')
    labelTotal.configure(text='Out of')
    labelNumTotal.configure(text='10')

window = tkinter.Tk()
window.geometry('500x500')
window.resizable(False, False)
labelTitle = Label(window, font='times 20')
labelTitle.pack(pady=30, ipady=10, ipadx=10)
labelCorrect = Label(window, font='times 14')
labelNumCorrect = Label(window, font='times 14')
labelTotal = Label(window, font='times 14')
labelNumTotal = Label(window, font='times 14')

answer12 = StringVar()
userInput = Entry(window, textvariable=answer12)
userInput.pack(ipady=5, ipadx=5)

buttonCheck = Button(window, text="Check", width=20, command=ans_check)
buttonCheck.pack(pady=40)

buttonNext = Button(window, text='Next', width=20, command=next)
buttonNext.pack()

buttonRestart = Button(window, text='Restart', width=20, command=restart)

labelCorrect.pack(pady=5)
labelNumCorrect.pack(pady=5)
labelTotal.pack(pady=5)
labelNumTotal.pack(pady=5)
buttonRestart.pack()

initial()

window.mainloop()
