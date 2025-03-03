import unittest
from maze import Maze

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

if __name__ == "__main__":
    unittest.main()
