from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持中英文、英文、法语、德语、韩语、日语，可以通过修改lang参数进行切换
# 参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`。
# 脚本名称不能是paddle.py，否则会报错
ocr = PaddleOCR(
    use_angle_cls=True, lang="ch"
)  # need to run only once to download and load model into memory
img_path = "./s1.png"
result = ocr.ocr(img_path, cls=True)
# 结果中的每个元素[[[24.0, 80.0], [172.0, 80.0], [172.0, 104.0], [24.0, 104.0]], ['产品信息/参数', 0.98069626]]
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# 显示结果
from PIL import Image

result = result[0]
image = Image.open(img_path).convert("RGB")
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(
    image, boxes, txts, scores, font_path="/path/to/PaddleOCR/doc/fonts/simfang.ttf"
)
im_show = Image.fromarray(im_show)
im_show.save("result.jpg")
