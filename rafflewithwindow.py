from tkinter import *
import random
#font used - from google fonts dl to desktop for gui. link - https://fonts.google.com/specimen/Red+Rose

Win = f'''Won - Invoice - Paypal #({random.randint(100, 4000)})
Congrats on your W! check your email and you will see your invoice!!'''
L = "ANOTHER L"
chance = "You have a 0.625% chance of winning each time."
wrong = "-Invalid entry-    Enter only numbers between 1 and 1600, then re-submit raffle"

root = Tk()
root.title("Raffler")
root.configure(background="black")

label = Label(root, text="ENTER RAFFLE", bg='black', fg='white', font=('Red Rose', 18, 'bold'))
label.grid(row=1, column=0)

label2 = Label(root, text="Enter number between 1 and 1600", bg='black', fg='#edbe00', font=('Red Rose', 14, 'bold'))
label2.grid(row=2, column=0)

def UserEntry():
    entered_text = textEntry.get()
    entries = list(range(1, 1600))
    numbers_generated = random.choices(entries, k=10)
    your_number = int(entered_text)
    pulled = f'resulting numbers : {numbers_generated}'
    output.delete(0.0, END)
    if your_number in numbers_generated:
        answer = (Win + "  ,  " + pulled + " " + chance)
    elif your_number > 1600:
        answer = wrong
    elif your_number not in numbers_generated:
        answer = (L + " , " + pulled + " , " + "  " + chance)
    output.insert(END, answer, chance)

textEntry = Entry(root, width=20, bg="white", justify='center')
textEntry.grid(row=3, column=0, padx=5, pady=5)

thebutton = Button(root, command=UserEntry, text="SUBMIT RAFFLE", font=('Red Rose', 12, 'bold'), bg="#edbe00", fg="white")
thebutton.grid(row=6, column=0, padx=10, pady=10)

output = Text(root, width=105, height=3, wrap=WORD, background="black", foreground="white", font=('Red Rose', 18))
output.grid(row=7, column=0, sticky=W+E+N+S)

root.mainloop()
