
def print_maze(maze):
    for i in maze:
        print(i)
    return


def flood_fill(maze, value, current_pos):
    # current_pos = queue.pop(0)
    maze[current_pos[0]][current_pos[1]] = value
    size = len(maze)*len(maze[0])
    
    for direction in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        next_i, next_j = current_pos[0] + direction[0], current_pos[1] + direction[1] 
        next_pos = (next_i, next_j)
        if(0 <= next_i < len(maze) and 0 <= next_j < len(maze[0]) and maze[next_i][next_j] == 0):
            if(maze[next_i][next_j] == 1):
                maze[next_i][next_j] = size*size + 1
            else:
                flood_fill(maze, value + 1, next_pos)

    return


def get_path(maze, start_point, end_point):
    path = [] 
    while(start_point != end_point):
        path.append(start_point)
        mini = 255
        for direction in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            updated_i, updated_j = start_point[0] + direction[0], start_point[1] + direction[1]
            if(0 <= updated_i < len(maze) and 0 <= updated_j < len(maze[0]) and maze[updated_i][updated_j] != -1):
                mininum = min(mini, maze[updated_i][updated_j])
                if(mininum != mini):
                    updated_index = (updated_i, updated_j)
                    mini = mininum
        start_point = updated_index
    
    path.append(start_point)
    return path


maze = [                        
    [0, -1, -1, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, 0, -1, 0],
    [0, -1, -1, -1, 0],
    [0, 0, 0, 0, 0]
]

print_maze(maze)
print()

start_point = (0, 0)
end_point = (4, 4)
value = 1

flood_fill(maze, value, end_point)
print_maze(maze)
print()
path = get_path(maze, start_point, end_point)
print(path)
