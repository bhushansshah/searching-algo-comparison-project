import tkinter as tk
import heapq
import random

class MazeGenerator:
    @staticmethod
    def generate_maze(rows, cols, obstacle_probability):
        maze = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if random.random() < obstacle_probability:
                    maze[i][j] = 1

        return maze

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])

    def heuristic(self, a, b):
        # Manhattan distance as the heuristic function
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, node):
        neighbors = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

        for dir in directions:
            new_node = (node[0] + dir[0], node[1] + dir[1])
            if 0 <= new_node[0] < self.rows and 0 <= new_node[1] < self.cols and self.maze[new_node[0]][new_node[1]] == 0:
                neighbors.append(new_node)

        return neighbors

    def a_star(self, start, goal):
        frontier = [(0, start)]
        came_from = {start: None}
        cost_so_far = {start: 0}

        while frontier:
            current_cost, current_node = heapq.heappop(frontier)

            if current_node == goal:
                path = self.reconstruct_path(came_from, start, goal)
                return path

            for neighbor in self.get_neighbors(current_node):
                new_cost = cost_so_far[current_node] + 1
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.heuristic(goal, neighbor)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current_node

        return None  # No path found

    def reconstruct_path(self, came_from, start, goal):
        path = []
        current_node = goal

        while current_node is not None:
            path.append(current_node)
            current_node = came_from[current_node]

        path.reverse()
        return path

class MazeGUI:
    def __init__(self, root, maze):
        self.root = root
        self.maze = maze
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
        solver = MazeSolver(self.maze)
        path = solver.a_star(start, goal)

        if path is not None:
            for node in path:
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


if __name__ == "__main__":
    # Example maze (1 represents obstacles, 0 represents open space)
    maze_rows = 30
    maze_cols = 30
    obstacle_prob = 0.25  # Adjust this probability as needed

    example_maze = MazeGenerator.generate_maze(maze_rows, maze_cols, obstacle_prob)

    root = tk.Tk()
    root.title("Maze Solver GUI")

    gui = MazeGUI(root, example_maze)

    root.mainloop()
