from tkinter import *
import random

Win = f'''Won - Invoice from __ #({random.randint(100, 4000)})
Congrats on your w! check your email and you will see your invoice!!'''
L = "Another L"
chance = "You have a 0.625% chance of winning each time."

root = Tk()
root.title("Raffler")
root.configure(background="black")

label = Label(root, text="ENTER RAFFLE", bg='black', fg='white', font=('rose', 18, 'bold'))
label.grid(sticky=W)

def UserEntry():
    entered_text = textEntry.get()
    entries = list(range(1, 1600))
    numbers_generated = random.choices(entries, k=10)
    your_number = int(entered_text)
    pulled = (f'resulting numbers : {numbers_generated}')
    output.delete(0.0, END)
    if your_number in numbers_generated:
        answer = (Win, pulled)
    else:
        answer = (L, pulled)
    output.insert(END, answer)

textEntry = Entry(root, width=20, bg="white")
textEntry.grid(sticky=W)

thebutton = Button(root, command=UserEntry,text="RUN RAFFLE", font=('rose', 18, 'bold'), bg="#ffe600", fg="white")
thebutton.grid(sticky=W)

label2 = Label(root, text="Result: ", bg='black', fg='white', font=('rose', 12, 'bold'))
label2.grid(sticky=(W))

output = Text(root, width=88, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0)

root.mainloop()
