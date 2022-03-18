import imp
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from cv2 import exp

from numpy import pad

# root window
root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('entry value')

email = tk.StringVar()
passw = tk.StringVar()

def login_cek():
    """callback when the login button kliked"""
    pesan = f'your email: {email.get()} and password: {passw.get()}'
    showinfo(title='Imformation', message=pesan)

# sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# email
email_label = ttk.Label(signin, text="Email Address:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=passw, show="*")
password_entry.pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Login", command=login_cek)
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()