import numpy as np
import math
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.feature import canny
from skimage.measure import label
from skimage.morphology import closing, square
from skimage.morphology import closing
from skimage.morphology.misc import remove_small_holes
from skimage.morphology.misc import remove_small_objects
import warnings
from shapely.geometry import LineString
warnings.filterwarnings("ignore")
import random


def isBetween(a, b, c):
    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])

    if abs(crossproduct) !=0:
        return False

    dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1])*(b[1] - a[1])
    if dotproduct < 0:
        return False

    squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dotproduct > squaredlengthba:
        return False

    return True
 

def preparation(image, k):
    grayscale = rgb2gray(image)
    bw = grayscale;

    bw[bw < k] = 0;
    bw[bw > k] = 1;

    edges = canny(bw)
    closed = (closing(bw, square(3)))

    labeled = label(closed)
    rem_so = remove_small_objects(labeled, min_size = 64, connectivity=8)
    rem_sh = remove_small_holes(rem_so, area_threshold = 512)
    temp = remove_small_objects(rem_sh, min_size = 2048)


    return temp


def get_top_curve(scale):

    for i in range (len(scale[0])):
        idx = list_rindex([scale[j][i] for j in range(len(scale))])
        if(idx != None):
            scale[idx][i] = 99

    for i in range(len(scale)):
        for j in range(len(scale[i])):
            if scale[i][j]!=99:
                scale[i][j] = 0

    return scale

def list_rindex(li):
    for i in reversed(range(len(li))):
        if li[i] != 0:
            return i

def list_index(li):
    for i in range(len(li)):
        if li[i] != 0:
            return i

def get_bottom_curve(scale):
    
    for i in range(len(scale)):
        idx = list_rindex(scale[i])
        if(idx != None):
            scale[i][idx] = 99

    for i in range (len(scale)):
        idx = list_index(scale[i])
        if(idx != None):
            scale[i][idx] = 99

    for i in range (len(scale[0])):
        idx = list_rindex([scale[j][i] for j in range(len(scale))])
        if(idx != None):
            scale[idx][i] = 99
    
    for i in range (len(scale[0])):
        idx = list_index([scale[j][i] for j in range(len(scale))])
        if(idx != None):
            scale[idx][i] = 99

    for i in range(len(scale)):
        for j in range(len(scale[i])):
            if scale[i][j]!=99:
                scale[i][j] = 0
    return scale


def get_curve_points(scale):
    x_points = []
    y_points = []
    
    for i in range(len(scale[0])):
        for j in range(len(scale)):
            if scale[j][i] != 0:
                x_points.append(i)
                y_points.append(j)
    return x_points, y_points


def intersect_points(x_points, y_points, approximated_curve):
    first_line = LineString(np.column_stack((x_points, y_points)))
    second_line = LineString(np.column_stack((x_points, approximated_curve)))
    intersection = first_line.intersection(second_line)
    x, y = LineString(intersection)[0].xy

    array = []
    for i in range(len(x)):
        array.append([x[i], y[i]])

    array.sort(key=lambda x: x[0])
    ret_x = []
    ret_y = []
    for i in range(len(array)):
        ret_x.append(array[i][0])
        ret_y.append(array[i][1])

    return ret_x, ret_y

def get_val(i):
    return i[1]


def magic_points(x,y):

    center = min(enumerate(y), key=get_val)
    center_x = x[center[0]]
    center_y = y[center[0]]

    return center_x, center_y

def cercle_circonscrit(T):
    (x1, y1), (x2, y2), (x3, y3) = T
    A = np.array([[x3-x1,y3-y1],[x3-x2,y3-y2]])
    Y = np.array([(x3**2 + y3**2 - x1**2 - y1**2),(x3**2+y3**2 - x2**2-y2**2)])
    if np.linalg.det(A) == 0:
        return False
    Ainv = np.linalg.inv(A)
    X = 0.5*np.dot(Ainv,Y)
    x,y = X[0],X[1]
    return int(x), int(y)

def dot(vA, vB):
    return vA[0]*vB[0]+vA[1]*vB[1]

def ang(lineA, lineB):
    vA = [(lineA[0][0]-lineA[1][0]), (lineA[0][1]-lineA[1][1])]
    vB = [(lineB[0][0]-lineB[1][0]), (lineB[0][1]-lineB[1][1])]
    dot_prod = dot(vA, vB)
    magA = dot(vA, vA)**0.5
    magB = dot(vB, vB)**0.5
    
    
    angle = math.acos(dot_prod/magB/magA)
    ang_deg = math.degrees(angle)%360
    
    if ang_deg-180>=0:
        return 360 - ang_deg
    else: 
        return ang_deg


def main_func(image, kf, num):

    temp = preparation(image, kf)

    scale1, scale2 = label(temp), label(temp)

    scale1[scale1 == 2] = 0
    scale2[scale2 == 1] = 0


    scale1 = get_top_curve(scale1)
    scale2 = get_bottom_curve(scale2)

    x_points, y_points = get_curve_points(scale1)
    a_points, b_points = get_curve_points(scale2)

    center_a, center_b = magic_points(a_points, b_points)

    sup_list = []
    for i in range(center_b+1, center_b+int(center_b/1.5)):
        if i%10==0:
            sup_list.append([center_a, i])

    side_points = []
    center_point = []
    for i in range (int(len(x_points)/4), len(x_points) - int(len(x_points)/4) ):
        for j in range(len(a_points)):
            for k in range(len(sup_list)):
                A = [sup_list[k][0], sup_list[k][1]]
                B = [x_points[i], y_points[i]]
                C = [a_points[j], b_points[j]]
                if isBetween(A,B,C) == True: 
                    if (ang([[0,0],[1,0]], [[C[0],C[1]],[B[0], B[1]]]) < 60 or ang([[0,0],[1,0]], [[C[0],C[1]],[B[0], B[1]]]) > 120):
                        side_points.append([[C[0],B[0]],[C[1],B[1]]])

                    elif  ang([[0,0],[0,1]], [[C[0],C[1]],[B[0], B[1]]]) < 20 or ang([[0,0],[0,1]], [[C[0],C[1]],[B[0], B[1]]]) > 150:
                        center_point.append([[C[0],B[0]],[C[1],B[1]]])


    max_dist = 0
    max_dist_point=[[0,0],[0,0]]        
    for i in center_point:
        dist = math.hypot(i[0][1] - i[0][0], i[1][1] - i[1][0])
        if dist > max_dist:
            max_dist = dist
            max_dist_point = i

    min_dist = 999
    min_dist_point=[[0,0],[0,0]]        
    for i in side_points:
        dist = math.hypot(i[0][1] - i[0][0], i[1][1] - i[1][0])
        if dist < min_dist and i[0][1] > len(scale1)/2:
            min_dist = dist
            min_dist_point = i

    min_dist = 999
    min_dist_point2=[[0,0],[0,0]]        
    for i in side_points:
        dist = math.hypot(i[0][1] - i[0][0], i[1][1] - i[1][0])
        if dist < min_dist and i[0][1] < len(scale1)/2:
            min_dist = dist
            min_dist_point2 = i

    figure = plt.figure(num)
    fig = figure.subplots()
    fig.scatter(x_points, y_points, s = 0.2, color = 'y')
    fig.scatter(a_points, b_points, s = 0.2, color='y')
    fig.imshow(image)

    fig.plot(min_dist_point[0], min_dist_point[1], marker ='o', color='red')
    fig.plot(max_dist_point[0], max_dist_point[1], marker ='o', color='red')
    fig.plot(min_dist_point2[0], min_dist_point2[1], marker ='o', color='red')

    dist1 = round(math.hypot(min_dist_point[0][1] - min_dist_point[0][0], min_dist_point[1][1] - min_dist_point[1][0])*0.2636*18000/(len(temp)*len(temp[0])),2)
    dist2 = round(math.hypot(max_dist_point[0][1] - max_dist_point[0][0], max_dist_point[1][1] - max_dist_point[1][0])*0.2636*18000/(len(temp)*len(temp[0])),2)
    dist3 = round(math.hypot(min_dist_point2[0][1] - min_dist_point2[0][0], min_dist_point2[1][1] - min_dist_point2[1][0])*0.2636*18000/(len(temp)*len(temp[0])),2)
    fig.set(title=f'Ширина в переднем отделе: {dist3} мм\nШирина в верхнем отделе: {dist2} мм\nШирина в заднем отделе: {dist1} мм')
    figure.set_figwidth(5)
    figure.set_figheight(6)



# 1 пиксель = 0.2636 мм

#for i in range(1,6):
#    for j in (range(10)):
#        image = plt.imread(f'{i}.jpg')
#        try:
#            main_func(image, j*0.1, i*j+i)
#        except Exception:
#            continue



image = plt.imread('1.jpg')
main_func(image,0.4,1)
image = plt.imread('2.jpg')
main_func(image,0.3,2)
image = plt.imread('3.jpg')
main_func(image,0.51,3)
image = plt.imread('4.jpg')
main_func(image,0.52,4)
image = plt.imread('5.jpg')
main_func(image, 0.5, 5)

plt.show()