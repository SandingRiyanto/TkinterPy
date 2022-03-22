import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from matplotlib.pyplot import text

from pyparsing import col

# root window
root = tk.Tk()
root.title('aplikasi konversi suhu')
root.geometry('300x70')
root.resizable(False, False)

# fungsi konversi suhu
def fahrenheit_to_celcius(f):
    """conventer fahrenheit to celcius temp"""
    return (f-32) * 5/9

# frame
frame = ttk.Frame(root)

# field options
opsi = {'padx':5, 'pady':5}

# temperatur label
temp_label = ttk.Label(frame, text='Fahrenheit')
temp_label.grid(column=0, row=0, sticky='W', **opsi)

# temperatur entry
temp = tk.StringVar()
temp_entry = ttk.Entry(frame, textvariable=temp)
temp_entry.grid(column=0, row=0, **opsi)
temp_entry.focus()

# convert button
def button_konversi_teklik():
    """Menangani acara klik tombol konversi"""
    try:
        f = float(temp.get())
        c = fahrenheit_to_celcius(f)
        hasil = f'{f} Fahrenheit = {c:.2f} Celcius'
        hasil_label.config(text=hasil)
    except ValueError as error:
        showerror(title='Error', message=error)

button_konversi = ttk.Button(frame, text='Convert!')
button_konversi.grid(column=2, row=0, sticky='W', **opsi)
button_konversi.configure(command=button_konversi_teklik)

# result label
hasil_label = ttk.Label(frame)
hasil_label.grid(row=1, columnspan=3, **opsi)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)

# start the app
root.mainloop()

# grid: (kolom, baris)