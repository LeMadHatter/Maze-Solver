from point import Point
from line import Line

class Cell():
    def __init__(self, x1, y1, x2, y2, window, has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.window = window
        #corners starting from top left going clockwise
        self.corners = [
            Point(self.x1, self.y1),
            Point(self.x2, self.y1),
            Point(self.x2, self.y2),
            Point(self.x1, self.y2)
        ]
        #Lines starting from top going clockwise
        self.lines = [
            Line(self.corners[0], self.corners[1]),
            Line(self.corners[1], self.corners[2]),
            Line(self.corners[2], self.corners[3]),
            Line(self.corners[3], self.corners[0])
        ]
        self.center = self.get_center()

    def draw(self): #x1,y1 is top left, x2,y2 is bottom right
        if self.has_top_wall:
            self.window.draw_line(self.lines[0], "black")
        if self.has_right_wall:
            self.window.draw_line(self.lines[1], "black")
        if self.has_bottom_wall:
            self.window.draw_line(self.lines[2], "black")
        if self.has_left_wall:
            self.window.draw_line(self.lines[3], "black")

    def draw_move(self, to_cell, undo=False):
        move = Line(self.center, to_cell.center)
        color = "red"
        if undo:
            color = "gray"
        move.draw(self.window.canvas, color)

    def get_center(self):
        return Point((self.x2 + self.x1) / 2, (self.y2 + self.y1) / 2)

