from maze import Maze
from window_class import Window

def main():

    win = Window(800, 600)
    maze = Maze(50, 50, 10, 10, 50, 50, win)
    if maze.solve():
        print("Maze solved!")
    else:
        print("No solution found.")
    win.wait_for_close()

if __name__ == "__main__":
    main()