import tkinter as tk
from tkinter import ttk
import cv2
import numpy as np
from PIL import Image, ImageTk


class RGB2HSVWnd(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("RGB转HSV")
        self.geometry("400x300")

        # 创建RGB滑动条
        self.r_slider = self.create_slider("R", 0)
        self.g_slider = self.create_slider("G", 1)
        self.b_slider = self.create_slider("B", 2)

        # 创建颜色显示区域
        self.color_display = tk.Canvas(self, width=100, height=100, bg="black")
        self.color_display.grid(row=0, column=3, rowspan=3, padx=10, pady=10)

        # 创建HSV值显示标签
        self.hsv_label = tk.Label(self, text="HSV: 0, 0, 0")
        self.hsv_label.grid(row=3, column=0, columnspan=4, pady=10)

        # 初始更新显示
        self.update_display()

    def create_slider(self, color, row):
        label = tk.Label(self, text=f"{color}:")
        label.grid(row=row, column=0, padx=5, pady=5)
        slider = ttk.Scale(
            self,
            from_=0,
            to=255,
            orient="horizontal",
            length=200,
            command=lambda x: self.update_display(),
        )
        slider.grid(row=row, column=1, padx=5, pady=5)
        value_label = tk.Label(self, text="0")
        value_label.grid(row=row, column=2, padx=5, pady=5)
        return {"slider": slider, "value_label": value_label}

    def update_display(self):
        # 获取RGB值
        r = int(self.r_slider["slider"].get())
        g = int(self.g_slider["slider"].get())
        b = int(self.b_slider["slider"].get())

        # 更新滑动条值标签
        self.r_slider["value_label"].config(text=str(r))
        self.g_slider["value_label"].config(text=str(g))
        self.b_slider["value_label"].config(text=str(b))

        # 更新颜色显示
        self.color_display.config(bg=f"#{r:02x}{g:02x}{b:02x}")

        # 转换为HSV
        rgb = np.uint8([[[b, g, r]]])  # OpenCV使用BGR顺序
        hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
        h, s, v = hsv[0][0]

        # 更新HSV标签
        self.hsv_label.config(text=f"HSV: {h}, {s}, {v}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RGB2HSVWnd(root)
    root.mainloop()
