from pdf2image import convert_from_path
from easygui import  fileopenbox
from easygui import  diropenbox
from easygui import  enterbox
from easygui import  msgbox
from os import mkdir
try:
    file=fileopenbox("请选择要进行转换的pdf文件","pdf转换器 by瓜大-18-黄磊")
    if file==None:
        raise ZeroDivisionError
    output=diropenbox("请选择要保存的位置","pdf转换器 by瓜大-18-黄磊")
    print(output)
    if output==None:
        raise ZeroDivisionError
    img_name=enterbox('请输入输出文件的名字',"pdf转换器 by瓜大-18-黄磊")
    if img_name==None:
        raise ZeroDivisionError
    path=output+'\\'+img_name
    mkdir(path)
    convert_from_path(file,200,path,fmt="JPEG",output_file=img_name,thread_count=4)
except:
    msgbox("啊欧，程序退出了哦","pdf转换器 by瓜大-18-黄磊")
