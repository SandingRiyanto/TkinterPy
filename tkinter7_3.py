import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label

root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Label Widget IMAGE')

# show a label
label = Label(root, text='This is a label', font=("Helvetica", 14))

# display image
foto = tk.PhotoImage(file='images/bg.png')
bg_foto = ttk.Label(root, image=foto, padding=5)

# call variable
bg_foto.pack()
label.pack(ipadx=10, ipady=10)

root.mainloop()