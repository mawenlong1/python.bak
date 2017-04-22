# -*- coding: utf-8 -*-
# @Author: AengusMa
# @Date:   2017-03-24 15:01:42
# @Last Modified by:   AengusMa
# @Last Modified time: 2017-03-24 15:58:37
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.io as sio  
from enthought.mayavi import mlab
#绘制3D曲面图
def demo01():
	fig = plt.figure()
	ax = Axes3D(fig)
	X = np.arange(-4, 4, 0.25)
	Y = np.arange(-4, 4, 0.25)
	X, Y = np.meshgrid(X, Y)
	Z = (X-Y+1)/2
	# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
	ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
	plt.show()
#绘制3维散点图
def demo02():
	mat1 = '4a.mat' #这是存放数据点的文件，需要它才可以画出来。上面有下载地址
	data = sio.loadmat(mat1)
	m = data['data']
	x,y,z = m[0],m[1],m[2]
	ax=plt.subplot(111,projection='3d') #创建一个三维的绘图工程
	#将数据点分成三部分画，在颜色上有区分度
	ax.scatter(x[:1000],y[:1000],z[:1000],c='y') #绘制数据点
	ax.scatter(x[1000:4000],y[1000:4000],z[1000:4000],c='r')
	ax.scatter(x[4000:],y[4000:],z[4000:],c='g')
	ax.set_zlabel('Z') #坐标轴
	ax.set_ylabel('Y')
	ax.set_xlabel('X')
	plt.show()
if __name__ == "__main__":
	demo03()
