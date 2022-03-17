import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Image Button Demo')

def download_kliked():
    showinfo(title='informasi', message='download klik!')

donlot_ikon = tk.PhotoImage(file='images/arrow.png')
donlot_button = ttk.Button(root, image=donlot_ikon, text='Donlot', compound=tk.LEFT, command=download_kliked)

donlot_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()