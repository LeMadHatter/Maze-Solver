from window import Window
from maze import Maze

def main():
    win = Window(1000, 600)

    # cells = [
    #     # Cell(10, 10, 50, 50, win),
    #     # Cell(50, 50, 100, 100, win, has_bottom_wall=False),
    #     # Cell(50, 0, 100, 50, win, has_right_wall=False, has_top_wall=False),
    #     # Cell(150, 150, 200, 200, win, has_left_wall=False)
    # ]
    # for x in range(1, 1000, 50):
    #     for y in range(1, 600, 50):
    #         cells.append(Cell(x, y, x + 50, y + 50, win))
    # for cell in cells:
    #     cell.draw()
    # for i in range(0, len(cells) - 1):
    #     undo = (i % 2 == 0)
    #     cells[i].draw_move(cells[i + 1], undo)

    maze = Maze(10, 10, 10, 10, 40, 40, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()