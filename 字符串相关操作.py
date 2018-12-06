#认识数据类型以及一些相关知识的用法
str = "abcdefg"
print(str)#输出str
print(str+str)#输出strstr
print(3*str)#数字*字符串表示字符串重复
#相应的数字的次数
print(str+3*str)#输出str+3*str
print("--------------------------------")
print(str,str,str,str,sep="\n")#需要连续输出好几个字符串时，
#可以用sep来设置间隔，比手动输入\n或者空格来的快&方便
#sep只控制多个字符之间的东西
print("123")
print("123")#多行print会自动分行输出，如果不想分行输出，使用end
print("123",end="")
print("123",end="\n")#end只控制输出字符后的东西
print("----------------------------------")
#强制类型转换
print(int("123")+5)#字符串123转换成数字123
#数字转换成字符加上引号就可以了。
print("----------------------------------")
print(str[0])#输出字符串中第一个字符
print(str[0:3])#[m:n]意思是输出字符串中从第（m+1）个字符输出
#（n-m）个字符m,n皆为正数
print(str[2:5])#从第3个字符开始输出（5-2）3个字符
print(str[0:-1])#表示从第一个字符到倒数第二个字符
print("----------------------------------")
print("hello world\n sanches")
print(r"hello world\n sanches")#取消转义符\的作用，变成普通字符
