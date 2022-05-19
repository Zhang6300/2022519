#创建一个下拉式菜单
import tkinter as tk
import tkinter .messagebox
#创建主窗口
win = tk.Tk()
win.config(bg='#87CEEB')
win.title("C语言中文网")
win.geometry('450x350+300+200')

#创建主目录菜单（顶级菜单）
顶上的菜单横条 = tk.Menu (win)

#在顶级菜单上新增"文件"菜单的子菜单，同时不添加分割线
二级菜单 = tk.Menu (顶上的菜单横条, tearoff=False)

#新增"文件"菜单的菜单项
二级菜单.add_command (label="新建")
二级菜单.add_command (label="打开")
二级菜单.add_command (label="保存")
# 添加一条分割线
二级菜单.add_separator ()
二级菜单.add_command (label="退出",command=win. quit)
#在主目录菜单上新增"文件"选项，并通过menu参数与下拉菜单绑定
顶上的菜单横条.add_cascade (label="文件",menu=二级菜单)

# 将主菜单设置在窗口上
win.config (menu=顶上的菜单横条)
# 显示主窗口
win.mainloop()