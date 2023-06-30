
import math
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

show_animation=True

def list2point(list1, list2):
    new_list = []
    #[[1,1],[2,2]]
    for x, y in zip(list1, list2):
        new_list.append([x, y])

    #new_list = list(zip(list1, list2)) ##[(1, 1), (2, 2)]点

    return new_list
def ReadObstacle(i, list2, list3, times, dtax, dtay):
    filename = str(i) + "." + "txt"
    # 打开文件
    with open(filename, 'r') as f:
        # 定义两个空列表存储提取的数据
        # 循环遍历每一行数据
        for line in f.readlines():
            # 去除每行末尾的空格和换行符
            line = line.strip()
            # 使用空格分隔每行数据
            data = line.split(' ')
            # 将第2个和第3个数据分别存储到对应的列表中
            list2.append(float(data[1]) * times - dtax)
            list3.append(float(data[2]) * times + dtay)
 # 计算点的中心
def center(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        a = x2 - x1
        b = y2 - y1
        c = x3 - x1
        d = y3 - y1
        e = a * (x1 + x2) + b * (y1 + y2)
        f = c * (x1 + x3) + d * (y1 + y3)
        g = 2 * (a * (y3 - y2) - b * (x3 - x2))
        if g == 0:
            return None
        else:
            x = (d * e - b * f) / g
            y = (a * f - c * e) / g
            return x, y

    # 计算圆心和半径
def circle_center(points):
        n = len(points)
        if n < 3:
            return None
        else:
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        cc = center(points[i], points[j], points[k])
                        if cc is not None:
                            r = math.sqrt((cc[0] - points[i][0]) ** 2 + (cc[1] - points[i][1]) ** 2)
                            ok = True
                            for p in points:
                                if math.sqrt((p[0] - cc[0]) ** 2 + (p[1] - cc[1]) ** 2) > r:
                                    ok = False
                                    break
                            if ok:
                                return cc, r
            return None

def center(points):
    x = sum([p[0] for p in points]) / len(points)
    y = sum([p[1] for p in points]) / len(points)
    return (x, y)

def ClcCircle(points,fig,ax,r):
    #points = [(1, 1), (2, 3), (4, 2), (5, 4), (3, 5)]

    # 计算外接圆并绘图
    #result = circle_center(points)
    result=1
    if result is not None:
       # cc, r = result
        #r=3.6
        cc=center(points)


        ax.set_aspect('equal')
        ax.add_artist(plt.Polygon(points, fill=False, color='gray'))
        ax.add_artist(plt.Circle(cc, r, fill=False, color='blue'))

       # plt.show()
    else:
        print("非法输入，无法计算外接圆")
    matplotlib.use('TKAgg')
    print(cc,r)
    return cc, r

def drawCircle(fig,ax):
    oox = []
    ooy = []
    # 1-4障碍物
    for i in range(1):
        ReadObstacle(i, oox, ooy, 1, 0, 0)
    # # 7障碍物
    # ReadObstacle(7, ox, oy, 1.2, -20, 0)
        print(oox)
        print(ooy)
        oxx = [round(oxx, 2) for oxx in oox]
        oyy = [round(oyy, 2) for oyy in ooy]
        points=list2point(oxx,oyy)
        print(points)
        #lst = [(x[0], x[1]) for x in points]
        #print(lst)
        ClcCircle(points,fig,ax,1.6)
def circle(x1, y1, x2, y2, x3, y3):
# 将输入的字符串转换为浮点数类型
 x1, y1, x2, y2, x3, y3 = 0,1,2,3,6,8

# 计算圆心坐标和半径
# 求出两条中垂线的交点(x0,y0)
 k1 = (y2 - y1) / (x2 - x1)
 k2 = (y3 - y2) / (x3 - x2)
 x0 = (k1 * k2 * (y3 - y1) + k1 * (x2 + x3) - k2 * (x1 + x2)) / (2 * (k1 - k2))
 y0 = -1 * (x0 - (x1 + x2) / 2) / k1 + (y1 + y2) / 2
 r = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

# 输出圆心坐标和半径
 print("圆心坐标为：({:.2f},{:.2f})".format(x0, y0))
 print("半径为：{:.2f}".format(r))

# 画出圆
 theta = [i * (2 * math.pi) / 1000 for i in range(1001)]
 x = [r * math.cos(t) + x0 for t in theta]
 y = [r * math.sin(t) + y0 for t in theta]

 plt.plot(x, y)
 plt.axis('equal')
#plt.show()


print(" start!!")
#fig = plt.figure(1)
fig, ax = plt.subplots()
ax.set_xlim(-50, 100)
ax.set_ylim(-50, 100)
ax.set_xlabel('X')
ax.set_ylabel('Y')
# camara = Camera(fig)  # 保存动图时使用
camara = None
# start and goal position
sx = -5.0  # [m]
sy = 10.0  # [m]
gx = 25.0  # [m]
gy = 5.0  # [m]
robot_size = 1.3  # [m]
ox = []
oy = []

# 6 外圈障碍物
ReadObstacle(6, ox, oy, 1.7, 8, 5)
p1 = np.array([7.59297399782e-05, 5.93557160755e-07])
p2 = np.array([-2.49960255623, -1.03229379654])
points = np.linspace(p1, p2, num=20, endpoint=True)
# 遍历每个点并将其x、y坐标加入列表中
for point in points:
        ox.append(point[0] * 1.7 - 8)
        oy.append(point[1] * 1.7 + 5)
#1-4障碍物
for i in range(6):
    ReadObstacle(i, ox, oy, 1, 0, 0)
# # 7障碍物
# ReadObstacle(7, ox, oy, 1.2, -20, 0)
if show_animation:
    plt.plot(ox, oy, ".k")
    plt.plot(sx, sy, "^r")
    plt.plot(gx, gy, "^c")

    plt.axis("equal")
    if camara != None:
        camara.snap()
#drawCircle(fig,ax)
#circle(2.79,-4.08,4.57,-5.06,4.66,-2.56)


plt.grid(None)
plt.show()
# 已知围成图形的点列表

#ClcCircle(points)










