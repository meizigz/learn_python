import tkinter as tk
import tkinter.ttk as ttk


def newWindow():
    # 创建新窗口
    newWnd = tk.Toplevel(rootWnd)
    newWnd.title("New Window")  # 设置新窗口标题
    newWnd.geometry("300x100")  # 设置新窗口大小

    # 创建标签
    ttk.Label(newWnd, text="This is a new window!").pack()
    # 创建按钮，点击时关闭新窗口
    ttk.Button(newWnd, text="Close", command=newWnd.destroy).pack()


# 创建主窗口。只允许创建一个主窗口。
rootWnd = tk.Tk()
rootWnd.title("Hello World")  # 设置窗口标题
rootWnd.geometry("400x100")  # 设置窗口大小

# 通过tk创建一个整型变量用于计数,初始值为0。简化变量变化时，更新UI。
count = tk.IntVar(value=0)

# 创建标签显示计数值。最后必须调用布局才会显示在窗口上。
ttk.Label(rootWnd, textvariable=count).pack()

# 创建按钮，点击时增加计数值
ttk.Button(rootWnd, text="Counter", command=lambda: count.set(count.get() + 1)).pack()
# 创建按钮，点击时创建新窗口
ttk.Button(rootWnd, text="New window", command=newWindow).pack()

# 启动主事件循环
rootWnd.mainloop()
