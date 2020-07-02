import random
def putbattleship(height, width, k) -> int:
    board = [["." for i in range(width)] for j in range(width)]
    if width == 0 or height == 0 or k > (height * width):
        return 0
    

    while k > 0:
        x = random.randrange(height)
        y = random.randrange(width)
        if board[x][y] != 'X':
            if (x > 0 and board[x-1][y] == '.'):
                if (y > 0 and board[x][y-1] == '.'):
                    board[x][y] = "X"
                    k-=1
    
    return board

print(putbattleship(8,8,26))            

#    y  y  y  y
# x  0  0  0  0
# x  0  0  0  0
# x  0  0  0  0
