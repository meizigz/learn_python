import tkinter as tk
from PIL import ImageGrab, ImageTk
import pyautogui


class ScreenshotTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-alpha", 0.3)  # 设置窗口透明度
        self.root.attributes("-fullscreen", True)  # 全屏显示
        self.root.configure(cursor="cross")  # 设置鼠标光标为十字形

        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.start_x = None
        self.start_y = None
        self.rect = None

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y, outline="red"
        )

    def on_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_release(self, event):
        end_x = self.canvas.canvasx(event.x)
        end_y = self.canvas.canvasy(event.y)
        x1 = min(self.start_x, end_x)
        y1 = min(self.start_y, end_y)
        x2 = max(self.start_x, end_x)
        y2 = max(self.start_y, end_y)

        self.root.withdraw()  # 隐藏主窗口
        self.root.update()  # 更新窗口状态

        # 截取屏幕
        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))

        # 创建新窗口显示截图
        self.show_screenshot(screenshot)

        self.root.quit()

    def show_screenshot(self, screenshot):
        new_window = tk.Toplevel()
        new_window.title("截图预览")

        # 将PIL图像转换为Tkinter可用的格式
        tk_image = ImageTk.PhotoImage(screenshot)

        # 创建标签并显示图像
        label = tk.Label(new_window, image=tk_image)
        label.image = tk_image  # 保持对图像的引用
        label.pack()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    tool = ScreenshotTool()
    tool.run()
