# import tkinter

# m =tkinter.Tk()

# '''widgets here'''
# m.mainloop()

# from tkinter import *
# root = Tk()
# w = Label(root, text='GeeksForGeeks.org!')
# w.pack()
# root.mainloop()

import tkinter as tk

r = tk.Tk()
r.title("Counting Seconds")
button = tk.Button(r, text="Stop", width=25, command=r.destroy)
button.pack()
r.mainloop()
