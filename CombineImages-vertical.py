import os
import time

import PIL.Image as Image

#功能：将多张图片在保持原貌的情况下按顺序拼接成一张长图，或者将所有图片按等比例缩放为等宽图片，然后拼接成一张长图

foldname = '白色嫁衣'
img_marg = 5   #图片间距
IMAGES_PATH = r'E:\PYTHON\CormPicture\Py\img\%s\\'%foldname  # 图片集地址
IMAGES_FORMAT = ['.jpg', '.JPG','png','tif']  # 图片格式

start=time.time()

IMAGE_COLUMN = 1  # 合并成一张图，一列
IMAGE_SAVE_PATH = r'E:\PYTHON\CormPicture\Py\img\合集\%s.jpg'%foldname # 图片转换后的地址
# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]
image_names.sort(key=len)
print("对图片进行排序",image_names)

#自动计算新图的高，获取所有图片像素的最大宽度,将每张图片的高度做一个列表
num = len(image_names)
i = 0
height = []
width = []
while i < num:
    image = Image.open(IMAGES_PATH+'\%s'%image_names[i])
    # print("image=",image)
    width_image,height_image = image.size
    # print(width_image,height_image)
    width.append(width_image)
    height.append(height_image)
    # height = height + height_image  #高度累加
    i += 1
    # print(height,i)
# print("width = ",max(width),"height = ",height)
# print("width = ",width)
# HEIGHT = height
WIDTH = max(width)

# 计算图片居中的左像素，得到等比例缩放后图片的高列表
i = 0
width_array =[]
height_array = []
while i < num:
    width_temp = (WIDTH-width[i])/2  #计算图片居中两侧单边宽度
    width_array.append(width_temp)
    height_temp = int(WIDTH*height[i]/width[i])
    height_array.append(height_temp)
    i += 1
# print("height_array = ",height_array)
HEIGHT = sum(height_array)                              #计算所有图片的总高
# print("HEIGHT = ",HEIGHT)

# 定义图像拼接函数
def image_compose():
    to_image = Image.new('RGB', (WIDTH,HEIGHT+img_marg*num) , color=(255,255,255))  # 创建一个新的空白白色底图

    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    total_num = 0
    height_temp = 0
    for y in range(0, num):
        for x in range(1, IMAGE_COLUMN + 1):
            image = Image.open(IMAGES_PATH + '\%s' %image_names[y])
            # (IMAGE_width, IMAGE_height) = image.size
            from_image = image.resize((WIDTH, height_array[y]), Image.ANTIALIAS)    #按最宽重新调整图片大小
            to_image.paste(from_image,(0,height_temp))                              #贴图
            # to_image.paste(from_image, (int(width_array[y]),height_temp))         #当不改变图片大小时，让图片居中
            height_temp = height_temp + height_array[y]+img_marg                    #计算每张图片距离顶端的距离
            total_num += 1
            print("------第 %s 张图片 %s 粘贴成功------" % (y+1, image_names[y]))
    return to_image.save(IMAGE_SAVE_PATH)  # 保存新图

image_compose()  # 调用函数
end=time.time()
print("成功创建 %s 长图, 耗时 %s 秒"%(foldname,(end-start)))

