import requests
import pyautogui
import time
waittime = int(input("等待时间:分钟\n\n")) * 60
pyautogui.PAUSE = waittime

# 导入os模块和time模块
import os
import time

# 定义一个函数，用来ping百度，并打印结果
def ping_baidu():
    # 使用os.system()方法执行ping命令，并将结果保存到result变量中
    result = os.system('ping www.baidu.com')
    # 判断result是否为0，如果为0，表示ping成功，否则表示ping失败
    if result == 0:
          print("success")
    else:
          print('fail')
          pyautogui.moveTo(1726,1079,0.5)  #触底
          pyautogui.PAUSE = 0.5
          pyautogui.moveTo(1726,1079,0.2)  #触底
          pyautogui.moveTo(593,1048,0.5)
          pyautogui.click(588,1048)  #打开edge浏览器
          pyautogui.keyDown('alt')
          pyautogui.keyDown('space')
          pyautogui.keyDown('x')
          pyautogui.keyUp('x')
          pyautogui.keyUp('space')
          pyautogui.keyUp('alt')
          pyautogui.PAUSE = 0.5
          pyautogui.moveTo(1899,564,0.5)  #移动至network
          while(True):
               if(pyautogui.screenshot().getpixel(pyautogui.position())[0] < 90):  #判断是否是network
                    pyautogui.click(1899,564)
                    break
          pyautogui.moveTo(1785,820,0.5)  #移动到空白
          while(True):
               if(pyautogui.screenshot().getpixel(pyautogui.position())[0] == 227):
                    break

          pyautogui.moveTo(1718,722,0.5)  #注销点
          if(pyautogui.screenshot().getpixel(pyautogui.position())[0] != 254):
               pyautogui.moveTo(1630,847,0.5)
               while(True):
                    if(pyautogui.screenshot().getpixel(pyautogui.position())[0] == 254):  #判断是否是network
                         pyautogui.click(1630,847)
                         break
               pyautogui.keyDown('alt')
               pyautogui.keyDown('f4')
               pyautogui.PAUSE = 0.3
               pyautogui.keyUp('f4')
               pyautogui.keyUp('alt')
          else:
               pyautogui.moveTo(1785,820,0.5)
               pyautogui.keyDown('alt')
               pyautogui.keyDown('f4')
               pyautogui.PAUSE = 0.3
               pyautogui.keyUp('f4')
               pyautogui.keyUp('alt')



          pyautogui.moveTo(1726,1079,0.5)  #触底
          pyautogui.PAUSE = 0.5
          pyautogui.moveTo(593,1048,0.5)
          pyautogui.click(700,1048)  #打开sakura_frp
          pyautogui.moveTo(1630,847,0.5)
          if(pyautogui.screenshot().getpixel(pyautogui.position())[0] == 254):
               pyautogui.moveTo(553,466,0.5)
               pyautogui.click(553,466)
          pyautogui.moveTo(1009,355,0.5)
          pyautogui.click(1009,355)
          while(True):
               pyautogui.PAUSE = 0.5
               if(pyautogui.screenshot().getpixel(pyautogui.position())[0] != 65):
                    break
               pyautogui.click(1009,355)


# 定义一个无限循环，每隔一分钟执行一次ping_baidu()函数
while True:
    # 调用ping_baidu()函数
    ping_baidu()
    # 使用time.sleep()方法暂停60秒（即一分钟）
    time.sleep(0.5) 


# while True:
#      print(pyautogui.displayMousePosition())


# pyautogui.moveTo(1726,1079,0.5)#触底
# time.sleep(0.5)
# pyautogui.click(1726,1069)#点击网络连接处
# time.sleep(0.5)
# pyautogui.click(1571,566)#管理WLAN连接
# time.sleep(0.5)
# pyautogui.click(1601,654)#点击具体链接页面
# time.sleep(8)
# pyautogui.click(1025,519)#
# time.sleep(0.5)
# pyautogui.click(1316,1046)
# time.sleep(0.5)
# pyautogui.click(906,837)
# while True:
#     pyautogui.keyDown('t')
#     pyautogui.keyUp('t')
#     pyautogui.keyDown('alt')
#     pyautogui.keyDown('s')
#     pyautogui.keyUp('s')
#     pyautogui.keyUp('alt')
# 