import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(m1._cells[0][0].has_left_wall, False)
        self.assertEqual(m1._cells[11][9].has_right_wall, False)

        num_cols = 20
        num_rows = 18
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(m1._cells[0][0].has_left_wall, False)
        self.assertEqual(m1._cells[-1][-1].has_right_wall, False)
        self.assertEqual(m1._cells[0][0].visited, False)
        self.assertEqual(m1._cells[-1][-1].visited, False)

if __name__ == "__main__":
    unittest.main()