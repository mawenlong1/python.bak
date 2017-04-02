from PIL import Image
import numpy as np
import matplotlib.image as mpimg
#将rgb转灰度图像
def rgb2gray(img):
	pil_im = Image.open(img)
	gray_cat = pil_im.convert('L')
	gray_name = img.split('.')[0]+".png"
	gray_cat.save(gray_name)
	return gray_name

#改变图片的大小图片
def resize(img,width, height):
	im = Image.open(img)
	out = im.resize((width, height),Image.ANTIALIAS)
	img_name = img.split('.')[0]+"_aa."+img.split('.')[1]
	out.save(img_name)
	return img_name
#数组转为图像
def array2img(img):
	im = Image.fromarray(img)
	img_name = '3.png'
	im.save(img_name)
	return img_name
#将图像装数组z
def img2array(img):
	img = rgb2gray(img)
	img = resize(img,28,28)
	im = Image.open(img)
	im_array = np.array(im)
	m=28
	n=28
	for i in range(m):
		for j in range(n):
			im_array[i][j] =255- im_array[i][j]
	return im_array
	
