import tkinter as tk
import cv2
import numpy as np
from PIL import Image, ImageTk


class FilterColorWnd(tk.Toplevel):
    def __init__(self, parent, image_path):
        super().__init__(parent)
        self.title("颜色过滤")
        self.geometry("1024x768")

        self.image_path = image_path

        # 创建上方frame用于显示图片
        self.top_frame = tk.Frame(self)
        self.top_frame.pack(fill=tk.BOTH, expand=True)

        # 创建label用于显示处理后的图片
        self.image_label = tk.Label(self.top_frame)
        self.image_label.pack(fill=tk.BOTH, expand=True)

        # 创建下方frame用于放置控件
        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(fill=tk.X)

        # 创建文本输入框
        self.rgb_entry = tk.Entry(self.bottom_frame)
        self.rgb_entry.pack(side=tk.LEFT, padx=5)

        # 创建按钮
        self.filter_button = tk.Button(
            self.bottom_frame, text="过滤颜色", command=self.filter_color
        )
        self.filter_button.pack(side=tk.LEFT)

    def filter_color(self):
        # 读取图片
        img = cv2.imread(self.image_path)

        # 获取用户输入的RGB值
        rgb_str = self.rgb_entry.get()
        try:
            r, g, b = map(int, rgb_str.split(","))
        except ValueError:
            tk.messagebox.showerror("错误", "请输入正确的RGB值，格式为：R,G,B")
            return

        # 创建掩码
        lower = np.array([b, g, r])  # OpenCV使用BGR顺序
        upper = np.array([b, g, r])
        mask = cv2.inRange(img, lower, upper)

        # 创建白色图像和黑色图像
        white_image = np.ones_like(img) * 255
        black_image = np.zeros_like(img)

        # 使用掩码将指定颜色变为白色，其他颜色变为黑色
        result = np.where(mask[:, :, None], white_image, black_image)

        # 转换为PIL图像
        result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(result_rgb)

        # 调整图像大小以适应label
        pil_img.thumbnail((self.top_frame.winfo_width(), self.top_frame.winfo_height()))

        # 显示结果
        photo = ImageTk.PhotoImage(pil_img)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # 保持引用
