#基础语法
# print("hello world")
# a="3";b="5"
# print(a+b,int(a)+int(b))
# c=3;d=5
# print(str(c)+str(d))  #整形和字符形无法隐式转换，必须显式转换
# e=4;f=5.5
# print(e+f) #整形和实形的隐式转换
# a=7.3;b=3
# print(a//b)
# print(a==b)
import random
# dict1={
#     "wang":1,
#     "zhang":2,
#     "li":3
# }
# list1=[1,2,3,4,5,6]
# t1=(1,2,3,4,5,6)
# print(random.choice(list1))
# # print(random.choice(dict1))
# print(random.choice(t1))
# # for item in dict1.items():
# #     print(item)
# l1=[1,2,3,4]
# def gen(array):
#     for each in array:
#         yield pow(each,3)
# for each in gen(l1):
#     print(each)
# class person:
#     def __init__(self,age,weight):
#         self.age=age
#         self.weight=weight
#     def talk(self):
#         print("talking")
# class teacher(person):
#     def __init__(self,age,weight,num):
#         person.__init__(self,age,weight)
#         self.__num=num
#     def getnum(self):
#         return self.__num
#     def setnum(self,num):
#         self.__num=num
#     def __talk(self):
#         print("teaching")
#     def sing(self):
#         self.__talk()
#         print("singing")
#
# zhangsan=teacher(35,185,217)
# print(zhangsan.age,zhangsan.weight )
# # print(zhangsan.__num)
# print(zhangsan.getnum())
# zhangsan.setnum(200)
# print(zhangsan.getnum())
# zhangsan.sing()
# super(teacher,zhangsan).talk()

# #总结 面向对象：封装 继承 多继承 属性重合并，方法重从前搜索 方法重写与多态 super函数调用父类方法 私有属性与私有函数（间接引用或调用） get set方法
#__init__函数 子类__init__调用父类__init__ 高内聚低耦合准则
# f=open(r"C:\Users\wyj30751\Desktop\1.txt",mode='a+',encoding='UTF-8')
# f.write("i am fine")
# f.close()
# # f.write("hello world")
# # f.writelines("hello\nhow are you\ni'm fine")
# f.seek()
# f.close()
# x=6
# if x>5:
#     raise Exception ("溢出，x的值为{}" .format(x))
#用户自定义异常 抛出异常
# f.seek(-2,2)
# print(f.tell())
# f.close()
# import numpy
# numpy.array()
# import json
# data1 = {
#     'no' : 1,
#     'name' : 'Runoob',
#     'url' : {
#         'no' : 1,
#         'name' : 'Runoob',
#         'name2':'zhangsan'
#             }
# }
# # with open(r"C:\Users\wyj30751\Desktop\11.json",mode='a+',encoding='UTF-8') as f:
# #     json.dump(data1,f)
# with open(r"C:\Users\wyj30751\Desktop\11.json",mode='r+',encoding='UTF-8') as f:
#     f_read=f.read()
#     data=json.loads(f_read)
#     print(data['url']['name'])

# print(data['url'],type(data['url']))
# data1=str(data['url'])
# print(type(data1))
# data2=json.dumps(data1)
# print(data2,type(data2))
# data3=json.loads(data2)
# print(data3,type(data3))
# from sqlalchemy import Column,create_engine,String,Integer
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# Base=declarative_base()
# class math(Base):
#     __tablename__='math'
#     id=Column(String(20),primary_key=True)
#     name=Column(String(50))
#     ms=Column(Integer)
# engine=create_engine('mysql+mysqlconnector://root:password@localhost:3306/databasename')
# DBSession=sessionmaker(bind=engine)
# session=DBSession
# lilizong=math(id='001',name='李立宗',ms=88)
# session.add(lilizong)
# session.commit()
# session.close()
# user=session.query(math.id,math.name,math.ms).all()
# for x in user:
#     print(x)
# session.close()
#csv文件读取
# import csv
# mode=[]
# data=[]
# with open(r"C:\Users\wyj30751\Desktop\12.csv",mode='r',encoding='UTF-8') as f:
#     csvreader=csv.reader(f)
#     mode=csvreader.__next__()
#     for item in csvreader:
#         data.append(item)
#     print(mode,type(mode))
# print(data)
# for item in data:
#     for each in item:
#         print(each,type(each))
# csv文件写入
# mode=['name','num','sex']
# data=[['laoliu','220','man'],['laoba','222','woman'],['laojiu','224','man']]
# import csv
# data=[['laoshi','226','man'],['laoshiyi','227','woman']]
# with open(r"C:\Users\wyj30751\Desktop\12.csv",mode='a+',encoding='UTF-8',newline='') as f:
#     csvwriter=csv.writer(f)
#     csvwriter.writerows(data)
#
# import csv
# data=[]
# mode=[]
# with open(r"C:\Users\wyj30751\Desktop\12.csv",mode='r',encoding='UTF-8',newline='') as f:
#     csvreader=csv.reader(f)
#     mode=csvreader.__next__()
#     for item in csvreader:
#         mode.append(item)
# print(mode)
# print(data,type(data))
# for item in data:
#     print(item)
# str="hello world"
# data="how are you\niam fime\nthank you\n"
# with open(r"C:\Users\wyj30751\Desktop\14.txt",mode='w+',encoding='UTF-8',newline='') as f:
#     f.writelines(data)
# l1=range(1,10)
# print(l1)
# print(l1[0])
# print(l1[1])
# print(l1[-3::])
# i=0
# while(i<len(l1)):
#     print(l1[i])
#     i=i+1
# l1=[1,2,2.5]
# l2=[4,5,6]
# print(zip(l1,l2))
# print(type(tuple(zip(l1,l2))[0]))
# print(dict(zip(l1,l2)))
# for i in dict(zip(l1,l2)).values():
#     print(i)
# import math
# print(type(math.pi))
