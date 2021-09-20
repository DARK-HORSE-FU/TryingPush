import os
import PIL.Image as Image

#功能：将多张图片在保持原貌的情况下按顺序拼接成一张横向长图

foldname = '网页首页'
IMAGES_PATH = r'E:\PYTHON\CormPicture\Py\img\%s\\'%foldname  # 图片集地址
IMAGES_FORMAT = ['.jpg', '.JPG','.png','.tif']  # 图片格式

IMAGE_ROW = 1 # 合并成一张图，一列
# IMAGE_SAVE_PATH = r'E:\PYTHON\CormPicture\Py\img\%s\%s.jpg'%(foldname,foldname)  # 图片转换后的地址
IMAGE_SAVE_PATH = r'E:\PYTHON\CormPicture\Py\img\合集\%s.jpg'%foldname # 图片转换后的地址
# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]
image_names.sort(key=len)
print(image_names)

#自动计算新图的高，获取所有图片像素的最大宽度
num = len(image_names)
i = 0
height = []
width = 0
while i < num:
    image = Image.open(IMAGES_PATH+'\%s'%image_names[i])
    width_image,height_image = image.size
    height.append(height_image)  #将高度做成一个向量，最后用于求最大高度
    width = width + width_image  #宽度累加
    i += 1
    # print(height,i)
    # print("width = ",max(width),"height = ",height)
HEIGHT = max(height)
WIDTH = width
print("height = ",height)
print("HEIGHT = ",HEIGHT)

# 计算图片居中的上像素
i = 0
height_array =[]
while i < num:
    height_temp = (HEIGHT-height[i])/2
    height_array.append(height_temp)
    i += 1

# height_array = int(height_array)
print("height_array = ",height_array)
print(type(int(height_array[1])))
# 计算有多少列
IMAGE_COLUMN_yu = len(image_names) % IMAGE_ROW  #图片总数量对行数求余
print(IMAGE_COLUMN_yu)

if IMAGE_COLUMN_yu == 0:
    IMAGE_COLUMN = len(image_names) // IMAGE_ROW
else:
    IMAGE_COLUMN = len(image_names) // IMAGE_ROW + 1
print("IMAGE_COLUMN = ",IMAGE_COLUMN)
print("image_names = ", image_names)

# 定义图像拼接函数
def image_compose():
    to_image = Image.new('RGB', (WIDTH,HEIGHT),color=(255,255,255)) # 创建一个新的白色底图

    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    total_num = 0
    width_temp = 0

    for x in range(0, IMAGE_COLUMN):
        for y in range(1, IMAGE_ROW + 1):

            image = Image.open(IMAGES_PATH + '\%s' %image_names[x])
            # print(image)
            IMAGE_width, IMAGE_height = image.size
            # print("height_p =",height_p)
            # from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * y + x-1]).resize(
            #     (IMAGE_width, IMAGE_height), Image.ANTIALIAS)
            from_image = Image.open(IMAGES_PATH + '\%s'%image_names[x])
            to_image.paste(from_image, (width_temp,int(height_array[x])))
            # to_image.paste(from_image, (width_temp,height_temp))
            width_temp = width_temp + IMAGE_width

            total_num += 1
            if total_num == len(image_names):
                break
    return to_image.save(IMAGE_SAVE_PATH)  # 保存新图
print("成功创建新图")



image_compose()  # 调用函数


