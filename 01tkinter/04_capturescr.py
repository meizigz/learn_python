import tkinter as tk
from PIL import Image, ImageTk, ImageGrab, ImageEnhance
import pyautogui


class ScreenshotTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-alpha", 0.3)
        self.root.attributes("-fullscreen", True)
        self.root.configure(cursor="cross")

        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.start_x = None
        self.start_y = None
        self.rect = None
        self.magnifier = None

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.canvas.bind("<Motion>", self.update_magnifier)

        # 添加新的属性
        self.is_dragging = False

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y, outline="red"
        )
        self.is_dragging = True

    def on_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

        # 在拖动时更新放大镜
        self.update_magnifier(event)

    def on_release(self, event):
        self.is_dragging = False
        end_x = self.canvas.canvasx(event.x)
        end_y = self.canvas.canvasy(event.y)
        x1 = min(self.start_x, end_x)
        y1 = min(self.start_y, end_y)
        x2 = max(self.start_x, end_x)
        y2 = max(self.start_y, end_y)

        self.root.withdraw()
        self.root.update()

        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        screenshot.save("screenshot.png")

        self.root.quit()

    def update_magnifier(self, event):
        # 只有在未拖动或正在拖动时更新放大镜
        if not self.is_dragging and self.magnifier:
            self.canvas.delete(self.magnifier)

        if self.is_dragging or not self.magnifier:
            x, y = event.x, event.y
            magnifier_size = 100
            zoom_factor = 2

            screen = ImageGrab.grab(bbox=(x - 25, y - 25, x + 25, y + 25))
            zoomed = screen.resize((magnifier_size, magnifier_size), Image.LANCZOS)
            enhancer = ImageEnhance.Sharpness(zoomed)
            zoomed = enhancer.enhance(1.5)

            photo = ImageTk.PhotoImage(zoomed)
            self.magnifier = self.canvas.create_image(
                x + 50, y - 50, image=photo, anchor=tk.NW
            )
            self.canvas.image = photo

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    tool = ScreenshotTool()
    tool.run()
