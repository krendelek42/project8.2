from turtle import *
import random
bgcolor('black')
speed(1000)

def pent(order, size):
    '''This function which draws the fractal of pentaplexity recursively.
            order - recursion depth
            size - line length'''
    speed(1000)

    if order == 0:
        forward(size)


    else:
        c = ['#FFA500', '#FFFF00', '#7FFF00', '#00FFFF', '#0000FF', '#800080', '#FF0000']
        color(random.choice(c))
        pent(order - 1, size / 4)
        left(36)
        left(36)
        pent(order - 1, size / 4)
        left(36)
        left(36)
        pent(order - 1, size / 4)
        left(36)
        left(36)
        left(36)
        left(36)
        left(36)
        pent(order - 1, size / 4)
        right(36)
        pent(order - 1, size / 4)
        left(36)
        left(36)
        pent(order - 1, size / 4)

def ring(order, size):
    '''This function which draws the fractal of ring recursively.
                order - recursion depth
                size - line length'''
    speed(1000)

    if order == 0:
        forward(size)


    else:
        c = ['#FFA500', '#FFFF00', '#7FFF00', '#00FFFF', '#0000FF', '#800080', '#FF0000']
        color(random.choice(c))
        ring(order - 1, size / 4)
        ring(order - 1, size / 4)
        left(90)
        ring(order - 1, size / 4)
        left(90)
        ring(order - 1, size / 4)
        left(90)
        ring(order - 1, size / 4)
        left(90)
        ring(order - 1, size / 4)
        left(90)
        ring(order - 1, size / 4)
        right(90)
        ring(order - 1, size / 4)

def moz(order, size):
    '''This function which draws the fractal of square recursively.
                order - recursion depth
                size - line length'''
    speed(1000)

    if order == 0:
        forward(size)


    else:
        c = ['#FFA500', '#FFFF00', '#7FFF00', '#00FFFF', '#0000FF', '#800080', '#FF0000']
        color(random.choice(c))
        moz(order - 1, size / 4)
        moz(order - 1, size / 4)
        left(90)
        moz(order - 1, size / 4)
        left(90)
        moz(order - 1, size / 4)
        left(90)
        moz(order - 1, size / 4)
        left(90)
        moz(order - 1, size / 4)
        moz(order - 1, size / 4)



def main():
    '''This function is basic. The function draws these fractals'''
    print('Меню:', '1. Кольцо с цветком', '2. Мозаика', sep = '\n')
    answer = int(input('Какой рисунок вы предпочитаете нарисовать? '))
    if answer == 1:
        speed(1000)
        up()
        goto(100, -200)
        down()
        n = int(input('Глубина рекурсии:'))
        a = int(input('Длина стороны:'))
        ring(n, a)
        left(90)
        ring(n, a)
        left(90)
        ring(n, a)
        left(90)
        ring(n, a)
        up()
        goto(-120, 100)
        q = int(input('Глубина рекурсии:'))
        w = int(input('Длина стороны:'))
        down()
        pent(q, w)
        left(36)
        left(36)
        pent(q, w)
        left(36)
        left(36)
        pent(q, w)
        left(36)
        left(36)
        pent(q, w)
        left(36)
        left(36)
        pent(q, w)
        mainloop()
    if answer == 2:
        speed(1000)
        up()
        goto(-250, -200)
        down()
        n = int(input('Глубина рекурсии:'))
        a = int(input('Длина стороны:'))
        moz(n, a)
        left(90)
        moz(n, a)
        left(90)
        moz(n, a)
        left(90)
        moz(n, a)
        up()
        goto(-75, 85)
        q = int(input('Глубина рекурсии:'))
        w = int(input('Длина стороны:'))
        down()
        pent(q, w)
        left(36)
        left(36)
        pent(q, w)
        left(36)
        left(36)
        pent(q, w)
        left(36)
        left(36)
        pent(q, w)
        left(36)
        left(36)
        pent(q, w)
        mainloop()


main()