#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/6 10:26
'多线程xkcd下载程序'
import requests,os,bs4,threading

os.makedirs('xkcd',exist_ok=True)

def downloadXkcd(startComic,endComic):
    for urlNumber in range(startComic,endComic):
        # 下载网页
        print('Downloading page http://xkcd.com/%s...' %(urlNumber))
        res = requests.get('http://xkcd.com/%s'  %(urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text,'lxml')

        # 查找图片的url
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # 下载图片
            print('Downloading image %s...' %(comicUrl))
            res = requests.get('https:'+comicUrl)
            res.raise_for_status()

            # 保存图片到文件夹
            imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# TODO: 创建多线程对象
downloadThreads = []
for i in range(0,1400,100):
    downloadThread = threading.Thread(target=downloadXkcd,args=(i,i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# TODO: 等待多线程结束
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')