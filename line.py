class Line():
    def __init__(self, point_A, point_B):
        self.point_A = point_A
        self.point_B = point_B

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_A.x, self.point_A.y, self.point_B.x, self.point_B.y, fill=fill_color, width=2)
