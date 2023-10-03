#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk

root = tk.Tk()
root.title('Simple Calculator')

display = tk.Entry(root)
display.grid(row=0, column=0, columnspan=4, pady=10)


def click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))


def clear():
    display.delete(0, tk.END)


def calculate():
    equation = display.get()
    try:
        result = eval(equation)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.insert(0, "Error")


btn_1 = tk.Button(root, text='1', command=lambda: click(1))
btn_1.grid(row=1, column=0)

# 其他数字按钮...

btn_clear = tk.Button(root, text='C', command=clear)
btn_clear.grid(row=1, column=3)

btn_equal = tk.Button(root, text='=', command=calculate)
btn_equal.grid(row=4, column=3)

root.mainloop()
