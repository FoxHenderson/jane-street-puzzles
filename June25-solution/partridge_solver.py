from copy import deepcopy

def partridge_tilings(partial_grid, tiles):
    grid = deepcopy(partial_grid)
    remaining_tiles = deepcopy(tiles)

    def backtrack(grid, remaining_tiles):
        pos = find_first_empty(grid)
        
        # check if configuration works
        if pos is None: 
            yield deepcopy(grid)
            print(f"solution found")
            return
        
        row, col = pos

        for size in sorted(remaining_tiles.keys()):
            if remaining_tiles[size] > 0 and is_valid_placement(grid, row, col, size):
                place_tile(grid, row, col, size)
                remaining_tiles[size] -= 1
                yield from backtrack(grid, remaining_tiles)
                remaining_tiles[size] += 1
                unplace_tile(grid, row, col, size)

    return backtrack(grid, remaining_tiles)

def find_first_empty(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 0:
                return i, j
    return None

def is_valid_placement(grid, row, col, size):
    S = len(grid)
    if row + size > S or col + size > S:
        return False
    for i in range(size):
        for j in range(size):
            if grid[row + i][col + j] != 0:
                return False
    return True

def place_tile(grid, row, col, size):
    for i in range(size):
        for j in range(size):
            grid[row + i][col + j] = size

def unplace_tile(grid, row, col, size):
    for i in range(size):
        for j in range(size):
            grid[row + i][col + j] = 0
        
# in this case consider 45x45 grid
N = 9
S = 45

# image 1
image = [[0]*S for _ in range(S)]
# tile dimension : quantity remaining
remaining_tiles = {1:1, 2:1, 3:2, 4:2, 5:3, 6:5, 7:2, 8:2, 9:1}

solutions = list(partridge_tilings(image, remaining_tiles))
print(f"{len(solutions)} solution(s) for preset")
print(solutions[0])
#print(image)
