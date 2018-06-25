from wand.image import Image

import os
# from PIL import Image # 这里报错是因为import 一个文件的时候，不能重名，在windows下需要安装一个exe

def get_imlist(path):
    """返回目录中所有png图像的文件名列表"""
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".tif")]

if __name__ == '__main__':
    path = "G:/Test/6-28/HBsAg_tif/"
    listdir = get_imlist(path)

    for dir in listdir:
        print(dir)
        with Image(filename = str(dir)) as img:
            img.resize(4096,4096) # width, height
            img.save(filename = (str(dir)[:-3]+'png').replace("HBsAg_tif","HBsAg_png")) # png, jpg, bmp, gif, tiff All OK--