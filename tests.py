import unittest 
from unittest.mock import MagicMock
from maze import Maze
from window_class import Window, Line, Point
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_maze_different_sizes(self):
        m2 = Maze(0, 0, 5, 8, 15, 15)
        self.assertEqual(len(m2._cells), 8)
        self.assertEqual(len(m2._cells[0]), 5)
        
        m3 = Maze(0, 0, 20, 20, 5, 5)
        self.assertEqual(len(m3._cells), 20)
        self.assertEqual(len(m3._cells[0]), 20)

    def test_break_entrance_and_exit(self):
        win = None  # Mock window
        maze = Maze(0, 0, 5, 5, 10, 10, win)
        maze._break_entrance_and_exit()

        self.assertFalse(maze._cells[0][0].has_top_wall, "Entrance wall should be removed.")
        self.assertFalse(maze._cells[4][4].has_bottom_wall, "Exit wall should be removed.")

        mock_window = MagicMock(Window)
        maze = Maze(0, 0, 5, 5, 20, 20, mock_window)
        maze._break_entrance_and_exit()
        
        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[maze.num_cols - 1][maze.num_rows - 1].has_bottom_wall)
        mock_window.draw_line.assert_called()

    def test_reset_cells_visited(self):
        maze = Maze(0, 0, 5, 5, 10, 10)
        
        # Mark all cells as visited manually
        for column in maze._cells:
            for cell in column:
                cell.visited = True
        
        # Reset visited status
        maze._reset_cells_visited()
        
        # Check if all cells are reset to False
        for column in maze._cells:
            for cell in column:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()
