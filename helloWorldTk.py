import tkinter as tk
from tkinter import ttk

window= tk.Tk()

label1=tk.Label(window, text='Hello')
label2=tk.Label(window, text='World')

label1.grid(column=0, row=0)
label2.grid(column=1, row=0)
window.mainloop()
