from tkinter import *
from tkinter import ttk

root = Tk()

root.title("测试")
li = ['c', 'python', 'java']
movie = ['CSS', 'HTML']

Label = ttk.Label(root, text="点我", font=20)
Label.grid(row=0, column=0)

root.mainloop()
