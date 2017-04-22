# -*- coding: utf-8 -*-
# @Author: AengusMa
# @Date:   2017-04-22 10:58:41
# @Last Modified by:   AengusMa
# @Last Modified time: 2017-04-22 13:46:25
#根据歌曲的id下载歌词，歌词保存到默认的目录下，歌词的命名为‘歌曲名-歌手.lrc’.
import urllib.request
import json
import re
def getMusciLyric(id):
	url = 'http://music.163.com/api/song/media?id='+str(id)
	response = urllib.request.urlopen(url)
	jscontent = response.read().decode('utf-8')
	jsDict = json.loads(jscontent)
	if('lyric' in jsDict):
		lyric = jsDict['lyric']
		fileName = getMusciInfo(id)[0]+'-'+getMusciInfo(id)[1]+'.lrc'
		fo = open(fileName,"wb+")
		aa = str(lyric)
		aa = aa.encode('utf-8')
		fo.write(aa)
		fo.close()
		print ('success')
	else:
		print ('failed!')
def getMusciInfo(id):
	url = 'http://music.163.com/song?id='+str(id)
	response = urllib.request.urlopen(url)
	content = response.read().decode('utf-8')
	info = re.match(r'[\s\S]*(<title>([\s\S]*)</title>)[\s\S]*',content).group(2)
	name = info.split('-')[0]
	songer = info.split('-')[1]
	return name,songer
if __name__ == '__main__':
	id = input('输入要下载的歌词的id:')
	getMusciLyric(id)
	