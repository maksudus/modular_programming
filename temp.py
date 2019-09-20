import numpy as np

def draw_triangle(N): # arguments
    m  = int(N / 2) + 1
    for i in range(m):
        line = ""
        for j in range(i+1):
            line += "*"
        print(line)

    m = int(N / 2)

    for i in range(m):
        line = ""
        for j in range(m-i):
            line = line + "*"
        print(line)
draw_triangle(11)
draw_triangle(13)













