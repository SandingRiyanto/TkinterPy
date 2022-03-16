import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Demo Button')

# exit button
exitButton = ttk.Button(root, text='Keluar', command=lambda:root.quit())

exitButton.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()
# kj