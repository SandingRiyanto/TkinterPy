# 3 Ways to Set Options for a Tk Themed Widget
# 1--------------------------------------------
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
ttk.Label(root, text='Hi, there').pack()

root.mainloop()

# 2--------------------------------------------
import tkinter as tk
from tkinter import ttk


root = tk.Tk()

label = ttk.Label(root)
label['text'] = 'Hi, there'
label.pack()

root.mainloop()

# 3----------------------------------------
import tkinter as tk
from tkinter import ttk


root = tk.Tk()

label = ttk.Label(root)
label.config(text='Hi, there')
label.pack()

root.mainloop()