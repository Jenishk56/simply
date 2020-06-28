import random
def minesweeper(w,h,k):
    matrix = [[0 for x in range(w)] for y in range(h)]
    while k >= 0:
        y = random.randrange(w)
        x = random.randrange(h)
        if matrix[x][y] != '*':
            matrix[x][y] = '*'
            k-=1
        
    return matrix

print(minesweeper(15,20,120))