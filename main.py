'''import tkinter as tk
def generate_mazes():
    print('in generate mazes')
root = tk.Tk()
root.title('AI Project')
frame = tk.Frame(root)
frame.pack(fill='x', padx=100, pady=5)
lbl = tk.Label(frame, text='Enter the no. of mazes: ')
lbl.pack(side='left', padx=5, pady=5)
ent = tk.Entry(frame)
ent.pack(fill='x', padx=500)
btn = tk.Button(frame, text='Generate Mazes', command=generate_mazes)
btn.pack()
root.mainloop()
'''

import tkinter as tk
import heapq
import time
mazes = None
paths = [] 
from tkinter import messagebox
import random
from tkinter import ttk
from collections import deque
class MazeGUI:
    def __init__(self, root, maze, path):
        self.root = root
        self.maze = maze
        self.path = path
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.cell_size = 20  # Default cell size, you can adjust this
        self.canvas_size = self.cell_size * max(self.rows, self.cols)

        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size)
        self.canvas.pack()

        self.draw_maze()
        self.draw_robot()

    def calculate_window_size(self):
        # Calculate the window size based on the maze size
        self.canvas_size = self.cell_size * max(self.rows, self.cols)
        self.root.geometry(f"{self.canvas_size}x{self.canvas_size}")

    def draw_maze(self):
        self.calculate_window_size()

        for i in range(self.rows):
            for j in range(self.cols):
                x0, y0 = j * self.cell_size, i * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size

                if self.maze[i][j] == 1:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="black")

    def draw_robot(self):
        start = (0, 0)
        goal = (self.rows - 1, self.cols - 1)
        self.canvas.create_rectangle(goal[1] * self.cell_size, goal[0] * self.cell_size,
                                     (goal[1] + 1) * self.cell_size, (goal[0] + 1) * self.cell_size, fill="red")

        if self.path is not None:
            for node in self.path:
                x0, y0 = node[1] * self.cell_size, node[0] * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="lightgreen", outline="green")
                self.root.update()  # Update the GUI to show the rectangle
                self.root.after(100)  # Add a delay of 100 milliseconds
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="lightblue", outline="blue")
                

        # Draw the robot and goal
        self.canvas.create_rectangle(start[1] * self.cell_size, start[0] * self.cell_size,
                                     (start[1] + 1) * self.cell_size, (start[0] + 1) * self.cell_size, fill="lightgreen", outline="green")
        self.canvas.create_rectangle(goal[1] * self.cell_size, goal[0] * self.cell_size,
                                     (goal[1] + 1) * self.cell_size, (goal[0] + 1) * self.cell_size, fill="red", outline="pink")



def generate_maze(rows, cols, obstacle_probability):
    maze = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if random.random() < obstacle_probability:
                maze[i][j] = 1

    return maze
def heuristic(a, b):
        # Manhattan distance as the heuristic function
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(maze, node):
    neighbors = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
    rows = len(maze)
    cols = len(maze[0])
    for dir in directions:
        new_node = (node[0] + dir[0], node[1] + dir[1])
        if 0 <= new_node[0] < rows and 0 <= new_node[1] < cols and maze[new_node[0]][new_node[1]] == 0:
            neighbors.append(new_node)

    return neighbors

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

def bfs(maze, start, goal):
    start_time = time.time()
    queue = deque([start])
    came_from = {start: None}
    rows = len(maze)
    cols = len(maze[0])

    while queue:
        current_node = queue.popleft()

        if current_node == goal:
            path = reconstruct_path(came_from, start, goal)
            return [path, time.time() - start_time]

        for neighbor in get_neighbors(maze, current_node):
            if neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current_node

    return [None, None]  # No path found

def a_star(maze, start, goal):
    start_time = time.time()
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    rows = len(maze)
    cols = len(maze[0])

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        if current_node == goal:
            path = reconstruct_path(came_from, start, goal)
            return [path, time.time() - start_time]

        for neighbor in get_neighbors(maze, current_node):
            new_cost = cost_so_far[current_node] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current_node

    return [None, None]  # No path found

def reconstruct_path(came_from, start, goal):
    path = []
    current_node = goal

    while current_node is not None:
        path.append(current_node)
        current_node = came_from[current_node]

    path.reverse()
    return path

def show_path():
    print('in show path')

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def show_path_new(maze_ind, path_ind):
    global mazes
    global paths
    print(maze_ind, path_ind)
    new_window = tk.Tk()
    new_window.title('A* Path')
    gui = MazeGUI(new_window, mazes[maze_ind], paths[maze_ind][path_ind][0])
    new_window.mainloop()

def shownew_mazes():
    global mazes
    global paths
    no_of_mazes = len(mazes)

    # Create a Canvas and add it to a Scrollbar
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    canvas.bind_all("<MouseWheel>", on_mousewheel)
    # Create a Frame inside the Canvas
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    for i in range(no_of_mazes):
        lbl = tk.Label(canvas, text=f'Maze {i + 1}', width=15, font=('TkDefaultFont', 12))
        lbl.grid(row=i, column=0, padx=40, pady=5)
        
        lbl = tk.Label(canvas, text=f'{paths[i][1][1]}', width=15, font=('TkDefaultFont', 12))
        lbl.grid(row=i, column=1, padx=40, pady=5)
        BFS_btn = tk.Button(canvas, text='BFS', command=lambda i=i : show_path_new(i, 1))
        BFS_btn.grid(row=i, column=2, padx=40, pady=5)

        lbl = tk.Label(canvas, text=f'{paths[i][2][1]}', width=15, font=('TkDefaultFont', 12))
        lbl.grid(row=i, column=3, padx=40, pady=5)
        DFS_btn = tk.Button(canvas, text='DFS', command=lambda i=i: show_path_new(i, 2))
        DFS_btn.grid(row=i, column=4, padx=40, pady=5)
        
        lbl = tk.Label(canvas, text=f'{paths[i][0][1]}', width=15, font=('TkDefaultFont', 12))
        lbl.grid(row=i, column=5, padx=40, pady=5)
        A_btn = tk.Button(canvas, text='A*', command=lambda i=i: show_path_new(i, 0))
        A_btn.grid(row=i, column=6, padx=40, pady=5)
        
        lbl = tk.Label(canvas, text='Flood Fill', width=15, font=('TkDefaultFont', 12))
        lbl.grid(row=i, column=7, padx=40, pady=5)
        FF_btn = tk.Button(canvas, text='Flood Fill', command=show_path)
        FF_btn.grid(row=i, column=8, padx=40, pady=5)
def show_mazes():
    global mazes
    no_of_mazes = len(mazes)
    for i in range(no_of_mazes):
        frame = tk.Frame(root)
        frame.pack(fill='x', padx=100, pady=5)
        lbl = tk.Label(frame, text=f'Maze {i + 1}', width=15, font=('TkDefaultFont', 12))
        lbl.pack(side='left', padx=5, pady=5)
        lbl = tk.Label(frame, text='BFS', width=15, font=('TkDefaultFont', 12))
        lbl.pack(side='left', padx=25, pady=5)
        BFS_btn = tk.Button(frame, text='BFS', command=show_path)
        BFS_btn.pack(side='left', padx=40, pady=5)
        lbl = tk.Label(frame, text='DFS', width=15, font=('TkDefaultFont', 12))
        lbl.pack(side='left', padx=40, pady=5)
        DFS_btn = tk.Button(frame, text='DFS', command=show_path)
        DFS_btn.pack(side='left', padx=40, pady=5)
        lbl = tk.Label(frame, text='A*', width=15, font=('TkDefaultFont', 12))
        lbl.pack(side='left', padx=40, pady=5)
        A_btn = tk.Button(frame, text='A*', command=show_path)
        A_btn.pack(side='left', padx=40, pady=5)
        lbl = tk.Label(frame, text='Flood Fill', width=15, font=('TkDefaultFont', 12))
        lbl.pack(side='left', padx=40, pady=5)
        FF_btn = tk.Button(frame, text='Flood Fill', command=show_path)
        FF_btn.pack(side='left', padx=40, pady=5)

def generate_mazes(maze_ent, row_ent, col_ent):
    global mazes
    global paths
    print('in generate mazes')
    try:
        no_of_mazes = int(maze_ent.get())
        rows = int(row_ent.get())
        cols = int(col_ent.get())
        mazes = []
        wall_prob = 0.25
        for i in range(no_of_mazes):
            mazes.append(generate_maze(rows, cols, wall_prob))
        start = (0, 0)
        goal = (rows - 1, cols - 1)
        for maze in mazes:
            #do something
            maze_paths = []
            path = a_star(maze, start, goal)
            maze_paths.append(path)
            path = bfs(maze, start, goal)
            maze_paths.append(path)
            start_time = time.time()
            path = dfs(maze, start, goal, [])
            duration = time.time() - start_time
            if path:
                maze_paths.append([path, duration])
            else:
                maze_paths.append([None, None])

            paths.append(maze_paths)
        a_sum = 0
        b_sum = 0
        d_sum = 0

        print(len(mazes))
        print(mazes[:1])
        shownew_mazes()
    except ValueError:
        messagebox.showerror('Error', 'You have entered invalid input! Please try again.')


def show_menu():
    frame = tk.Frame(root)
    frame.pack(fill='x', padx=100, pady=5)

    lbl = tk.Label(frame, text='Enter the no. of mazes: ', width=25, font=('TkDefaultFont', 12))
    lbl.pack(side='left', padx=5, pady=5)

    maze_ent = tk.Entry(frame, width=8, font=('TkDefaultFont', 12))
    maze_ent.pack(side='left', padx=100)

    lbl = tk.Label(frame, text='Enter the no. of rows: ', width=25, font=('TkDefaultFont', 12))
    lbl.pack(side='left', padx=5, pady=5)

    row_ent = tk.Entry(frame, width=8, font=('TkDefaultFont', 12))
    row_ent.pack(side='left', padx=100)

    lbl = tk.Label(frame, text='Enter the no. of columns: ', width=25, font=('TkDefaultFont', 12))
    lbl.pack(side='left', padx=5, pady=5)

    col_ent = tk.Entry(frame, width=8, font=('TkDefaultFont', 12))
    col_ent.pack(side='left', padx=100)
    btn = tk.Button(frame, text='Generate Mazes', command=lambda : generate_mazes(maze_ent, row_ent, col_ent), width=16, height=4)
    btn.pack(side='right', padx=50)

    root.mainloop()

root = tk.Tk()
root.title('AI Project')
show_menu()
