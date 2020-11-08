import random
def tic_tac_toe(x):
    if x < 3:
        return "Sorry! It atleast needs 3X3"

    w = h = x
    board = [["." for i in range(w)] for j in range(h)]
    
    next_input = ''
    skip_input = ''
    k = w * h
    while k > 0:
        if skip_input:
            next_input = skip_input
        elif next_input == 'O':
            next_input = 'X'
        else:
            next_input = 'O'
        x = random.randrange(h)
        y = random.randrange(w)
        if board[x][y] != 'X' and board[x][y] != 'O':
            board[x][y] = next_input
            k -= 1
            skip_input = ''
        else:
            skip_input = next_input
    
    for i in range(w):
        temp = []
        for j in range(h):
            temp.append(board[i][j])
        print(temp)

    cross_compare = 0
    vertical_compare = 0
    reverse_cross_compare = 0
    horizontal_compare = 0
    
    for i in range(w):
        horizontal_compare = 0
        for j in range(h):
            if (i == j and i < w-1 and j < h-1 and board[i][j] == board[i+1][j+1]):
                cross_compare += 1
            
            if (j < h-1 and board[i][j] == board[i][j+1]):
                horizontal_compare += 1
        
        if horizontal_compare == w-1:
            return "Player won through horizontal pair."

    if  cross_compare == w-1:
        return "Player won through cross compare pair." 

    for i in range(h):
        vertical_compare = 0
        for j in range(w):
            if (j < w-1 and board[j][i] == board[j+1][i]):
                vertical_compare += 1
        if vertical_compare == w-1:
            return "Player won through vertical pair."

    j = h-1
    for i in range(w):
        if (j > 0 and board[i][j] == board[i+1][j-1]):
            reverse_cross_compare += 1
        j -= 1

    if reverse_cross_compare == w-1:
        return "Player won through reverse cross pair." 

    return "Oops! No player won..."

print(tic_tac_toe(3))