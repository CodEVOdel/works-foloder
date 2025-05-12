import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.geometry('500x500')
root.anchor='e'
root.grid_columnconfigure(0,weight=10,minsize=100)
root.grid_columnconfigure(1,weight=2,minsize=100)
root.grid_columnconfigure(2,weight=1,minsize=150)
tk.Label(root, text="Имя:",background="#00FF00").grid(row=0, column=0,columnspan=3,sticky="ew")
tk.Entry(root,background="#005512").grid(row=1, column=1, padx=0, pady=5)
root.mainloop()