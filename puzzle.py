#!/usr/bin/python3
import copy

FLAG_LEFT = -1
FLAG_RIGHT = 1
FLOWER_SMALL = -2
FLOWER_BIG = 2
FISH_HEAD = -3
FISH_TAIL = 3
BIRD_HEAD = -4
BIRD_TAIL = 4

pieces = [
    [FISH_TAIL, FLAG_LEFT, FLOWER_SMALL, BIRD_HEAD], #No text
    [BIRD_TAIL, FLOWER_SMALL, FISH_HEAD, FLAG_RIGHT], #Both texts
    [FISH_TAIL, FLOWER_BIG, BIRD_TAIL, FLAG_LEFT], #Brainmadestonia
    [FLAG_LEFT, FISH_HEAD, BIRD_TAIL, BIRD_HEAD], #Brainmadestonia
    [FISH_HEAD, FLAG_LEFT, BIRD_TAIL, FLOWER_BIG], #Brainmadestonia
    [FLAG_LEFT, FLOWER_SMALL, BIRD_TAIL, FLOWER_BIG], #Brainmadestonia
    [FISH_TAIL, FLAG_LEFT, BIRD_TAIL, FLOWER_BIG], #Brainmadestonia
    [FISH_HEAD, FLOWER_SMALL, BIRD_HEAD, FLAG_RIGHT], #Portel
    [FLOWER_BIG, FISH_HEAD, FISH_TAIL, FLAG_RIGHT] #Portel
]

def rotate(piece, amt):
    new_piece = []

    for i in range(len(piece)):
        new_piece.append(piece[(i + amt) % 4])
    return new_piece

def transform(grid):
    transformed = []
    line = []
    for i in range(len(grid)):
        line.append(grid[i])

        if len(line) == 3:
            transformed.append(line)
            line = []
    return transformed

def assemble(grid, pool):
    if len(pool) == 0:
        if check(transform(grid)):
            print(to_string(transform(grid)))

    if not check(transform(grid)):
        return

    for piece in pool:
        new_pool = copy.deepcopy(pool)
        new_pool.remove(piece)

        grid0 = copy.deepcopy(grid)
        grid0.append(piece)
        assemble(grid0, new_pool)

        grid1 = copy.deepcopy(grid)
        grid1.append(rotate(piece, 1))
        assemble(grid1, new_pool)

        grid2 = copy.deepcopy(grid)
        grid2.append(rotate(piece, 2))
        assemble(grid2, new_pool)

        grid3 = copy.deepcopy(grid)
        grid3.append(rotate(piece, 3))
        assemble(grid3, new_pool)

def check(grid):
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if i > 0 and grid[j][i - 1][1] != -grid[j][i][3]:
                return False
            
            if j > 0 and grid[j - 1][i][2] != -grid[j][i][0]:
                return False
            
    return True

def to_string(grid):
    s = ""
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i][0] < 0:
                s += "   "
            else:
                s += "    "
            s += str(grid[j][i][0]) + " "

        s += "\n"

        for i in range(len(grid[j])):
            if grid[j][i][3] < 0:
                s += " "
            else:
                s += "  "
            
            s += str(grid[j][i][3])

            if grid[j][i][1] < 0:
                s += " "
            else:
                s += "  "
            
            s += str(grid[j][i][1])

        s += "\n"
        
        for i in range(len(grid[j])):
            if grid[j][i][2] < 0:
                s += "   "
            else:
                s += "    "
            s += str(grid[j][i][2]) + " "

        s += "\n"

    return s

test_grid = [
    [[1, 2, -1, -2], [-1, 2, 1, -2]], 
    [[1, 2, -1, -2], [-1, 2, 1, -2]]
]

pool = pieces

assemble([], pool)

print(to_string(test_grid))
print(check(test_grid))
