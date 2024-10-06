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

        # 创建过滤灰色按钮
        self.filter_gray_button = tk.Button(
            self.bottom_frame,
            text="过滤灰色",
            command=lambda: self.filter_gray_or_red("gray"),
        )
        self.filter_gray_button.pack(side=tk.LEFT, padx=5)

        # 创建过滤偏红色按钮
        self.filter_red_button = tk.Button(
            self.bottom_frame,
            text="过滤偏红色",
            command=lambda: self.filter_gray_or_red("red"),
        )
        self.filter_red_button.pack(side=tk.LEFT, padx=5)

    def filter_color(self):
        # 读取图片
        img = cv2.imread(self.image_path)

        # 获取用户输入的多个RGB值
        rgb_str = self.rgb_entry.get()
        try:
            rgb_values = [list(map(int, rgb.split(","))) for rgb in rgb_str.split("-")]
        except ValueError:
            tk.messagebox.showerror(
                "错误", "请输入正确的RGB值，格式为：R,G,B R,G,B ..."
            )
            return

        # 创建掩码
        mask = np.zeros(img.shape[:2], dtype=np.uint8)
        for r, g, b in rgb_values:
            lower = np.array([b, g, r])  # OpenCV使用BGR顺序
            upper = np.array([b, g, r])
            mask |= cv2.inRange(img, lower, upper)

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

    def filter_gray_or_red(self, color_type="gray"):
        # 读取图片
        img = cv2.imread(self.image_path)

        # 转换为HSV颜色空间
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # 定义灰色和偏红色的HSV范围
        if color_type == "gray":
            # 灰色的色相不重要，饱和度低
            lower = np.array([0, 0, 1])  # 修改最小亮度为1，排除纯黑色
            upper = np.array([180, 30, 255])
        else:  # 偏红色
            # 红色在HSV中的色相范围是0-10和160-180
            lower1 = np.array([0, 50, 50])
            upper1 = np.array([10, 255, 255])
            lower2 = np.array([160, 50, 50])
            upper2 = np.array([180, 255, 255])

        # 创建掩码
        if color_type == "gray":
            mask = cv2.inRange(hsv, lower, upper)
        else:
            mask1 = cv2.inRange(hsv, lower1, upper1)
            mask2 = cv2.inRange(hsv, lower2, upper2)
            mask = cv2.bitwise_or(mask1, mask2)

        # 创建白色图像
        white_image = np.ones_like(img) * 255

        # 使用掩码将指定颜色变为白色，其他颜色保持不变
        result = np.where(mask[:, :, None], white_image, img)

        # 转换为PIL图像
        result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(result_rgb)

        # 调整图像大小以适应label
        pil_img.thumbnail((self.top_frame.winfo_width(), self.top_frame.winfo_height()))

        # 显示结果
        photo = ImageTk.PhotoImage(pil_img)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # 保持引用
