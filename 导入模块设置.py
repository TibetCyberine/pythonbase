import sys#导入sys模块
import sys,time,os#一次性导入多个模块
import sys as s #导入模块并命名为system，方便调用模块
#比如
# print(s.platform)
#有一些比较特殊的库需要加上'.'之后才能import
#例如
# import urllib.error
"""
from ~ import ~
从某块调用某模块，推荐使用这种方法
后期维护容易看出调出了什么模块
或从某个库中调用了什么
from ~ import *
使用from import 调用时导入某个模块的全部的内容的方法
和java 类似
与import同理，想要一行导入多个模块时，用逗号分开就可以了
