import cv2
import easyocr

image_path = "./water-meter-reading.jpg"

img = cv2.imread(image_path)

reader = easyocr.Reader(["en"], gpu=False)

text_ = reader.readtext(img)

threshold = 0.25
# draw bbox and text
for t_, t in enumerate(text_):

    bbox, text, score = t
    print(text)
