from PIL import Image
import csv
import numpy as np
import os
def array2img(img,img_label,labelCount):
	im = Image.fromarray(np.uint8(img))
	img_path = './test/'+str(img_label)
	img_name = str(img_label)+'_'+str(labelCount)+'.png'
	if os.path.exists(img_path)==False:	
		os.mkdir(img_path)
	img_name = img_path + '/' +img_name
	im.save(img_name)
def loadTrainData():
	l=[]
	with open('test.csv') as file:
		lines=csv.reader(file)
		for line in lines:
			l.append(line)
	l.remove(l[0])
	l = array(l)
	label = l[:,0]
	data = l[:,1:]
	m,n = shape(data)
	numberCount={}  
	for i in range(m):
		numberCount[label[i]] = numberCount.get(label[i],0) + 1
		tmp = data[i]
		for j in range(28*28):
			tmp[j] = 255 - int(tmp[j])
		img = np.array(tmp).reshape(28,28)
		#img_name = str(label[i])+'_'+str(numberCount.get(label[i]))+'.png'
		array2img(img,label[i],numberCount.get(label[i],0))
def array2img2(data,label):
	im = Image.fromarray(np.uint8(data))
	img_path = './test/'
	img_name = str(label)+'.png'
	if os.path.exists(img_path)==False:	
		os.mkdir(img_path)
	img_name = img_path + img_name
	im.save(img_name)
def loadTestData():
	l=[]
	with open('test.csv') as file:
		lines=csv.reader(file)
		for line in lines:
			l.append(line)
	l.remove(l[0])
	l = array(l)
	data = array(l)	
	m,n=shape(data) 
	for i in range(m):
		tmp = data[i]
		for j in range(28*28):
			tmp[j] = 255 - int(tmp[j])
		img = np.array(tmp).reshape(28,28)		
		array2img2(img,i)
		













