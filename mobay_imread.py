# #
# #
# #
# #
# # room = {"account":"账目","dream":"梦想","abuse":"虐待","door":"门","fox":"狐狸",
# #
# #         "ball":"气球","book":"书","cat":"猫","horse":"马","stallion":"雄马",
# #
# #         "donkey":"驴","hinny":"驴骡","mule":"马骡","cattle":"牛","bull":"雄牛",
# #
# #         "ox":"雄牛","cow":"雌牛","calf":"幼牛","yak":"牦牛","sheep":"绵羊",
# #
# #         "ram":"雄绵羊","ewe":" 雌绵羊","lamb":"年幼的绵羊","flock":"绵羊的统称","mutton":"羊肉",
# #
# #         "goat":"山羊","billy":"雄山羊","nanny":"雌山羊","pig":"猪","boar":"雄猪"}
# #
# # import random
# # all = []
# # i = 0
# # while True:
# #     word = random.sample(room.keys(),1)[0]
# #     if word in all:
# #         continue
# #     else:
# #         all.append(word)
# #         print(len(all),word)
# #         mean = input('Please input the mean:')
# #         if mean == room[word]:
# #             i = i + 1
# #             print('right')
# #         else:
# #             print('error')
# #     if len(all) == 10:
# #         print('Your accuracy in the ten word:',i*10,'%')
# #         break
#
#
# # import numpy as np
# # import matplotlib.pyplot as plt
# # plt.figure(figsize=(8,4))
# # col = ['red','orange','yellow','green','blue','purple']
# # li = []
# # n = int(input('你想输入几组数据：'))
# # print('将每组A,ω,φ依次输入：')
# # for i in range(3 * n):
# #     li.append(input())
# # for i in range(n):
# #     a = float(li[3 * i])
# #     w = float(li[3 * i + 1])
# #     fi = float(li[3 * i + 2])
# #     x = np.linspace(0, 10, 1000)
# #     y = np.sin(w*x+fi)*a
# #     plt.plot(x,y,color=col[i%6],label=(a,w,fi),linewidth=2)
# # plt.xlabel("X")
# # plt.ylabel("Y")
# # plt.title("y=Asin(ωx+φ)")
# # plt.legend()
# # plt.show()
#
# #
# # num=int(input('输几组数啊？'))
# # a=[]
# # fi=[]
# # w=[]
# # for i in range(num):
# #     print('第',i+1,'个a是')
# #     a.insert(1, int(input()))
# #     print('第', i + 1, '个fi是')
# #     fi.insert(1, int(input()))
# #     print('第', i + 1, '个w是')
# #     w.insert(1, int(input()))
# # import numpy as np
# # import matplotlib.pyplot as plt
# # xita = np.linspace(-1, 1, 2000)
# # coloall=['red','blue','yellow','orange','green','purple','black']
# # for i in range(num):
# #     y = a[i]*np.sin(xita*w[i]+fi[i])
# #     # plt.ylim(-a[i],a[i])
# #     # print(coloall[i])
# #     plt.plot(xita, y, label="$sin(xita)$", color=coloall[i%7], linewidth=2)
# # plt.xlabel("Theda")
# # plt.ylabel("y")
# # plt.title("PyPlot First Example")
# # plt.show()
# # plt.figure(8)
# #
# #
# # import matplotlib.pyplot as plt
# # import numpy as np
# # def func(a, w, fi):  # 定义一个函数
# #     x = np.linspace(1, 10, 1000)
# #     y = np.sin(w * x + fi) * a
# #     plt.plot(x, y, color=L1[i], label=(a, w, fi))
# # L1 = ["red","green","yellow","black","orange","blue","purple"]
# # plt.figure(figsize = (8,4))
# # L2 = []         #L2列表用来存一组一组的a,w,fi
# # while True:
# #     n = int(input("How many lines do you plot:"))
# #     if n > 7:
# #         continue
# #     for i in range(n):
# #         a = float(input("Please input a:"))
# #         w = float(input("Please input w:"))
# #         fi = float(input("Please input fi:"))
# #         L2.append((a,w,fi))     #让学生输入多组数据，然后存到L2
# #     for i in range(n):
# #         a, w, fi = L2[i]
# #         func(a,w,fi)
# #     plt.xlabel("x")
# #     plt.ylabel("a*sin(w*x+fi)")
# #     plt.legend()
# #     plt.show()
# #     break
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# n=int(input('please input the number of your charts(n<= 7):'))
# print('input a,w,fi according to priority: ')
# #tmp=input()
# # x=np.linspace(0, 10, 1000)
# # y=np.sin(w*x+fi)*a
# plt.figure(figsize=(8,4))
# color=['red','green','yellow','orange','blue','purple','black']
# case=[]
#
# for i in range(3*n):
#     case.append(input())
# for i in range(n):
#     a=float(case[i*3])
#     w=float(case[i*3+1])
#     fi=float(case[i*3+2])
#     x=np.linspace(0,10,1000)
#     y=np.sin(w*x+fi)*a
#     plt.plot(x,y,color=color[i%7],label=(a,w,fi),linewidth=2)
#
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title('sin(w*x+fi)*a')
# plt.legend(loc=1)               #固定标签位置
# plt.show()

#
#
import numpy as np
import matplotlib.pylab as plt

def plti(im,**kwargs):
    plt.imshow(im,interpolation="none",**kwargs)
    plt.axis('off')
    plt.show()

im = plt.imread("d:\\lena512color.tiff")
print(im.shape)
plti(im)


im = im[400:3800,:2000,:]
plti(im)
