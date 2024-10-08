from cell import Cell
import time

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for y in range(self.num_cols):
            for x in range(self.num_rows):
                x1 = self.x1 + x * self.cell_size_x
                x2 = self.x1 + x * self.cell_size_x + self.cell_size_x
                y1 = self.y1 + y * self.cell_size_y
                y2 = self.y1 + y * self.cell_size_y + self.cell_size_y

                self._cells.append(Cell(x1, y1, x2, y2, self.win))
        
        self._draw_cells()

    def _draw_cells(self):
        for cell in self._cells:
            cell.draw()
            self._animate()
        
        
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)