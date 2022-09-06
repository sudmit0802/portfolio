import numpy as np
import matplotlib.pyplot as plt
import math
import random

#--------------------------------------------------Инициализация------------------------------------------------------#
a = 3
t = 4
abc = 0.267
u = 0.228
k = 1.28
E = 7
d = 2.28
f1 = open('Задание1 Выборка1.txt','w')
f2 = open('Задание1 Выборка2.txt','w')
f_1_1 = open('Задание1 Вариационный ряд1.txt','w')
f_1_2 = open('Задание1 Вариационный ряд2.txt','w')
f3 = open('Задание3 (u) Выборка1.txt','w')
f4 = open('Задание3 (u) Выборка2.txt','w')
f5 = open('Задание3 (k) Выборка1.txt','w')
f6 = open('Задание3 (k) Выборка2.txt','w')
f7 = open('Задание4 Выборка1.txt', 'w')
f8 = open('Задание4 Выборка2.txt', 'w')
f9 = open('Расчёты.txt','w')

E1 = 0
E2 = 0
E3 = 0
E4 = 0
E5 = 0
E6 = 0
E7 = 0
E8 = 0
d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
d6 = 0
d7 = 0
d8 = 0
fixed_d1 = 0
fixed_d2 = 0
fixed_d3 = 0
fixed_d4 = 0
fixed_d5 = 0
fixed_d6 = 0
fixed_d7 = 0
fixed_d8 = 0
med1 = 0
med2 = 0
med3 = 0
med4 = 0
med5 = 0
med6 = 0
med7 = 0
med8 = 0



lin = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
right_list_4 = []
right_list_tmp1 = []
right_list_tmp2 = []
right_xu = []
right_xk = []
right_yu = []
right_yk = []
bern1 = []
bern2 = []
mu1 = []
mu2 = []
gist1 = []
gist2 = []
gist3 = []
gist4 = []
gist5 = []
gist6 = []
gist7 = []
gist8 = []
gist9 = []
gist10 = []
gist11 = []
gist12 = []
gistc1 = []
gistc2 = []
gistc3 = []
gistc4 = []
gist_right_yu1 = []
gist_right_yk2 = []
gist_right_yu3 = []
gist_right_yk4 = []
gist_right_4 = []


del1 = []
del2 = []
del3 = []
del4 = []
del5 = []
del6 = []



for i in range(8):
    gist1.append(0)
    gist2.append(0)
    gist3.append(0)
    gist4.append(0)
    gist5.append(0)
    gist6.append(0)
    gist7.append(0)
    gist8.append(0)
    gist9.append(0)
    gist10.append(0)
    gist11.append(0)
    gist12.append(0)
    gistc1.append(0)
    gistc2.append(0)
    del1.append("0")
    del2.append("0")
    del3.append("0")
    del4.append("0")
    del5.append("0")
    del6.append("0")
    gist_right_yu1.append(0)
    gist_right_yk2.append(0)
    gist_right_yu3.append(0)
    gist_right_yk4.append(0)

for i in range(9):
    gistc3.append(0)
    gistc4.append(0)


for i in range(10):
    lin.append(0)
    mu1.append(0)
    mu2.append(0)
    lin[i] = abc

for i in range(100):
    list1.append(0)
    list2.append(0)
    list3.append(0)
    list4.append(0)
    list5.append(0)
    list6.append(0)
    list7.append(0)
    list8.append(0)
    bern1.append(0)
    bern2.append(0)
    right_xu.append(0)
    right_xk.append(0)
    right_yu.append(0)
    right_yk.append(0)
    
#for i in range(90):
#   gist_right_4.append(0)

for i in range(130):
    right_list_4.append(0)
    right_list_tmp1.append(0)
    right_list_tmp2.append(0)
    list9.append(0)
    list10.append(0)
    list11.append(0)
    gist_right_4.append(0)
#--------------------------------------------------Инициализация------------------------------------------------------#












#--------------------------------------------------Получение выборок Задание(1-2)------------------------------------------------------#
for i in range(100):
    if(i < 1):
        list1[i] = (abc * (10*t + a))%1
        list2[i] = (abc * 11 + math.pi)%1
    else:
        list1[i] = (list1[i-1] * (10*t + a))%1
        list2[i] = (list2[i-1] * 11 + math.pi)%1
#--------------------------------------------------Получение выборок Задание(1-2)------------------------------------------------------#
        











#--------------------------------------------------Получение выборок Задание3------------------------------------------------------#

s1 = 0
s2 = 0
s3 = 0
s4 = 0

for i in range(100):    
    right_xu[i] = (i+1)/4.438
    right_xk[i] = (i+1)/25
    right_yu[i] =  1 - math.e**((-1)*right_xu[i]*u)
    right_yk[i] =  1 - math.e**((-1)*right_xk[i]*k)

    list3[i] = (-1)*math.log(list1[i])/u
    list4[i] = (-1)*math.log(list2[i])/u
    list5[i] = (-1)*math.log(list1[i])/k
    list6[i] = (-1)*math.log(list2[i])/k
    s1+=list3[i]
    s2+=list4[i]
    s3+=list5[i]
    s4+=list6[i]
    
print(s1)
print(s2)
print(s3)
print(s4)

#--------------------------------------------------Получение выборок Задание3------------------------------------------------------#














#--------------------------------------------------Получение выборок Задание4------------------------------------------------------#
for i in range(100):
    list7[i] = E + math.sqrt(d)*math.sin(2*math.pi*list2[i])*math.sqrt((-2)*math.log(list1[i]))
    list8[i] = E + math.sqrt(d)*math.cos(2*math.pi*list2[i])*math.sqrt((-2)*math.log(list1[i]))
    
for i in range(130):
    right_list_tmp1[i] = math.e**((-1)*(((i*0.1 - E)**2)/(d*2))) / (math.sqrt(d*2*math.pi))

for i in range(1,130):
    right_list_tmp2[i] = 0.05*(right_list_tmp1[i-1]+right_list_tmp1[i])


for i in range(1,130):
    right_list_4[i] = (right_list_4[i-1] + right_list_tmp2[i])   

for i in range(31,130):
    list9[i] = math.e**((-1)*(((i*0.1 - E)**2)/(d*2))) / (math.sqrt(d*2*math.pi))
    
for i in range(32,130):
    list10[i] = 0.05*(list9[i-1]+list9[i])

for i in range(32,130):
    list11[i] = (list11[i-1]+list10[i])


for i in range(32):
    list11.pop(0)
for i in range(8):
    list11.pop()

#--------------------------------------------------Получение выборок Задание4------------------------------------------------------#








#--------------------------------------------------Форматирование (округление)--------------------------------------------------#
for i in range(100):
    list1[i] = round(list1[i],3)
    list2[i] = round(list2[i],3)
    list3[i] = round(list3[i],3)
    list4[i] = round(list4[i],3)
    list5[i] = round(list5[i],3)
    list6[i] = round(list6[i],3)
    list7[i] = round(list7[i],3)
    list8[i] = round(list8[i],3)
    right_yu[i] = round(right_yu[i],3)
    right_yk[i] = round(right_yk[i],3)
#--------------------------------------------------Форматирование (округление)--------------------------------------------------#





#--------------------------------------------------Расчёты-------------------------------------------#
for i in range(100):
    E1 += list1[i]
    E2 += list2[i]
    E3 += list3[i]
    E4 += list4[i]
    E5 += list5[i]
    E6 += list6[i]
    E7 += list7[i]
    E8 += list8[i]


E1/=100
E2/=100
E3/=100
E4/=100
E5/=100
E6/=100
E7/=100
E8/=100

for i in range(100):
    d1 += (list1[i] - E1)**2 
    d2 += (list2[i] - E2)**2
    d3 += (list3[i] - E3)**2
    d4 += (list4[i] - E4)**2
    d5 += (list5[i] - E5)**2 
    d6 += (list6[i] - E6)**2
    d7 += (list7[i] - E7)**2
    d8 += (list8[i] - E8)**2

d1 /= 100 
d2 /= 100
d3 /= 100
d4 /= 100
d5 /= 100 
d6 /= 100
d7 /= 100
d8 /= 100

fixed_d1 = d1*(100/99) 
fixed_d2 = d2*(100/99)
fixed_d3 = d3*(100/99)
fixed_d4 = d4*(100/99)
fixed_d5 = d5*(100/99) 
fixed_d6 = d6*(100/99)
fixed_d7 = d7*(100/99)
fixed_d8 = d8*(100/99)

E1 = round(E1,3)
E2 = round(E2,3)
E3 = round(E3,3)
E4 = round(E4,3)
E5 = round(E5,3)
E6 = round(E6,3)
E7 = round(E7,3)
E8 = round(E8,3)

d1 = round(d1,3) 
d2 = round(d2,3)
d3 = round(d3,3)
d4 = round(d4,3)
d5 = round(d5,3) 
d6 = round(d6,3)
d7 = round(d7,3)
d8 = round(d8,3)

fixed_d1 = round(fixed_d1,3) 
fixed_d2 = round(fixed_d2,3)
fixed_d3 = round(fixed_d3,3)
fixed_d4 = round(fixed_d4,3)
fixed_d5 = round(fixed_d5,3) 
fixed_d6 = round(fixed_d6,3)
fixed_d7 = round(fixed_d7,3)
fixed_d8 = round(fixed_d8,3)
#--------------------------------------------------Расчёты-------------------------------------------#










#--------------------------------------------------Печать выборок в файлы--------------------------------------------------#
for i in range(100):
    f1.write(str(list1[i]).replace('.',',') + '\n')
    f2.write(str(list2[i]).replace('.',',') + '\n')
    f3.write(str(list3[i]).replace('.',',') + '\n')
    f4.write(str(list4[i]).replace('.',',') + '\n')
    f5.write(str(list5[i]).replace('.',',') + '\n')
    f6.write(str(list6[i]).replace('.',',') + '\n')
    f7.write(str(list7[i]).replace('.',',') + '\n')
    f8.write(str(list8[i]).replace('.',',') + '\n')
#--------------------------------------------------Печать выборок в файлы--------------------------------------------------#













#--------------------------------------------------Испытания Бернулли Задание2--------------------------------------------------#
for i in range(100):
    if(list1[i]<abc):
        bern1[i] = 1
    else:
        bern1[i] = 0
    if(list2[i]<abc):
        bern2[i] = 1
    else:
        bern2[i] = 0

for i in range(10):
    for j in range((i+1)*10):
        mu1[i] += bern1[j]
        mu2[i] += bern2[j] 


for i in range(10):
    mu1[i] /= (10 * (i+1))
    mu2[i] /= (10 * (i+1))
#--------------------------------------------------Испытания Бернулли Задание2--------------------------------------------------#












#--------------------------------------------------Получение вариационных рядов из выборок-------------------------------------------#
list1.sort()
list2.sort()
list3.sort()
list4.sort()
list5.sort()
list6.sort()
list7.sort()
list8.sort()

med1 = round((list1[49]+list1[50]) / 2, 3)
med2 = round((list2[49]+list2[50]) / 2, 3)
med3 = round((list3[49]+list3[50]) / 2, 3)
med4 = round((list4[49]+list4[50]) / 2, 3)
med5 = round((list5[49]+list5[50]) / 2, 3)
med6 = round((list6[49]+list6[50]) / 2, 3)
med7 = round((list7[49]+list7[50]) / 2, 3)
med8 = round((list8[49]+list8[50]) / 2, 3)


for i in range(100):
    f_1_1.write(str(list1[i]).replace('.',',') + '\n')
    f_1_2.write(str(list2[i]).replace('.',',') + '\n')
f9.write('\t\t' +  'Задание 1')
f9.write('\n' + 'Выб.среднее1: ' + str(E1).replace('.',',') + '\n' + 'Выб.среднее2: ' + str(E2).replace('.',',') + '\n' + 'Выб.дисперсия1: ' + str(d1).replace('.',',') + '\n' + 'Выб.дисперсия2: ' + str(d2).replace('.',',') + '\n' + 'Испр. выб.дисперсия1: ' + str(fixed_d1).replace('.',',') + '\n' + 'Испр. выб.дисперсия2: ' + str(fixed_d2).replace('.',',') + '\n' + 'Медиана1: ' + str(med1).replace('.',',') + '\n' + 'Медиана2: ' + str(med2).replace('.',',') + '\n')
f9.write('\n\t\t' +  'Задание 3')
f9.write('\n' + 'Выб.среднее1(u): ' + str(E3).replace('.',',') + '\n' + 'Выб.среднее2(u): ' + str(E4).replace('.',',') + '\n' + 'Выб.среднее1(k): ' + str(E5).replace('.',',') + '\n' + 'Выб.среднее2(k): ' + str(E6).replace('.',',') + '\n' + 'Выб.дисперсия1(u): ' + str(d3).replace('.',',') + '\n' + 'Выб.дисперсия2(u): ' + str(d4).replace('.',',') + '\n' + 'Выб.дисперсия1(k): ' + str(d5).replace('.',',') + '\n' + 'Выб.дисперсия2(k): ' + str(d6).replace('.',',') + '\n' + 'Испр. выб.дисперсия1(u): ' + str(fixed_d3).replace('.',',') + '\n' + 'Испр. выб.дисперсия2(u): ' + str(fixed_d4).replace('.',',') + '\n' + 'Испр. выб.дисперсия1(k): ' + str(fixed_d5).replace('.',',') + '\n' + 'Испр. выб.дисперсия2(k): ' + str(fixed_d6).replace('.',',') + '\n' + 'Медиана1(u): ' + str(med3).replace('.',',') + '\n' + 'Медиана2(u): ' + str(med4).replace('.',',') + '\n' + 'Медиана1(k): ' + str(med5).replace('.',',') + '\n' + 'Медиана2(k): ' + str(med6).replace('.',',') + '\n')
f9.write('\n\t\t' +  'Задание 4')
f9.write('\n' + 'Выб.среднее1: ' + str(E7).replace('.',',') + '\n' + 'Выб.среднее2: ' + str(E8).replace('.',',') + '\n' + 'Выб.дисперсия1: ' + str(d7).replace('.',',') + '\n' + 'Выб.дисперсия2: ' + str(d8).replace('.',',') + '\n' + 'Испр. выб.дисперсия1: ' + str(fixed_d7).replace('.',',') + '\n' + 'Испр. выб.дисперсия2: ' + str(fixed_d8).replace('.',',') + '\n' + 'Медиана1: ' + str(med7).replace('.',',') + '\n' + 'Медиана2: ' + str(med8).replace('.',',') + '\n')
#--------------------------------------------------Получение вариационных рядов из выборок-------------------------------------------#



#--------------------------------------------------------------------Графики как гистограммы Задание1--------------------------------------------------------------------#
tmpс1 = (list1[99] - list1[0]) / 8
tmpс2 = (list2[99] - list2[0]) / 8


for j in range(8):
    for i in range(100):
        if(list1[i] <= (tmpс1*(j+1))):
            gistc1[j] += 1
        if(list2[i] <= (tmpс2*(j+1))):
            gistc2[j] += 1

for i in range(1,9):
    gistc3[i] = gistc1[i-1]/100
    gistc4[i] = gistc2[i-1]/100
#--------------------------------------------------------------------Графики как гистограммы Задание1--------------------------------------------------------------------#








#--------------------------------------------------------------------Гистограммы Задание3--------------------------------------------------------------------#
tmp1 = list3[99] / 8
tmp2 = list4[99] / 8
tmp3 = list5[99] / 8
tmp4 = list6[99] / 8


for j in range(8):
    for i in range(100):
        if(list3[i] <= tmp1*(j+1)):
            gist1[j] += 1
        if(list4[i] <= tmp2*(j+1)):
            gist2[j] += 1
        if(list5[i] <= tmp3*(j+1)):
            gist3[j] += 1
        if(list6[i] <= tmp4*(j+1)):
            gist4[j] += 1

gist5[0] = gist1[0] 
gist6[0] = gist2[0]
gist7[0] = gist3[0]
gist8[0] = gist4[0]


gist_right_yu3[0] = round((right_yu[14] - right_yu[0])*100, 3)
gist_right_yu3[1] = round((right_yu[27] - right_yu[15])*100, 3)
gist_right_yu3[2] = round((right_yu[39] - right_yu[27])*100, 3)
gist_right_yu3[3] = round((right_yu[51] - right_yu[39])*100, 3)
gist_right_yu3[4] = round((right_yu[63] - right_yu[51])*100, 3)
gist_right_yu3[5] = round((right_yu[75] - right_yu[63])*100, 3)
gist_right_yu3[6] = round((right_yu[87] - right_yu[75])*100, 3)
gist_right_yu3[7] = round((right_yu[99] - right_yu[87])*100, 3)

gist_right_yk4[0] = round((right_yk[14] - right_yk[0])*100, 3)
gist_right_yk4[1] = round((right_yk[27] - right_yk[15])*100, 3)
gist_right_yk4[2] = round((right_yk[39] - right_yk[27])*100, 3)
gist_right_yk4[3] = round((right_yk[51] - right_yk[39])*100, 3)
gist_right_yk4[4] = round((right_yk[63] - right_yk[51])*100, 3)
gist_right_yk4[5] = round((right_yk[75] - right_yk[63])*100, 3)
gist_right_yk4[6] = round((right_yk[87] - right_yk[75])*100, 3)
gist_right_yk4[7] = round((right_yk[99] - right_yk[87])*100, 3)



for i in range(1,8):
    gist5[i] = gist1[i] - gist1[i-1]
    gist6[i] = gist2[i] - gist2[i-1]
    gist7[i] = gist3[i] - gist3[i-1]
    gist8[i] = gist4[i] - gist4[i-1]


for i in range(8):
    del1[i] = '<' + str(round((tmp1*(i+1)),2))
    del2[i] = '<' + str(round((tmp2*(i+1)),2))
    del3[i] = '<' + str(round((tmp3*(i+1)),2))
    del4[i] = '<' + str(round((tmp4*(i+1)),2))
#--------------------------------------------------------------------Гистограммы Задание3--------------------------------------------------------------------#











#--------------------------------------------------------------------Гистограммы Задание4--------------------------------------------------------------------#
tmp5 = (list7[99] - list7[0]) / 7
tmp6 = (list8[99] - list8[0]) / 7


for j in range(8):
    for i in range(100):
        if(list7[i] <= (list7[0]+tmp5*j)):
            gist9[j] += 1
        if(list8[i] <= (list8[0]+tmp6*j)):
            gist10[j] += 1



gist11[0] = gist9[0] 
gist12[0] = gist10[0]

gist_right_4[0] = round((right_list_4[1] - right_list_4[0])*500,3)
for i in range(1, 130):
    gist_right_4[i] = round((right_list_4[i] - right_list_4[i-1])*1000,3)




for i in range(1,8):
    gist11[i] = gist9[i] - gist9[i-1]
    gist12[i] = gist10[i] - gist10[i-1]

for i in range(8):
    del5[i] = '<' + str(round((list7[0]+tmp5*i),2))
    del6[i] = '<' + str(round((list8[0]+tmp6*i),2))
#--------------------------------------------------------------------Гистограммы Задание4--------------------------------------------------------------------#










#--------------------------------------------------------------------Формирование результатов--------------------------------------------------------------------#
y = np.linspace(0, 1, 100)
fig, ax = plt.subplots()
ax.minorticks_on()
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.1)
plt.grid(True, color = 'grey', linewidth= 0.8)
ax.grid(which ='minor', color = 'k', linestyle = ':', linewidth= 0.4) 
ax.plot(list1, y, color = "indigo",  linewidth = 2.5, label = "Эмп. функция распр.(1)")      
ax.plot(list2, y, color = "crimson", linewidth = 2.5, label = "Эмп. функция распр.(2)")
ax.plot(y, y, color = "teal", linestyle = '--', linewidth = 2, label = "Теор. функция распр.")
ax.legend()                                    
plt.show()                            
fig.savefig('Задание1.png')
plt.clf()

y = np.linspace(0, 1, 9)
fig, ax = plt.subplots()
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.1)
plt.grid(True, color = 'grey', linewidth= 0.8)
ax.grid(which ='minor', color = 'k', linestyle = ':', linewidth= 0.4) 
ax.plot(y, gistc3, color = "indigo",  linewidth = 2.5, label = "Эмп. функция распр.(1)")      
ax.plot(y, gistc4, color = "crimson", linewidth = 2.5, label = "Эмп. функция распр.(2)")
ax.plot(y, y, color = "teal", linestyle = '--', linewidth = 2, label = "Теор. функция распр.")
ax.legend()                                    
plt.show()
plt.show()
fig.savefig('Задание1 график как гистограмма.png')
plt.clf()

y = np.linspace(0, 100, 10)
fig, ax = plt.subplots()
ax.minorticks_on()
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.1)
plt.grid(True, color = 'grey', linewidth= 0.8)
ax.grid(which ='minor', color = 'k', linestyle = ':', linewidth= 0.4)
ax.plot(y, lin, color = "teal", linestyle = '--',  linewidth = 2)
z1 = np.polyfit(y, mu1, 8)
z2 = np.polyfit(y, mu2, 6)
p1 = np.poly1d(z1)
p2 = np.poly1d(z2)
xp1 = np.linspace(0, 100)
xp2 = np.linspace(0, 100)
plt.plot(xp1, p1(xp1), '-',  color = "indigo",  linewidth = 2.5, label = "Функция(1) mu/m(m)")
plt.plot(xp2, p2(xp2), '-',  color = "crimson",  linewidth = 2.5, label = "Функция(2) mu/m(m)")
ax.legend()                  
plt.show()                  
fig.savefig('Задание2.png')
plt.clf()


y = np.linspace(0, 1, 100)
fig, ax = plt.subplots()
ax.minorticks_on()
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.1)
plt.grid(True, color = 'grey', linewidth= 0.8)
ax.grid(which ='minor', color = 'k', linestyle = ':', linewidth= 0.4) 
ax.plot(list3, y, color = "indigo",  linewidth = 2.5, label = "Эмп. функция распр.(1)")      
ax.plot(list4, y, color = "crimson", linewidth = 2.5, label = "Эмп. функция распр.(2)")
ax.plot(right_xu, right_yu, color = "teal", linestyle = '--', linewidth = 2, label = "Теор. функция распр.")
ax.legend()                                    
plt.show()                            
fig.savefig('Задание3 (u).png') 
plt.clf()

x = np.linspace(0, 8, 8)
fig, ax = plt.subplots()
plt.ylim([0, 50])
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.2)
ax.bar(del3,gist7)
z1 = np.polyfit(x, gist_right_yk4, 7)
p1 = np.poly1d(z1)
xp1 = np.linspace(0, 7.5)
ax.plot(xp1, p1(xp1), '-',  color = "crimson",  linewidth = 2.5, label = "Теор. функция плотности")
ax.legend() 
fig.savefig('Гистограмма(k1).png')
plt.clf()

x = np.linspace(0, 8, 8)
fig, ax = plt.subplots()
plt.ylim([0, 50])
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.2)
ax.bar(del4,gist5)
z1 = np.polyfit(x, gist_right_yk4, 7)
p1 = np.poly1d(z1)
xp1 = np.linspace(0, 7.5)
ax.plot(xp1, p1(xp1), '-',  color = "crimson",  linewidth = 2.5, label = "Теор. функция плотности")
ax.legend() 
fig.savefig('Гистограмма(k2).png')
plt.clf()

x = np.linspace(0, 8, 8)
fig, ax = plt.subplots()
plt.ylim([0, 50])
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.2)
ax.bar(del1,gist8)
z1 = np.polyfit(x, gist_right_yu3, 7)
p1 = np.poly1d(z1)
xp1 = np.linspace(0, 7.5)
ax.plot(xp1, p1(xp1), '-',  color = "crimson",  linewidth = 2.5, label = "Теор. функция плотности")
ax.legend() 
fig.savefig('Гистограмма(u1).png')
plt.clf()

x = np.linspace(0, 8, 8)
fig, ax = plt.subplots()
plt.ylim([0, 50])
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.2)
ax.bar(del2,gist6)
z1 = np.polyfit(x, gist_right_yu3, 7)
p1 = np.poly1d(z1)
xp1 = np.linspace(0, 7.5)
ax.plot(xp1, p1(xp1), '-',  color = "crimson",  linewidth = 2.5, label = "Теор. функция плотности")
ax.legend() 
fig.savefig('Гистограмма(u2).png')
plt.clf()




y = np.linspace(0, 1, 100)
fig, ax = plt.subplots()
ax.minorticks_on()
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.1)
plt.grid(True, color = 'grey', linewidth= 0.8)
ax.grid(which ='minor', color = 'k', linestyle = ':', linewidth= 0.4) 
ax.plot(list5, y, color = "indigo",  linewidth = 2.5, label = "Эмп. функция распр.(1)")      
ax.plot(list6, y, color = "crimson", linewidth = 2.5, label = "Эмп. функция распр.(2)")
ax.plot(right_xk, right_yk, color = "teal", linestyle = '--', linewidth = 2, label = "Теор. функция распр.")
ax.legend()                                    
plt.show()                            
fig.savefig('Задание3 (k).png')
plt.clf()

y = np.linspace(0, 1, 100)
x = np.linspace(3, 12, 90)
fig, ax = plt.subplots()
ax.minorticks_on()
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.1)
plt.grid(True, color = 'grey', linewidth= 0.8)
ax.grid(which ='minor', color = 'k', linestyle = ':', linewidth= 0.4) 
ax.plot(list7, y, color = "indigo",  linewidth = 2.5, label = "Эмп. функция распр.(1)")      
ax.plot(list8, y, color = "crimson", linewidth = 2.5, label = "Эмп. функция распр.(2)")
ax.plot(x, list11, color = "teal", linestyle = '--', linewidth = 2, label = "Теор. функция распр.")
ax.legend()                                    
plt.show()                            
fig.savefig('Задание4.png')
plt.clf()


x = np.linspace(-1.3, 7.5, 130)
fig, ax = plt.subplots()
plt.xlim([-0.7, 7.5])
plt.ylim([0, 31])
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.2)
ax.bar(del5,gist11)
ax.plot(x, gist_right_4, '-',  color = "crimson",  linewidth = 2.5, label = "Теор. функция плотности")
plt.show()
fig.savefig('Задание4 гистограмма1.png')
plt.clf()

x = np.linspace(-2, 6.8, 130)
fig, ax = plt.subplots()
plt.xlim([-0.7, 7.5])
plt.ylim([0, 31])
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.2)
ax.bar(del6,gist12)
ax.plot(x, gist_right_4, '-',  color = "crimson",  linewidth = 2.5, label = "Теор. функция плотности")
plt.show()
fig.savefig('Задание4 гистограмма2.png')
plt.clf()

#--------------------------------------------------------------------Формирование результатов--------------------------------------------------------------------#
