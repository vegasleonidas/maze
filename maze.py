from cell import *
import random
import time 
from window_class import *

class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed is not None:
            random.seed(seed)
        
        self._cells = []
        self._create_cells()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._break_entrance_and_exit()
    
    def _create_cells(self):
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                x1 = self.x1 + i * self.cell_size_x
                y1 = self.y1 + j * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                cell = Cell(x1, y1, x2, y2, self.win)
                column.append(cell)
            self._cells.append(column)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        cell = self._cells[i][j]
        cell.draw()
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        """Removes the entrance and exit walls and updates the drawing."""
        # Remove top wall of the entrance (top-left cell)
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        
        # Remove bottom wall of the exit (bottom-right cell)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)


    def _break_walls_r(self, i, j):
        cell = self._cells[i][j]
        cell.visited = True
        
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        random.shuffle(directions)
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.num_cols and 0 <= nj < self.num_rows and not self._cells[ni][nj].visited:
                if di == -1:  # Move left
                    cell.has_left_wall = False
                    self._cells[ni][nj].has_right_wall = False
                elif di == 1:  # Move right
                    cell.has_right_wall = False
                    self._cells[ni][nj].has_left_wall = False
                elif dj == -1:  # Move up
                    cell.has_top_wall = False
                    self._cells[ni][nj].has_bottom_wall = False
                elif dj == 1:  # Move down
                    cell.has_bottom_wall = False
                    self._cells[ni][nj].has_top_wall = False
                
                self._draw_cell(i, j)
                self._break_walls_r(ni, nj)
    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        
        cell = self._cells[i][j]
        cell.visited = True
        
        # If the goal is reached (bottom-right cell), return True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        # Possible movements: left, right, up, down
        directions = [(0, -1, "top_wall"), (1, 0, "right_wall"), (0, 1, "bottom_wall"), (-1, 0, "left_wall")]
        
        for di, dj, wall in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < self.num_cols and 0 <= nj < self.num_rows:
                next_cell = self._cells[ni][nj]
                
                if not next_cell.visited and not getattr(cell, f"has_{wall}"):
                    cell.draw_move(next_cell)
                    
                    if self._solve_r(ni, nj):
                        return True
                    
                    # Undo move if path doesn't lead to solution
                    cell.draw_move(next_cell, undo=True)
        
        return False