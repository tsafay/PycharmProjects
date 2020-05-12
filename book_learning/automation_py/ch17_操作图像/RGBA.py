#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/7 16:12
from PIL import ImageColor,Image
import os
os.makedirs('picture',exist_ok=True)
os.chdir('picture')
print(ImageColor.getcolor('red','RGBA'))

# 打开图片
catImg = Image.open('zophie.png')
width,height = catImg.size
print(catImg.size)
print(width,height)
print(catImg.filename)
print(catImg.format_description)
catImg.save('zophie.jpg')

# 新建图片
im = Image.new('RGBA',(100,200),'red')
im.save('new.png')

# 剪裁图片
cropimg = catImg.crop((335,345,565,560))
cropimg.save('newcat.png')

# 复制粘贴图片
catcopy = catImg.copy()
catcopy.paste(cropimg,(0,0))
catcopy.paste(cropimg,(400,500))

catcopy.save('pasted.png')

catcopy_width,catcopy_height = catcopy.size
cropimg_width,cropimg_height = cropimg.size
catcpoy1 = catImg.copy()
for left in range(0,catcopy_width,cropimg_width):
    for top in range(0,catcopy_height,cropimg_height):
        print(left,top)
        catcpoy1.paste(cropimg,(left,top))
catcpoy1.save('newcat2.png')

# 调整图像大小
w,h = catImg.size
quart = catImg.resize((int(w/2),int(h/2)))
quart.save('quart.png')
svelte = catImg.resize((w,h+300))
svelte.save('svelte.png')

# 旋转和翻转图像
# 角度旋转，expand参数为True，放大图像尺寸，以适应旋转后的图形
catImg.rotate(90,expand=True).save('rotate90.png')
# 水平翻转和垂直翻转
catImg.transpose(Image.FLIP_LEFT_RIGHT).save('left_right.png')
catImg.transpose(Image.FLIP_TOP_BOTTOM).save('top_bo.png')

logo = Image.open('picture/catlogo.png')
logo_copy = logo.copy()
logo_copy.resize((100,100)).save('logo.png')