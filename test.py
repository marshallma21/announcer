from PIL import Image,ImageOps
import pytesseract
import pyautogui
from paddleocr import PaddleOCR, draw_ocr
import cv2
import matplotlib.pyplot as plt

# 打开图片
image = Image.open('error_1725089336.png')


# capture_x = 700 + 485
# capture_y = 820 - 130
# capture_width = 100
# capture_height = 50

# screenshot = pyautogui.screenshot()
# # Crop the screenshot to the specified capture region
# capture_screenshot = screenshot.crop((capture_x, capture_y, capture_x + capture_width, capture_y + capture_height))
# rgb_image = capture_screenshot.convert('RGB')

# # 图片颜色反转
# inverted_image = ImageOps.invert(rgb_image)
# inverted_image.save('inverted_image2.png')

ocr = PaddleOCR(use_angle_cls=True, lang='ch')
image_path = 'error_1725105140.png'
img = cv2.imread(image_path)


# 使用 pytesseract 提取文字
# text = pytesseract.image_to_string(inverted_image)

result = ocr.ocr(img, cls=True)


print(result[0][0][1][0])