import turtle
import time
import math

turtle.reset()
turtle.speed(8)

pa = []  # 外设，应用全局


def draw_pict_pa(org_x, org_y, w, n):  # 生成一个圆，数组pa[]记录圆上以n平分的点位置
    turtle.setpos(org_x, org_y)
    turtle.lt(180 / n)  # 圆有一定的角度起始
    turtle.fd(w)
    turtle.rt(90)
    for i in range(0, n):
        turtle.circle(-w, 360 / n)
        pa.append(turtle.pos())
    turtle.rt(180 / n)  # 恢复turtle的角度


def draw_pict1(org_x, org_y, w, n):  # 第一个图，w控制图形大小，n控制复杂度（以下同）
    st1 = w * math.sin(math.pi * 1 / n)
    st2 = w * math.cos(math.pi * 1 / n)  # 依据w，调整需要的长度st + number（以下同）
    turtle.pu()
    turtle.setpos(org_x, org_y + 2 * st2)  # 设置作图初始点（以下同）
    turtle.pd()
    for m in range(0, n):  # 设置小单元，开始循环
        turtle.fd(st1)
        turtle.rt(90)
        turtle.fd(st2)
        turtle.lt(180 - 360 / n)
        turtle.fd(st2)
        turtle.rt(90)
        turtle.fd(st1)


def draw_pict2(org_x, org_y, w, n):  # 第二个图
    st1 = w * math.tan(math.pi * 1 / n)
    st2 = st1 * 2
    turtle.pu()
    turtle.setpos(org_x, org_y + w)
    turtle.pd()
    for m in range(0, n):
        turtle.fd(st1)
        turtle.rt(720 / n)  # 每个角度都添加n控制，确定图行的准确性
        turtle.fd(st2)
        turtle.lt(360 / n)
        turtle.fd(st2)
        turtle.rt(720 / n)
        turtle.fd(st1)


def draw_pict3(org_x, org_y, w, n):  # 第三个图
    st1 = 2 * w * math.sin(math.pi * 1 / n)
    turtle.pu()
    turtle.setpos(org_x + w, org_y)
    turtle.rt(90 - 180 / n)
    turtle.pd()
    for m in range(0, n):
        for j in range(0, 2):  # 循环两次，等边的两条边
            turtle.fd(st1)
            turtle.rt(120)
        turtle.fd(st1)  # 第三条边
        turtle.lt(240 - 360 / n)  # 回到内图形
        turtle.fd(st1)
    turtle.lt(90 - 180 / n)  # 恢复turtle的角度


def draw_pict4(org_x, org_y, w, n):  # 第四个图
    turtle.pu()
    draw_pict_pa(org_x, org_y, w, n)  # 调用圆点数组，配合特定w，n
    turtle.pd()
    for j in range(0, n):
        turtle.goto(pa[j])  # 以数组点开始，转向特定角度贴边
        turtle.rt(360 / n)
        for m in range(0, 3):  # 等边三角形
            turtle.fd(w)
            turtle.lt(120)
    turtle.lt(90)  # 恢复turtle的角度
    del pa[:]  # 清空数组pa，方便下次重新填数


def draw_pict5(org_x, org_y, w, n):  # 第五个图
    turtle.pu()
    draw_pict_pa(org_x, org_y, w, n)  # 调用
    turtle.pd()
    for j in range(0, n):  # 以数组点开始，转向特定角度贴边
        turtle.goto(pa[j])
        turtle.rt(360 / n)
        for m in range(0, 2):  # 折返
            turtle.fd(3 * w)
            turtle.lt(180)
    turtle.lt(90)  # 恢复turtle的角度
    del pa[:]


def draw_pict6(org_x, org_y, w, s, n):  # 第六个图，w控制长边，s短边比例，n辅助度
    st1 = w * s  # 短边
    st2 = w + st1 * math.tan(math.pi * 1 / n)  # 起始点抬升距离
    turtle.pu()
    turtle.setpos(org_x, org_y + st2)
    turtle.pd()
    for m in range(0, n * 2):  # 两倍，使n较高图形完整
        turtle.fd(st1)
        turtle.rt(90)
        turtle.fd(w)
        turtle.lt(360 / n)
        turtle.fd(w)
        turtle.rt(90)
        turtle.fd(st1)


turtle.pencolor('yellow')
draw_pict2(0, 120, 95, 16)
draw_pict4(-200, -120, 70, 16)
draw_pict6(200, -120, 110, 0.2, 17)

turtle.pencolor('orange')  # 作业要求
draw_pict1(-200, 120, 40, 10)
draw_pict2(0, 120, 70, 8)
draw_pict3(200, 120, 40, 5)
draw_pict4(-200, -120, 50, 8)
draw_pict5(0, -120, 30, 8)
draw_pict6(200, -120, 80, 0.2, 8)

turtle.ht()
time.sleep(10)
