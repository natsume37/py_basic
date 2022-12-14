import tkinter as tk  # 可视化页面
# from tkinter.filedialog import *
from tkinter.messagebox import *
import webbrowser  #

urls = [
    "https://vip.parwix.com:4433/player/?url=",
    "https://jx.xmflv.com/?url=",
    "https://vip.bljiex.com/?v=",
    "https://jx.m3u8.tv/jiexi/?url=",
    "https://www.yemu.xyz/?url=",
    "https://api.okjx.cc:3389/jx.php?url=",
    "http://60jx.com/?url="
]

one = urls[0]
two = urls[1]
three = urls[2]
four = urls[3]
five = urls[4]
six = urls[5]
se = urls[6]


# 子标签


def author():
    showinfo(title='作者', message='夏目&青一\n2.1')


def user():
    showinfo(title='说明', message='浏览器复制想要看的链接到文本框')


def problem():
    showinfo(title='问题', message='解析失败后请尝试其他线路\n使用过程有如何问题都可以直接联系作者')


# 界面可视化
root = tk.Tk()
menubar = tk.Menu(root)
fmenu = tk.Menu(menubar)
fmenu.add_cascade(label='关于', command=author, font=8)
fmenu.add_cascade(label='说明', command=user, font=8)
fmenu.add_cascade(label='问题', command=problem, font=15)
menubar.add_cascade(label='帮助', font=10, menu=fmenu)
# 保持
root['menu'] = menubar

# 格式话提示框
root.geometry('600x300+400+200')
l1 = tk.Label(root, text='  播放接口：', font=('Arial', 12))
l1.grid()

l2 = tk.Label(root, text='  播放链接：   ', font=('Arial', 12))
l2.grid(row=7, column=0)

t1 = tk.Entry(root, text='', width=50)
t1.grid(row=7, column=1)

# 消息循环
var = tk.StringVar()
var.set(six)  # 设置默认值为 six
r1 = tk.Radiobutton(root, text='播放接口(b番剧)', variable=var, value=one)
r1.grid(row=0, column=1)
r2 = tk.Radiobutton(root, text='播放接口2       ', variable=var, value=two)
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root, text='播放接口3       ', variable=var, value=three)
r3.grid(row=2, column=1)
r4 = tk.Radiobutton(root, text='TV解析4        ', variable=var, value=four)
r4.grid(row=3, column=1)
r5 = tk.Radiobutton(root, text='夜幕解析        ', variable=var, value=five)
r5.grid(row=4, column=1)
r6 = tk.Radiobutton(root, text='ok解析(推荐)  ', variable=var, value=six)
r6.grid(row=5, column=1)


def bf():
    webbrowser.open(var.get() + t1.get())


def del_text():
    t1.delete(0, 'end')


b1 = tk.Button(root, text='播放', font=('Arial', 12), width=8, command=bf)
b1.grid(row=8, column=1)

b2 = tk.Button(root, text='清除', font=('Arial', 12), width=8, command=del_text)
b2.grid(row=9, column=1)


# 热键
def bf(bf):
    webbrowser.open(var.get() + t1.get())


root.bind('<Return>', bf)

root.mainloop()
