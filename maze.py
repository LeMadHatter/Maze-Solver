from cell import Cell
import time, random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        if not self.seed is None:
            random.seed(self.seed)
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for x in range(self.num_cols):
            self._cells.append([])
            for y in range(self.num_rows):
                x1 = self.x1 + x * self.cell_size_x
                x2 = self.x1 + x * self.cell_size_x + self.cell_size_x
                y1 = self.y1 + y * self.cell_size_y
                y2 = self.y1 + y * self.cell_size_y + self.cell_size_y

                self._cells[x].append(Cell(x1, y1, x2, y2, self.win))
        
                self._draw_cells(x, y)

    def _draw_cells(self, x, y):
            try:
                self._cells[x][y].draw()
            except:
                return
            self._animate()
                
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[self.num_cols-1][self.num_rows-1].has_right_wall = False
        self._draw_cells(0, 0)
        self._draw_cells(self.num_rows-1, self.num_cols-1)

    def _break_walls_r(self, x, y):
        self._cells[x][y].visited = True
        while True:
            to_visit = []
            if x-1 >= 0 and not self._cells[x-1][y].visited:
                to_visit.append((x-1, y))
            if x+1 < self.num_cols and not self._cells[x+1][y].visited:
                to_visit.append((x+1, y))
            if y+1 < self.num_rows and not self._cells[x][y+1].visited:
                to_visit.append((x, y+1))
            if y-1 >= 0 and not self._cells[x][y-1].visited:     
                to_visit.append((x, y-1))
            if len(to_visit) == 0:
                return
            else:
                direction = random.choice(to_visit)
                if direction == (x-1, y):
                    self._cells[x][y].has_left_wall = False
                    self._cells[x-1][y].has_right_wall = False
                if direction == (x+1, y):
                    self._cells[x][y].has_right_wall = False
                    self._cells[x+1][y].has_left_wall = False
                if direction == (x, y+1):
                    self._cells[x][y].has_bottom_wall = False
                    self._cells[x][y+1].has_top_wall = False
                if direction == (x, y-1):
                    self._cells[x][y].has_top_wall = False
                    self._cells[x][y-1].has_bottom_wall = False
                self._draw_cells(x, y)
                self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, x, y):
        self._animate()
        current_cell = self._cells[x][y]
        current_cell.visited = True
        if current_cell == self._cells[-1][-1]:
            return True
        
        if x-1 >= 0 and not current_cell.has_left_wall and not self._cells[x-1][y].visited:
            current_cell.draw_move(self._cells[x-1][y])
            next_cell = self._solve_r(x-1, y)
            if next_cell:
                return True
            else:
                current_cell.draw_move(self._cells[x-1][y], undo=True)

        if x+1 < self.num_cols and not current_cell.has_right_wall and not self._cells[x+1][y].visited:
            current_cell.draw_move(self._cells[x+1][y])
            next_cell = self._solve_r(x+1, y)
            if next_cell:
                return True
            else:
                current_cell.draw_move(self._cells[x+1][y], undo=True)

        if y-1 >= 0 and not current_cell.has_top_wall and not self._cells[x][y-1].visited:
            current_cell.draw_move(self._cells[x][y-1])
            next_cell = self._solve_r(x, y-1)
            if next_cell:
                return True
            else:
                current_cell.draw_move(self._cells[x][y-1], undo=True)

        if y+1 < self.num_rows and not current_cell.has_bottom_wall and not self._cells[x][y+1].visited:
            current_cell.draw_move(self._cells[x][y+1])
            next_cell = self._solve_r(x, y+1)
            if next_cell:
                return True
            else:
                current_cell.draw_move(self._cells[x][y+1], undo=True)

        return False