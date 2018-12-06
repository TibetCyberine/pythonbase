'''1.创建一个空列表，命名为names,往里面添加old_driver,rain,jack,shanshan,peiqi,black_girl 元素
2.往names列表里black_girl前面插入一个alex
3.把shanshan的名字改成中文，姗姗
4.往names列表里rain的后面插入一个子列表，[oldboy, oldgirl]
5.返回peiqi的索引值
6.创建新列表[1,2,3,4,2,5,6,2],合并入names列表
7.取出names列表中索引4-7的元素
8.取出names列表中索引2-10的元素，步长为2
9.取出names列表中最后3个元素
10.循环names列表，打印每个元素的索引值，和元素
11.循环names列表，打印每个元素的索引值，和元素，当索引值 为偶数时，把对应的元素改成-1
12.names里有3个2，请返回第2个2的索引值。不要人肉数，要动态找(提示，找到第一个2的位置，在此基础上再找第2个)
13.现有商品列表如下:
    products = [ ['Iphone8',6888],['MacPro',14800], ['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799] ]
    需打印出这样的格式：

    ---------商品列表----------
    
0. Iphone8    6888
    
1. MacPro    14800
    
2. 小米6    2499
    
3. Coffee    31
    
4. Book    80
    
5. Nike Shoes    799
14. 写一个循环，不断的问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里， 最终用户输入q退出时，打印购物车里的商品列表'''
#1
names=["old_driver",'rain','jack','shanshan','peiqi','black_girl']
print(names)
print('-----------------------------------------------------')
#2
names.insert(-1,"alex")#插入函数前面的数字，是指把要插入的元素
#放在这个数字序号的元素的前面，所以设置为-1时，意思就是
#把这个元素放在最后一个元素的前面，也就是倒数第二个。如果
#输入的数是正整数且大于旧列表的元素个数，则默认把这个元素
#放在新列表的最后一位，如果是负数超出旧列表范围，则默认放在第一位
print(names)
print('----------------------------------------------------')
#3
for i in range(len(names)):
    if(names[i]=="shanshan"):
        names[i]="珊珊"
print(names)
#不用遍历的话有什么好的办法呢？我暂时还想不到
#4
names.insert(2,['oldboy','oldgirl'])
print(names)
print("--------------------------------------------------")
#5
print(names.index('peiqi'))
print('---------------------------------------------------')
#6
lisy=[1,2,3,4,2,5,6,2]
names+=lisy
print(names)
print('--------------------------------------------------')
#7&8
print(names[4:8],sep=' ')
print(names[2:11:2],sep=" ")
#names[m:n:k],m表示起始元素序号
#n表示终点元素序号，始终不在取值的范围内
#所以如果要去2到5就要写成2：6
#k是取元素的步长，不写默认是1
#9
name=names.copy()
print(names)
print(names[-3:])
print('--------------------------------------------------9')
#10
for i in range(len(names)):
    print(names[i],i,sep=' ')
print("------------------------------------------------")
for i in range(len(names)):
    if(i%2==0):
        names[i]=-1
    print(names[i],i,sep=" ")
print('-------------------------------------------------')
#11
print(name)
n=0
for i in range(len(name)):
    if(name[i]==2):
        n=n+1
        if(n==2):
            break
print(i)
#12
products = [ ['Iphone8',6888],['MacPro',14800], ['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799] ]
print("----------商品列表------------")
for i in range(len(products)):
    print(i,'. ',products[i][0],"    ",products[i][1])
#14
shopcar=[]
print(shopcar)
for i in range(1000):
    m=int(input('请输入您喜欢的商品的编号以放进购物车'))
    if(m=="q"):
        print("感谢您的使用")
        break
    shopcar.append(products[m])
print(shopcar)
