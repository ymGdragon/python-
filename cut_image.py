#-*- coding:utf-8 -*-

# 将原来4096*4096的图片切割为1024的图片

import os
from PIL import Image

def get_imlist(path):
    """返回目录中所有png图像的文件名列表"""
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".png")]

def save_change(save_dir,n,x1,y1,x2,y2):
    box = (x1,y1,x2,y2)
    region = pil_im.crop(box)

    out = region.resize((1024,1024)) # 每张图片大小为1024 * 1024
    save_dir = save_dir + str(n) + ".png"
    print(save_dir)
    out.save(save_dir)


if __name__ == "__main__":

    """
    读取的图片的路径： G:/Test/6-28/data_raw/
    结果的图片的路径： G:/Test/6-28/res/
    """
    path = "G:/Test/6-28/data_raw/"
    listdir = get_imlist(path)

    for dir in listdir:
        infile = os.path.splitext(dir)[0]
        infile = infile.replace("data_raw","res")
        save_dir = infile + "_"
        print(save_dir)

        pil_im = Image.open(dir)
        #pil_im.show()
        i = 0
        # save_change(save_dir,i, 0, 0, 2048, 2048)
        # save_change(save_dir,i+1, 2048, 0, 4096, 2048)
        # save_change(save_dir,i+2, 0, 2048, 2048, 4096)
        # save_change(save_dir,i+3, 2048, 2048, 4096, 4096)
        x1 = 0
        y1 = 0
        x2 = 1024
        y2 = 1024        
        while(x2 <= 4096 and y2 <= 4096):
            save_change(save_dir,i, x1, y1, x2, y2)
            x1 += 1024
            x2 += 1024
            i += 1
            save_change(save_dir,i, x1, y1, x2, y2)
            x1 += 1024
            x2 += 1024
            i += 1
            save_change(save_dir,i, x1, y1, x2, y2)
            x1 += 1024
            x2 += 1024
            i += 1
            save_change(save_dir,i, x1, y1, x2, y2) 
            i += 1
            x1 = 0
            y1 += 1024
            x2 = 1024
            y2 += 1024