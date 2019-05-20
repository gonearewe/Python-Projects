from os import environ
from os import path
from os import mkdir
from os import system
from easygui import enterbox
from easygui import msgbox
ini="""[global] 
index-url = https://pypi.doubanio.com/simple/ 
[install] 
trusted-host=pypi.doubanio.com 
"""  
pippath=environ["USERPROFILE"]+"\\pip\\"  

if not path.exists(pippath):  
    mkdir(pippath)  


with open(pippath+"pip.ini","w+") as f:  
    f.write(ini) 


try:
    mod_name=enterbox("请输入你想要安装的模块的名称",'pip installer',"确定")
    system('pip install --user '+mod_name)
except TypeError:
    msgbox("请输入正确的模块名","pip installer")


