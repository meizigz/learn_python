from PIL import Image, ImageTk
from ctypes import windll


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


def enableHighDPI():
    windll.shcore.SetProcessDpiAwareness(1)
    scale_factor = get_dpi_scale()
    return scale_factor
