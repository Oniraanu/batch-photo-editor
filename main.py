import glob
from PIL import Image, ImageEnhance

image_path = glob.glob("/home/olubunmi/Pictures/*.jpg")
for image in image_path:
    my_image = Image.open(image)
    brightness = ImageEnhance.Brightness(my_image).enhance(-0.1)
    contrast = ImageEnhance.Contrast(brightness).enhance(0.3)
    contrast.save(image)
