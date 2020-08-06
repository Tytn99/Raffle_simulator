from tkinter import *
import random

W = f'''Won - Invoice from __ #({random.randint(1000, 4000)})
Congrats on your w! check your email and you will see your invoice!!'''
L = "Another L"

root = Tk()
root.title("Raffler")

def UserEntry():
    entries = list(range(1, 1600))
    numbers_generated = random.choices(entries, k=10)
    i = input('answer: ')
    your_number = int(i)
    if your_number in numbers_generated:
        print(W)
        print(f'Resulting numbers : {numbers_generated}')
    else:
        print(L)
        print(f'Resulting numbers : {numbers_generated}')

thebutton = Button(root, command=UserEntry(),text="Run RAFFLE", bg="#fff200")
thebutton.pack

root.mainloop()