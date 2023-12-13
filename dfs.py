def dfs(maze, start, goal, path = []):
    
    if(start == goal):
        return path + [goal]
    
    i, j = start
    if(0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] == 0):
        maze[i][j] = 2
        for direction in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            next_i, next_j = i + direction[0], j + direction[1]
            next_pos = (next_i, next_j)
            if(0 <= next_i < len(maze) and 0 <= next_j < len(maze[0]) and maze[next_i][next_j] == 0):
                new_path = dfs(maze, next_pos, goal, path + [start])
                if new_path:
                    return new_path

    return None


maze = [
    [1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start_point = (0, 0)
end_point = (4, 4)

result_path = dfs(maze, start_point, end_point)

if result_path:
    print("Path found:", result_path)
else:
    print("No path found.")

