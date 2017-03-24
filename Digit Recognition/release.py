import csv
from numpy import *
import operator
from PIL import Image
import numpy as np
import matplotlib.image as mpimg
import os
def loadTrainData():
	l=[]
	with open('train.csv') as file:
		lines=csv.reader(file)
		#for line in lines:
		for line in lines:
			l.append(line)
	l.remove(l[0])
	l = array(l)
	label = l[0:2000,0]
	data = l[0:2000,1:]
	return nomalizing(toInt(data)),toInt(label)
def toInt(array):
	array = mat(array)
	m,n = shape(array)
	newArray = zeros((m,n))
	for i in range(m):
		for j in range(n):
			newArray[i,j] = int(array[i,j])
	return newArray
def nomalizing(array):
	m,n = shape(array)
	for i in range(m):
		for j in range(n):
			if  array[i,j]!=0:
				array[i,j]=1
	return array	
def classify(inX, dataSet, labels, k):
	inX  = mat(inX)
	dataSet = mat(dataSet)
	labels = mat(labels)
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize,1)) - dataSet
	sqDiffMat = array(diffMat)**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()    
	classCount={}          
	for i in range(k):
		voteIlabel = labels[0,sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]
#将图像装数组z
def img2array(img):
	im = Image.open(img)
	im_array = np.array(im)
	for i in range(28):
		for j in range(28):
			im_array[i,j]=255 - im_array[i,j]
	return im_array
def test(img):
	im = img2array(img)
	l = array(im)
	test_data = nomalizing(toInt(l))
	trainData,trainLabel=loadTrainData()
	classifierResult = classify(test_data.flatten(), trainData, trainLabel, 5) 
	print ("the classifier came back with: %d." % (classifierResult))
def array2img(img,img_label,labelCount):
	im = Image.fromarray(np.uint8(img))
	img_path = './test/'+str(img_label)
	img_name = str(img_label)+'_'+str(labelCount)+'.png'
	if os.path.exists(img_path)==False:	
		os.mkdir(img_path)
	img_name = img_path + '/' +img_name
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
	return data
	
if __name__ == "__main__":
	data = loadTestData()
	m,n=shape(data) 
	trainData,trainLabel=loadTrainData()
	numberLabel={} 
	for i in range(m):
		im = data[i]
		l = array(im)
		test_data = nomalizing(toInt(l))
		classifierResult = classify(test_data.flatten(), trainData, trainLabel, 5) 
		classifierResult = int(classifierResult)
		print ("the classifier came back with: %d." % (classifierResult))
		numberLabel[classifierResult] = numberLabel.get(classifierResult,0) + 1
		for j in range(28*28):
			l[j] = 255 - int(l[j])
		img = np.array(l).reshape(28,28)		
		array2img(img,classifierResult,numberLabel[classifierResult])

	
	



