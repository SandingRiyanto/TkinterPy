# Pengikatan Perintah Tkinter
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

window_width = 600
window_height = 400

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.iconbitmap('images\opencv_icon.ico')

def button_clicked():
    print('Button clicked')


button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack()

root.mainloop()
# kj