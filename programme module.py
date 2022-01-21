#programme module 20/01/2022-21/01/2022#

#importation des librairie#
import math, time, os

os.system("cls")

#definition des variables#
print("partie réelle")
x = int(input())
time.sleep(0.2)
os.system("cls")    #efface la console
print("partie imaginaire")
y = int(input())
time.sleep(0.2)
os.system("cls")    #efface la console

#calcul du module#
carx = x ** 2
cary = y ** 2
car = carx + cary
mdl = math.sqrt(car)

#réponse#
print("z =", x, "+", y, "i")
print("ce qui fait racine de", car)
print("ce qui est égale à", mdl)
time.sleep(5)