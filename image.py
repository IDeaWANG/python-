from PIL import Image
im = Image.open('1.png')#图片
im.show()
box = (10,20,30,40)#(x1,y1,x2,y2)
crop_img = im.crop(box)
crop_img.save('2.png')
