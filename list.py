list =['abc',123,2.5,]
tinylist = [123,'qwe']
list3=[123,56,5.0]
lisr=['123','asd','1345','dfg','128','qwe']
liss=['123','qwe','asdf','zxc']
list9=[123,546,3135,88,313]
print(list)#输出整个列表
print(list[0])#输出列表的第一个元素
print(list[0:-1])#输出列表中第一个到最后一个的元素，
#包含第一个，不包含最后一个
print(list[1:2])#输出列表中第二个到第三个元素
#包含第二个，不包含第三个
print(list[1:])#输出列表中从第二个开始到最后的元素
print(list*2)#输出两次列表
print(list+tinylist)#链接两个列表
print('--------------------------------------------')
print(list3)
del list3[2]#删除list3列表中的第三个元素
print(list3)
print('--------------------------------------------')
print(list)
print(len(list))#输出列表list的长度
print('--------------------------------------------')
print(list)
print(123 in list )#检验元素是否在列表中
print('--------------------------------------------')
print(list)
for x in list:
    print(x,end="")#逐个输出list列表中的元素
print('\n')
print('--------------------------------------------')
print(list)
list+=['sadaf','asfafs','asfasf',12546]#列表拼接操作
print(list)
print('--------------------------------------------')
list4=[list3,tinylist]
print(list4)#列表嵌套操作
print('--------------------------------------------')
list3.append('x')#在列表末尾添加一个元素“x”
print(list3)
print('---------------------------------------------')
print(lisr)
print(lisr.count('123'))#“123”在列表lisr中出现的次数为1
print('---------------------------------------------')
print(list)
list.extend(['5','lll','lll'])
print(list)
print('---------------------------------------------')
print(list)
list.append('1231')
print(list)
print('---------------------------------------------')
print(list)
list.extend('33')
print(list)#exend只能追加序列，所以会将33拆分成两个3，
#而append在这方面就自由多了。
print('---------------------------------------------')
print(lisr)
lisr.remove("asd")
print(lisr)#删除lisr列表中与“asd”相匹配的元素
print("--------------------------------------------")
print(liss)#先打印一个liss列表做对照
liss.reverse()
print(liss)
#反转liss列表顺序
print('--------------------------------------------')
#列表复制操作
print(list)
list6=list.copy()
print(list6)
print('-------------------------------------------')
print(list)
list.pop(0)#删除列表中第一个元素
#pop函数括号内的数值就是要删除的元素在列表中的序号
#不写默认为-1，就是默认删除掉最后一个元素
list_pop=list.pop(0)#list.pop(0)是被删掉的元素的返回值
print(list_pop)#打印出被删除掉的元素
print(list)
print('------------------------------------------')
print(list)
list.insert(1,'2')#插入函数，括号内前一个数字
#用来设置插入元素在新列表中的序号，后面的字符是新元素
print(list)
print('------------------------------------------')
print(list9)
list9.sort()
print(list9)
'''
list.sort(cmp=None, key=None, reverse=False)排序函数，三个参数，reverse参数默认是False,升序
reverse=true就是降序号,排序不支持字符和数字混合排序。
'''
