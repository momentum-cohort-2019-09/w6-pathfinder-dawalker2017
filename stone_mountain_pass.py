from PIL import Image, ImageDraw


img1 = Image.new("RGBA", (601, 601), color=(65, 60, 35, 255))
draw = ImageDraw.Draw(img1)
img1.save('img1.png')

with open()
