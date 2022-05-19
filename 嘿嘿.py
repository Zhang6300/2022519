from re import A
# 导入窗口模块
import tkinter as tk

import tkinter.ttk as ttk
# 导入随机数模块
import random

# 弹窗模块
import tkinter.messagebox

# 声明窗口
top = tk.Tk()


# 将窗口设置成320x320的大小
top.geometry("320x320")

# 随机移动的函数
def heihie():
    A.place(x= random.randint(0,300) , y=random.randint(0,300) )

# 创建一个按钮,并把它放在top上，绑定随机移动的函数
A = ttk.Button(top, text= "关闭", command= heihie)

# 先让按钮生成在窗口上
heihie()

# 点击右上角的“x”的时候的函数
def guanbi():
    tkinter.messagebox.showwarning("提示","请按关闭按钮关闭窗口")

# 右上角的x动手脚
top.protocol('WM_DELETE_WINDOW' , guanbi)

# 让窗口循环显示
top.mainloop()