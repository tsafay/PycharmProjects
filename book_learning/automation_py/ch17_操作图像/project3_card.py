#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/7 21:11
'项目：座位卡'
import os
from PIL import Image,ImageDraw,ImageFont

# os.makedirs('sentCard',exist_ok=True)
# img = Image.open('timg.jpg')
#
# card = Image.new('RGBA',(288,360))
# card.paste(img.resize((288,360)))
# draw = ImageDraw.Draw(card)
# draw.line([(0,0),(287,0),(287,359),(0,359),(0,0)],fill='black')
# folder = 'FONT_FOLDER'
# arialfont = ImageFont.truetype(os.path.join(folder,'arial.ttf'),30)
# with open('guests.txt') as f:
#     for name in f.readlines():
#         draw.text((100,100),name.strip(),fill='blue',font=arialfont)
#         card.save(os.path.join('sentCard',name.strip())+'.png')

with open('guests.txt') as f:
    for guest in f.readlines():
        im = Image.open('timg.jpg')
        draw = ImageDraw.Draw(im)
        draw.text((50,50),guest.strip().title(),fill='blue')
        card_name = 'card_to_%s.png' % guest.strip()
        im.save(card_name)

    print('card-making work is done!')