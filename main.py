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
mazes = None
paths = None
from tkinter import messagebox
import random
from tkinter import ttk
def generate_maze(rows, cols, obstacle_probability):
    maze = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if random.random() < obstacle_probability:
                maze[i][j] = 1

    return maze
def show_path():
    print('in show path')

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def shownew_mazes():
    global mazes
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
        lbl = tk.Label(frame, text=f'Maze {i + 1}', width=15, font=('TkDefaultFont', 12))
        lbl.grid(row=i, column=0, padx=40, pady=5)
        
        lbl = tk.Label(frame, text=f'BFS', width=15, font=('TkDefaultFont', 12))
        lbl.grid(row=i, column=1, padx=40, pady=5)
        BFS_btn = tk.Button(frame, text='BFS', command=show_path)
        BFS_btn.grid(row=i, column=2, padx=40, pady=5)
        lbl = tk.Label(frame, text=f'DFS', width=15, font=('TkDefaultFont', 12))
        lbl.grid(row=i, column=3, padx=40, pady=5)
        
        DFS_btn = tk.Button(frame, text='DFS', command=show_path)
        DFS_btn.grid(row=i, column=4, padx=40, pady=5)
        
        lbl = tk.Label(frame, text=f'A*', width=15, font=('TkDefaultFont', 12))
        lbl.grid(row=i, column=5, padx=40, pady=5)
        A_btn = tk.Button(frame, text='A*', command=show_path)
        A_btn.grid(row=i, column=6, padx=40, pady=5)
        
        lbl = tk.Label(frame, text='Flood Fill', width=15, font=('TkDefaultFont', 12))
        lbl.grid(row=i, column=7, padx=40, pady=5)
        FF_btn = tk.Button(frame, text='Flood Fill', command=show_path)
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
    print('in generate mazes')
    try:
        no_of_mazes = int(maze_ent.get())
        rows = int(row_ent.get())
        cols = int(col_ent.get())
        mazes = []
        wall_prob = 0.25
        for i in range(no_of_mazes):
            mazes.append(generate_maze(rows, cols, wall_prob))
        for maze in mazes:
            #do something
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
