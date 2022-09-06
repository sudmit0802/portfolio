import numpy as np
import matplotlib.pyplot as plt
import math
import random

#--------------------------------------------------Инициализация------------------------------------------------------#
NOM = 16384
DIVNOM = 128
a = 3
t = 4
abc = 0.267


lin = []
list1 = []
list2 = []
right_xu = []
right_xk = []
right_yu = []
right_yk = []
bern1 = []
bern2 = []
mu1 = []
mu2 = []


for i in range(DIVNOM):
    lin.append(0)
    mu1.append(0)
    mu2.append(0)
    lin[i] = abc

for i in range(NOM):
    list1.append(0)
    list2.append(0)
    bern1.append(0)
    bern2.append(0)
#--------------------------------------------------Инициализация------------------------------------------------------#




#--------------------------------------------------Получение выборок Задание(1-2)------------------------------------------------------#
for i in range(NOM):
    if(i < 1):
        list1[i] = (abc * (10*t + a))%1
        list2[i] = (abc * 11 + math.pi)%1
    else:
        list1[i] = (list1[i-1] * (10*t + a))%1
        list2[i] = (list2[i-1] * 11 + math.pi)%1
#--------------------------------------------------Получение выборок Задание(1-2)------------------------------------------------------#
        



#--------------------------------------------------Форматирование (округление)--------------------------------------------------#
for i in range(NOM):
    list1[i] = round(list1[i],3)
    list2[i] = round(list2[i],3)
#--------------------------------------------------Форматирование (округление)--------------------------------------------------#




#--------------------------------------------------Испытания Бернулли--------------------------------------------------#
for i in range(NOM):
    if(list1[i]<abc):
        bern1[i] = 1
    else:
        bern1[i] = 0
    if(list2[i]<abc):
        bern2[i] = 1
    else:
        bern2[i] = 0

for i in range(DIVNOM):
    for j in range((i+1)*DIVNOM):
        mu1[i] += bern1[j]
        mu2[i] += bern2[j] 


for i in range(DIVNOM):
    mu1[i] /= (DIVNOM * (i+1))
    mu2[i] /= (DIVNOM * (i+1))
#--------------------------------------------------Испытания Бернулли--------------------------------------------------#


#--------------------------------------------------Получение вариационных рядов из выборок-------------------------------------------#
list1.sort()
list2.sort()
#--------------------------------------------------Получение вариационных рядов из выборок-------------------------------------------#


#--------------------------------------------------------------------Формирование результатов--------------------------------------------------------------------#
y = np.linspace(0, NOM, DIVNOM)
fig, ax = plt.subplots()
ax.minorticks_on()
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.1)
plt.grid(True, color = 'grey', linewidth= 0.8)
ax.grid(which ='minor', color = 'k', linestyle = ':', linewidth= 0.4)
ax.plot(y, lin, color = "teal", linestyle = '--',  linewidth = 2)
plt.plot(y, mu1, '-',  color = "indigo",  linewidth = 2.5, label = "Функция(1) mu/m(m)")
plt.plot(y, mu2, '-',  color = "crimson",  linewidth = 2.5, label = "Функция(2) mu/m(m)")
ax.legend()                  
plt.show()                  
fig.savefig('Задание2.png')


y = np.linspace(0, NOM, DIVNOM)
fig, ax = plt.subplots()
ax.minorticks_on()
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.1)
plt.grid(True, color = 'grey', linewidth= 0.8)
ax.grid(which ='minor', color = 'k', linestyle = ':', linewidth= 0.4)
ax.plot(y, lin, color = "teal", linestyle = '--',  linewidth = 2)
z1 = np.polyfit(y, mu1, 2)
z2 = np.polyfit(y, mu2, 4)
p1 = np.poly1d(z1)
p2 = np.poly1d(z2)
xp1 = np.linspace(0, NOM)
xp2 = np.linspace(0, NOM)
plt.plot(xp1, p1(xp1), '-',  color = "indigo",  linewidth = 2.5, label = "Функция(1) mu/m(m)")
plt.plot(xp2, p2(xp2), '-',  color = "crimson",  linewidth = 2.5, label = "Функция(2) mu/m(m)")
ax.legend()                  
plt.show()                  
fig.savefig('Задание2.1.png')

y = np.linspace(0, NOM, DIVNOM)
fig, ax = plt.subplots()
ax.minorticks_on()
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.1)
plt.grid(True, color = 'grey', linewidth= 0.8)
ax.grid(which ='minor', color = 'k', linestyle = ':', linewidth= 0.4)
ax.plot(y, lin, color = "teal", linestyle = '--',  linewidth = 2)
z1 = np.polyfit(y, mu1, 6)
z2 = np.polyfit(y, mu2, 8)
p1 = np.poly1d(z1)
p2 = np.poly1d(z2)
xp1 = np.linspace(0, NOM)
xp2 = np.linspace(0, NOM)
plt.plot(xp1, p1(xp1), '-',  color = "indigo",  linewidth = 2.5, label = "Функция(1) mu/m(m)")
plt.plot(xp2, p2(xp2), '-',  color = "crimson",  linewidth = 2.5, label = "Функция(2) mu/m(m)")
ax.legend()                  
plt.show()                  
fig.savefig('Задание2.2.png')

y = np.linspace(0, NOM, DIVNOM)
fig, ax = plt.subplots()
ax.minorticks_on()
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.1)
plt.grid(True, color = 'grey', linewidth= 0.8)
ax.grid(which ='minor', color = 'k', linestyle = ':', linewidth= 0.4)
ax.plot(y, lin, color = "teal", linestyle = '--',  linewidth = 2)
z1 = np.polyfit(y, mu1, 4)
z2 = np.polyfit(y, mu2, 6)
p1 = np.poly1d(z1)
p2 = np.poly1d(z2)
xp1 = np.linspace(0, NOM)
xp2 = np.linspace(0, NOM)
plt.plot(xp1, p1(xp1), '-',  color = "indigo",  linewidth = 2.5, label = "Функция(1) mu/m(m)")
plt.plot(xp2, p2(xp2), '-',  color = "crimson",  linewidth = 2.5, label = "Функция(2) mu/m(m)")
ax.legend()                  
plt.show()                  
fig.savefig('Задание2.3.png')

y = np.linspace(0, NOM, DIVNOM)
fig, ax = plt.subplots()
ax.minorticks_on()
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.1)
plt.grid(True, color = 'grey', linewidth= 0.8)
ax.grid(which ='minor', color = 'k', linestyle = ':', linewidth= 0.4)
ax.plot(y, lin, color = "teal", linestyle = '--',  linewidth = 2)
z1 = np.polyfit(y, mu1, 6)
z2 = np.polyfit(y, mu2, 8)
p1 = np.poly1d(z1)
p2 = np.poly1d(z2)
xp1 = np.linspace(0, NOM)
xp2 = np.linspace(0, NOM)
plt.plot(xp1, p1(xp1), '-',  color = "indigo",  linewidth = 2.5, label = "Функция(1) mu/m(m)")
plt.plot(xp2, p2(xp2), '-',  color = "crimson",  linewidth = 2.5, label = "Функция(2) mu/m(m)")
ax.legend()                  
plt.show()                  
fig.savefig('Задание2.4.png')

y = np.linspace(0, NOM, DIVNOM)
fig, ax = plt.subplots()
ax.minorticks_on()
ax.patch.set_facecolor('blue')
ax.patch.set_alpha(0.1)
plt.grid(True, color = 'grey', linewidth= 0.8)
ax.grid(which ='minor', color = 'k', linestyle = ':', linewidth= 0.4)
ax.plot(y, lin, color = "teal", linestyle = '--',  linewidth = 2)
z1 = np.polyfit(y, mu1, 8)
z2 = np.polyfit(y, mu2, 10)
p1 = np.poly1d(z1)
p2 = np.poly1d(z2)
xp1 = np.linspace(0, NOM)
xp2 = np.linspace(0, NOM)
plt.plot(xp1, p1(xp1), '-',  color = "indigo",  linewidth = 2.5, label = "Функция(1) mu/m(m)")
plt.plot(xp2, p2(xp2), '-',  color = "crimson",  linewidth = 2.5, label = "Функция(2) mu/m(m)")
ax.legend()                  
plt.show()                  
fig.savefig('Задание2.5.png')
#--------------------------------------------------------------------Формирование результатов--------------------------------------------------------------------#
