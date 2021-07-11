# 功能：爬某一网址下的图片
import os
import requests
import re

url_web = 'http://bj.121314.com/huodong/2408.html'               #图片网址，变量（需要手动修改）
foldername = '东方囍殿'                                           #存放图片的文件夹名称，变量（需要手动修改）
down_url = 'http://bj.121314.com/uploads/allimg/202010/'         #下载图片的url前缀，变量（需要手动修改,最简单的查看方法是右键，选择新标签打开，可以看到网址，也就是url）

#不知道怎么写headers的，看这篇文章 https://blog.csdn.net/qq_39380155/article/details/105584887
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
res = requests.get(url_web,headers = headers)

pattern = re.compile('src="/uploads/allimg/202010/(.*?.jpg)"',re.S)         #src=“ ”中的内容必须和下载图片url后缀完全对应，变量（需要手动修改）
results = re.findall(pattern,res.text)

saveImg_path = os.getcwd()+ '\img\%s' %foldername               # 存放图片的文件夹路径
print('saveImg_path = ',saveImg_path)
isExist = os.path.exists(saveImg_path)
print('isExist = ',isExist)
if isExist==False:
    os.mkdir(saveImg_path)                                      # 创建存放图片的文件夹
    print('创建目录成功')
else:
    print('目录已存在')

num = 1
for img_url in results:
    response =requests.get(down_url+img_url,headers = headers)
    print(response.content)
    with open(saveImg_path+'/%d.jpg'%num,'wb') as f:
        f.write(response.content)
    print("已经下载%d张 ："%num+img_url)
    num = num+1

