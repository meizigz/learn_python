import tkinter as tk
from tkinter import filedialog
from ctypes import windll
from PIL import Image, ImageTk


# 获取系统DPI设置
def get_dpi_scale():
    try:
        return windll.shcore.GetScaleFactorForDevice(0) / 100
    except:
        return 1  # 如果无法获取，则返回默认值1


# 调整图像大小
def resize_image(image_path, width, height):
    # 加载图像
    image = Image.open(image_path)
    # 调整图像大小，保持纵横比
    image.thumbnail((width, height))
    return ImageTk.PhotoImage(image)


# 打开图像文件
def openImage():
    # 打开文件对话框选择图片
    file_path = filedialog.askopenfilename(
        filetypes=[("图片文件", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )

    if file_path:
        global image_path
        image_path = file_path
        # 调整图像大小并显示
        photo = resize_image(file_path, imgFrame.winfo_width(), imgFrame.winfo_height())
        img_label.config(image=photo)
        img_label.image = photo  # 保持对图像的引用，防止被垃圾回收


# 处理图像标签大小变化
def on_img_label_resize(event):
    if image_path:
        # 获取当前的大小
        width = event.width
        height = event.height
        # 重新调整图像大小
        photo = resize_image(image_path, width, height)
        # 更新图像显示
        img_label.config(image=photo)
        img_label.image = photo  # 保持对图像的引用，防止被垃圾回收


# 查找矩形（待实现）
def findRectangle():
    pass


# 查找文本（待实现）
def findText():
    pass


# 全局变量，存储当前打开的图像路径
image_path = None

# 创建主窗口
rootWnd = tk.Tk()
rootWnd.title("图像工具")
rootWnd.geometry("800x600")

# 支持Windows下的高DPI缩放
windll.shcore.SetProcessDpiAwareness(1)
scale_factor = get_dpi_scale()

# 创建图像显示框架
imgFrame = tk.Frame(rootWnd)
imgFrame.pack(expand=True, fill=tk.BOTH)

# 创建按钮框架
btnFrame = tk.Frame(rootWnd)
btnFrame.pack(fill=tk.X)

# 创建图像标签
img_label = tk.Label(imgFrame, background="deep sky blue")
img_label.pack(expand=True, fill=tk.BOTH)
img_label.bind("<Configure>", on_img_label_resize)

# 创建按钮
tk.Button(
    btnFrame,
    text="打开图像",
    command=openImage,
    font=("宋体", int(12 * scale_factor)),
).pack(side=tk.LEFT)
tk.Button(
    btnFrame,
    text="查找矩形",
    command=findRectangle,
    font=("宋体", int(12 * scale_factor)),
).pack(side=tk.LEFT)
tk.Button(
    btnFrame, text="查找文本", command=findText, font=("宋体", int(12 * scale_factor))
).pack(side=tk.LEFT)

# 启动主循环
rootWnd.mainloop()
