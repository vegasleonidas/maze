from window_class import *

def main():
    win = Window(400, 400)
    
    cell1 = Cell(50, 50, 100, 100, win)
    cell1.draw()
    
    cell2 = Cell(100, 50, 150, 100, win)
    cell2.has_left_wall = False  # Removing left wall to connect to cell1
    cell2.draw()
    
    cell1.draw_move(cell2)

    win.wait_for_close()

if __name__ == "__main__":
    main()