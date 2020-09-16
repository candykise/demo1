# a = 32
# b = 2
#判断 if
# if a == 1:
#     print("a是自然数")
# #if else 
# if a > b:
#     print("a比b大")
# else:
#     print("b更大")
#if elif else
# a = int(input("请输入你的年龄："))
# if a > 20 and a <= 30:
#     print("你还年轻")
# elif a > 30 and a <= 40:
#     print("你该结婚生子了")
# elif a > 40 and a <=50:
#     print("你已经不年轻了")
# # else:
# #     print("你该退休了")
# a = input("请输入：")
# # if a == "":
# #     print("请输入数字")
# # if a in "0123456789":
# #     a = int(a)
# # else:
# #     print("请输入正确的数字")
# #     exit()
# # if a > 5:
# #     print("大")
# # else:
# #     print("小")
# int(a)
# if a in ["你好，今天你吃了吗",1,2,3,4,5]:
#     print("a是字符串")
# elif a in "013456789":
#     print("a是数字")
# else:
#     print("a是其他")

# a = "你好"
# if type(a) is int:
#     print("是数字")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("是其他")

#循环
# a = 1
# while a < 10:
#     print("哈哈哈")
#     a = a + 1
"""
现在有十个学生的成绩，需要录入到系统中，
这十个人分别是：张三、李四、王麻子、浪晋、流云、希希、小梁、二狗、陈平安、亚索
并且名字和成绩需要对应上。
而且大于60的和小于60的需要分开存放。
"""
 
highsorce = {}
lowsorce = {}
studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","亚索"]
a = 0
while a < len(studentlist):
    sorce =  float(input("请输入"+ studentlist[a] + "的成绩："))
    if sorce <= 60:
        highsorce[studentlist[a]]=sorce
    else:
        lowsorce[studentlist[a]]=sorce
    a = a + 1
print("高分组:",highsorce)
print("低分组:",lowsorce)


# b = {"name":"candy","age":"16"}
# b.update(high="168cm")
# print(b)



 


# a = input("请输入你的姓名：")
# b = input("请输入你的年龄：")
# c = input("请输入你的性别：")
# d ={"name":a,"age":b,"sex":c}
# print(d)

