import time

def print_maze(maze):
    for i in maze:
        print(i)
    return


def flood(maze, value, current_pos):
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
                flood(maze, value + 1, next_pos)

    return


def get_path(maze, start_point, end_point):

    count = 0
    for direction in [(0, 1), (1, 0)]:
        updated_i, updated_j = start_point[0] + direction[0], start_point[1] + direction[1]
        if(maze[updated_i][updated_j] == 0):
            count = count + 1
    if(count == 2):
        return None

    path = [] 
    start_point1 = (255, 255)
    updated_index = (255, 255)
    while(start_point != end_point):
        start_point1 = start_point
        path.append(start_point)
        mini = 255
        for direction in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            updated_i, updated_j = start_point[0] + direction[0], start_point[1] + direction[1]
            if(0 <= updated_i < len(maze) and 0 <= updated_j < len(maze[0]) and maze[updated_i][updated_j] != -1):
                mininum = min(mini, maze[updated_i][updated_j])
                if(mininum != mini):
                    updated_index = (updated_i, updated_j)
                    mini = mininum
                maze[updated_i][updated_j] = -1
        # print(path)
        if(start_point1 == updated_index):
            return None
        start_point = updated_index
    
    path.append(start_point)
    return path

def get_req_matrix(maze, multiplier):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if(maze[i][j] == 1*multiplier):
                maze[i][j] = -1*multiplier
    return 

def copy_matrix(maze):
    maze1 = [[0 for i in range(len(maze[0]))] for j in range(len(maze))]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            maze1[i][j] = maze[i][j]
    return maze1


def flood_fill(maze, start, end):
    maze1 = copy_matrix(maze)
    value = 1
    get_req_matrix(maze1, 1)
    start_time = time.time()
    flood(maze1, value, end)
    path = get_path(maze1, start, end)
    end_time = time.time()
    get_req_matrix(maze1, -1)
    if(path):
        return [path, round(time.time() - start_time, 7)]
    else:
        return [None, None]


'''maze = [                        
    [0, -1, -1, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, 0, -1, 0],
    [0, -1, -1, -1, 0],
    [0, 0, 0, 0, 0]
]

maze1 = [
        [-1, 0, 0, -1, 0, 0, -1, 0, -1, 0], 
        [0, 0, -1, 0, -1, 0, 0, 0, 0, -1], 
        [0, -1, 0, 0, 0, 0, 0, 0, -1, 0], 
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [-1, 0, 0, 0, 0, 0, -1, -1, -1, 0], 
        [-1, 0, -1, 0, 0, -1, 0, 0, -1, -1], 
        [0, 0, 0, -1, 0, 0, 0, 0, 0, -1], 
        [-1, 0, -1, 0, 0, -1, 0, 0, -1, -1], 
        [-1, 0, 0, -1, 0, -1, 0, 0, 0, 0], 
        [0, -1, 0, -1, 0, 0, 0, 0, 0, 0]]



# print_maze(maze)
# print()

start_point = (0, 0)
end_point = (4, 4)
value = 1

flood(maze1, value, end_point)
print_maze(maze1)
print()
path = get_path(maze1, start_point, end_point)
print(path) ''' 
