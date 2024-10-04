import tkinter as tk
import tkinter.ttk as ttk


# pack布局，默认从上到下依次排列增加的控件，窗口大小不够时，会排到窗口外。
def createPackLayoutWindow():
    # 创建新窗口
    newWnd = tk.Toplevel(rootWnd)
    newWnd.title("Pack Layout")  # 设置新窗口标题
    newWnd.geometry("300x100")  # 设置新窗口大小

    ttk.Label(newWnd, text="btn1 btn1", background="green").pack(side="left")
    ttk.Label(newWnd, text="btn22 btn22", background="red").pack(side="left")
    ttk.Label(newWnd, text="btn333 btn333", background="blue").pack(side="left")
    ttk.Label(newWnd, text="btn4444 btn4444", background="yellow").pack(side="left")
    ttk.Label(newWnd, text="btn55555 btn55555", background="purple").pack(side="left")
    ttk.Label(newWnd, text="btn666666 btn666666", background="orange").pack(side="left")
    ttk.Label(newWnd, text="btn7777777 btn7777777", background="pink").pack(side="left")
    ttk.Label(newWnd, text="btn88888888 btn88888888", background="gray").pack(
        side="left",
    )
    ttk.Label(
        newWnd, text="btn999999999 btn999999999", background="white", anchor="center"
    ).pack(side="left", padx=10, ipadx=30, fill="x")


def createGridLayoutWindow():
    # 创建新窗口
    newWnd = tk.Toplevel(rootWnd)
    newWnd.title("Grid Layout")  # 设置新窗口标题
    newWnd.geometry("300x100")  # 设置新窗口大小

    for i in range(28):
        newWnd.grid_rowconfigure(i, weight=1)
    for j in range(24):
        newWnd.grid_columnconfigure(j, weight=1)

    for i in range(28):
        for j in range(24):
            ttk.Button(newWnd, text=" (" + str(i) + "," + str(j) + ")").grid(
                row=i, column=j
            )


def createPlaceLayoutWindow():
    # 创建新窗口
    newWnd = tk.Toplevel(rootWnd)
    newWnd.title("Place Layout")  # 设置新窗口标题
    newWnd.geometry("300x100")  # 设置新窗口大小

    # 使用place布局方法
    ttk.Label(newWnd, text="左上角").place(x=0, y=0)
    ttk.Label(newWnd, text="右上角").place(relx=1.0, y=0, anchor="ne")
    ttk.Label(newWnd, text="左下角").place(x=0, rely=1.0, anchor="sw")
    ttk.Label(newWnd, text="右下角").place(relx=1.0, rely=1.0, anchor="se")

    ttk.Button(newWnd, text="居中按钮").place(relx=0.5, rely=0.5, anchor="center")

    ttk.Entry(newWnd).place(relx=0.5, rely=0.2, anchor="center", width=150)

    ttk.Checkbutton(newWnd, text="选项1").place(relx=0.2, rely=0.8)
    ttk.Checkbutton(newWnd, text="选项2").place(relx=0.5, rely=0.8)
    ttk.Checkbutton(newWnd, text="选项3").place(relx=0.8, rely=0.8)

    # 演示 relwidth 和 relheight
    ttk.Label(newWnd, text="相对宽度和高度", background="lightblue").place(
        relx=0.5, rely=0.6, anchor="center", relwidth=0.8, relheight=0.2
    )

    # 创建一个框架来演示嵌套的相对尺寸
    frame = ttk.Frame(newWnd, borderwidth=2, relief="solid")
    frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)

    # 在框架内部放置一个按钮，其尺寸相对于框架
    ttk.Button(frame, text="框架内按钮").place(
        relx=0.5, rely=0.5, anchor="center", relwidth=0.6, relheight=0.6
    )


def createMixedLayoutWindow():
    # 创建新窗口
    newWnd = tk.Toplevel(rootWnd)
    newWnd.title("Mixed Layout")  # 设置新窗口标题
    newWnd.geometry("300x100")  # 设置新窗口大小

    # 使用pack创建顶部和底部的框架
    top_frame = ttk.Frame(newWnd)
    top_frame.pack(side="top", fill="x", padx=10, pady=5)

    bottom_frame = ttk.Frame(newWnd)
    bottom_frame.pack(side="bottom", fill="x", padx=10, pady=5)

    # 在顶部框架中使用grid布局
    ttk.Label(top_frame, text="用户名:").grid(row=0, column=0, padx=5, pady=5)
    ttk.Entry(top_frame).grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(top_frame, text="密码:").grid(row=1, column=0, padx=5, pady=5)
    ttk.Entry(top_frame, show="*").grid(row=1, column=1, padx=5, pady=5)

    # 在底部框架中使用pack布局
    ttk.Button(bottom_frame, text="登录").pack(side="left", padx=5)
    ttk.Button(bottom_frame, text="取消").pack(side="right", padx=5)

    # 使用place布局在窗口中央放置一个标签
    ttk.Label(newWnd, text="混合布局示例", font=("Arial", 16)).place(
        relx=0.5, rely=0.5, anchor="center"
    )


# 创建主窗口
rootWnd = tk.Tk()
rootWnd.title("Layout")
rootWnd.geometry("400x200")

ttk.Button(rootWnd, text="Pack layout", command=createPackLayoutWindow).pack()
ttk.Button(rootWnd, text="Grid layout", command=createGridLayoutWindow).pack()
ttk.Button(rootWnd, text="Place layout", command=createPlaceLayoutWindow).pack()
ttk.Button(rootWnd, text="Mixed layout", command=createMixedLayoutWindow).pack()


rootWnd.mainloop()
