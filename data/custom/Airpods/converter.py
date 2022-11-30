import sys
import os
files = os.listdir("./source")
for file in files: #遍历文件夹
    filename = file.split('.')[0]
    path = "./source"+"/"+filename
    try:
        os.rename(path+".jpg",path+".png")
    except Exception as e:
        print(e)