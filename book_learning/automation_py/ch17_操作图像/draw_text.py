#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/7 18:32
import os
from PIL import Image,ImageDraw,ImageFont
img = Image.new('RGBA',(200,200),'white')
draw = ImageDraw.Draw(img)
draw.text((20,150),'hello',fill='red')
#fontsFolder = 'FONT_FOLDER'
#arialFont = ImageFont.truetype(os.path.join('FONT_FOLDER','arial.ttf'),40)
arialFont = ImageFont.truetype('ariali.ttf',40)
draw.text((100,150),'world',fill='blue',font=arialFont)
img.save('text.png')

