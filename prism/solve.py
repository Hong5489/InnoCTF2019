from PIL import Image
black = Image.new('RGB', (22, 22), color = 'black')
image = Image.open("prism.png")
new_image = [Image.new('RGB',(22*22,22*22),color='white') for i in range(3)]
rgb_im = image.convert('RGB')
for i in range(21):
	for j in range(21):
		r, g, b = rgb_im.getpixel((i*22,j*22))
		if r == 0:
			new_image[0].paste(black,(i*22,j*22))
		if g == 0:
			new_image[1].paste(black,(i*22,j*22))
		if b == 0:
			new_image[2].paste(black,(i*22,j*22))
new_image[0].save("red.png")
new_image[1].save("green.png")
new_image[2].save("blue.png")