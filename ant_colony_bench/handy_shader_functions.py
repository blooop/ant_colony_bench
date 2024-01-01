#from https://github.com/theAfish/Homework-2-Ant-Colony

import taichi as ti
import math


@ti.func
def randUnit2D():
    a = ti.random() * math.tau
    return ti.Vector([ti.cos(a), ti.sin(a)])


@ti.func
def rand():
    return ti.random()


pi = math.pi