def replaceString(row, index, replacement):
    text = ""
    for i in range(0, len(row)):
        if i == index:
            text += replacement
        else:
            text += row[i]
    
    return text

def plantBomb(grid, timing):
    grid_height = len(grid)
    grid_len = len(grid[0])
    
    for i in range(0, grid_height):
        for j in range(0, grid_len):
            if grid[i][j] == ".":
                grid[i] = replaceString(grid[i], j, "O")
                timing[i][j] = 1
            else:
                timing[i][j] = timing[i][j] + 1
    
    return (grid, timing)

def blast(grid, timing):
    grid_height = len(grid)
    grid_len = len(grid[0])
    
    for i in range(0, grid_height):
        for j in range(0, grid_len):
            if grid[i][j] == "O" and timing[i][j] == 3:
                    grid[i] = replaceString(grid[i], j, ".")
                    timing[i][j] = 0
                    
                    if i - 1 >= 0 and not (grid[i - 1][j] == "O" and timing[i-1][j] == 3):
                        grid[i - 1] = replaceString(grid[i-1], j, ".")
                        timing[i - 1][j] = 0
                    
                    if i + 1 < grid_height and not (grid[i+1][j] == "O" and timing[i+1][j] == 3):
                        grid[i + 1] = replaceString(grid[i + 1], j, ".")
                        timing[i + 1][j] = 0
                        
                    if j - 1 >= 0 and not (grid[i][j-1] == "O" and timing[i][j-1] == 3):
                        grid[i] = replaceString(grid[i], j - 1, ".")
                        timing[i][j - 1] = 0
                    
                    if j + 1 < grid_len and not (grid[i][j+1] == "O" and timing[i][j+1] == 3):
                        grid[i] = replaceString(grid[i], j + 1, ".")
                        timing[i][j + 1] = 0
            elif grid[i][j] == "O":
                timing[i][j] = timing[i][j] + 1
        
    return (grid, timing)
    

def bomberMan(n, grid):
    timing = [[1 for i in range(0, len(grid[j]))] for j in range(len(grid))]
    
    plant_bomb = False
    while n > 0:
        print("--------------------------")
        print(grid)
        print(timing)
        if plant_bomb:
            grid, timing = plantBomb(grid, timing)
        else:
            grid, timing = blast(grid, timing)
        
        plant_bomb = not plant_bomb
        
        n -= 1
    
    print("=============================================")
    return grid
    

gr = [".......",
"...O...",
"....O..",
".......",
"OO.....",
"OO....."]
print(bomberMan(3, gr))

