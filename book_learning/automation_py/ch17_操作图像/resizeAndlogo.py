#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/7 17:10
'项目：添加图标'
'''
调整图片大小，并在每张图片角上增加一个徽标水印；
'''
import os
from PIL import Image

os.makedirs('logos',exist_ok=True)

fit_size = 300
logo_img = Image.open('logo.png')
logo_width,logo_height = logo_img.size


# TODO: 查找工作目录所有图片
for filename in os.listdir('picture'):
    if not filename.endswith('.png') or filename.endswith('.jpg'):
        continue
    image = Image.open(os.path.join('picture',filename))
    width,height = image.size

    # TODO: 检查所有需要剪裁的图片
    if width > fit_size or height > fit_size:
        # TODO: 计算新的尺寸
        if width > height:
            height = int((fit_size / width) * height)
            width = fit_size
        else:
            width = int((fit_size / height) * width)
            height = fit_size

        # TODO: 剪裁图片
        print('Resizing %s...' % filename)
        image = image.resize((width,height))

    # TODO: 加入logo
    if min(width,height) >= 200:
        print('Adding logo to %s...' %(filename))
        image.paste(logo_img,(width-logo_width,height-logo_height),logo_img)

        # TODO: 保存图片
        image.save(os.path.join('logos',filename))