# 导入tkinter模块
import tkinter


# 创建一个窗体
zhang = tkinter.Tk()


# 第三个函数，一个按钮
def san():
    EE = tkinter.Button(zhang , text = "总之来说，这是一个十分简陋的程序，功能也比较单一，那好吧，这就是最后一个按钮了，退吧")
    
    
    # 我不知道这个是什么意思，应该是让这个按钮生效
    EE.pack()


# 和上面同理
def er():
    DD = tkinter.Button(zhang , text = "这是我的第一个GUI程序！" , command = san)
    DD.pack()



def hello():
    CC = tkinter.Button(zhang , text = "你好，我叫张峻熙" , command = er)
    CC.pack()

A = tkinter.Button(zhang , text = "你好" , command = hello)
A.pack()


# 消息循环
zhang.mainloop()

