
import mymath.operations.trigonometric as trig
import mymath.operations.arithmetic as arif
from mymath.operations.arithmetic import *
from mymath.operations.trigonometric import *
from mymath import other
import mymath as m
m.operations.arithmetic.add()
def povtor1():
    print('если хотите вычислить синус введите 1')
    print('если хотите вычислить косинус введите 2')
    print('если хотите вычислить сумму двух чисел 3')
    print('если хотите вычислить разность двух чисел 4')
    print('если хотите округлить число введите 5 ')
    print('если хотите вычислить минимальное число введите 6 ')
    print('если хотите вычислить максимальное число введите 7 ')
    print('если хотите выйти из программы 8 ')
    comand = int(input())
    if comand == 1:
        sinus()
    if comand == 2:
        cosinus()
    if comand == 3:
        add()
    if comand == 4:
        subtract()
    if comand == 5:
        other.okr()
    if comand == 6:
        other.minimum()
    if comand == 7:
        other.maximum()
    if comand==8:
        return
povtor1()
