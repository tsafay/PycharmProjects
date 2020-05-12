#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/7 18:18
from PIL import Image,ImageDraw
img = Image.new('RGBA',(200,200),'white')
draw = ImageDraw.Draw(img)
draw.line([(0,0),(199,0),(199,199),(0,199),(0,0)],fill='black')
draw.rectangle((20,30,60,60),fill='blue')
draw.ellipse((120,30,160,60),fill='red')
draw.polygon(((57,87),(79,62),(94,85),(120,90),(103,113)),fill='brown')
for i in range(100,200,10):
    draw.line([(i,0),(200,i-100)],fill='green')
img.save('draw.png')
