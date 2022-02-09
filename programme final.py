#programme final forme algébrique vers forme trigonométrique 09/02/2022#
#par St-Fabio#
from http import server
import math, os, time

def varx():
    print("x est-il une racine ?")
    xrac = str(input())
    os.system("cls")
    if xrac == "oui":
        x = math.sqrt(float(input("x = ")))
        os.system("cls")
        return(x)
    if xrac == "non":
        x = float(input("x = "))
        os.system("cls")
        return(x)
        
def vary():
    print("y est-il une racine ?")
    yrac = str(input())
    os.system("cls")
    if yrac == "oui":
        y = math.sqrt(float(input("y = ")))
        os.system("cls")
        return(y)
    if yrac == "non":
        y = float(input("y = "))
        os.system("cls")
        return(y)    

def module(x, y):
    carx = x ** 2
    cary = y ** 2
    car = carx + cary
    mod = math.sqrt(car)
    return(mod, car)

def cost(x, mod):
    costeta = x / mod
    return(costeta)
    
def sint(x, mod):
    sinteta = y / mod
    return(sinteta)

def trigo(cosinus, sinus):
    if cosinus == 1 and sinus == 0:
        arg = 0
        return(arg)
    if cosinus == 0.8660254037844387 and sinus == 0.5000000000000001:
        arg = "π/6"
        return(arg)
    if cosinus == 0.7071067811865475 and sinus == 0.7071067811865475:
        arg = "π/4"
        return(arg)
    if cosinus == 0.5000000000000001 and sinus == 0.8660254037844387:
        arg = "π/3"
        return(arg)
    if cosinus == 0 and sinus == 1:
        arg = "π/2"
        return(arg)
    if cosinus == -0.5000000000000001 and sinus == 0.8660254037844387:
        arg = "2π/3"
        return(arg)
    if cosinus == -0.7071067811865475 and sinus == 0.7071067811865475:
        arg = "3π/4"
        return(arg)
    if cosinus == -0.8660254037844387 and sinus == 0.5000000000000001:
        arg = "5π/6"
        return(arg)
    if cosinus == -1 and sinus == 0:
        arg = "π"
        return(arg)
    if cosinus == -0.8660254037844387 and sinus == -0.5000000000000001:
        arg = "-5π/6"
        return(arg)
    if cosinus == -0.7071067811865475 and sinus == -0.7071067811865475:
        arg = "-3π/4"
        return(arg)
    if cosinus == -0.5000000000000001 and sinus == -0.8660254037844387:
        arg = "-2π/3"
        return(arg)
    if cosinus == 0 and sinus == -1:
        arg = "-π/2"
        return(arg)
    if cosinus == 0.5000000000000001 and sinus == -0.8660254037844387:
        arg = "-π/3"
        return(arg)
    if cosinus == 0.7071067811865475 and sinus == -0.7071067811865475:
        arg = "-π/4"
        return(arg)
    if cosinus == 0.8660254037844387 and sinus == -0.5000000000000001:
        arg = "-π/6"
        return(arg)
    time.sleep(3)

x = varx()
y = vary()

mod, car = module(x, y)

cosinus = cost(x, mod)
sinus = sint(y, mod)

arg = trigo(cosinus, sinus)

print("argument =", arg)
print("ce qui donne :")
print("z = r [ cos(", arg, ") + sin(", arg, ")i]")
print("avec r = racine de", car)
time.sleep(10)
    