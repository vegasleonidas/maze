from tkinter import Tk, BOTH, Canvas

class Cell:
    def __init__(self, x1, y1, x2, y2, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = window
    
    def draw(self):
        """Draws the cell walls, erasing walls that are removed."""
        bg_color = "#d9d9d9"  # Background color
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill_color=bg_color)

        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        else:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fill_color=bg_color)

        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill_color=bg_color)

        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))
        else:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill_color=bg_color)

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        start_x = (self._x1 + self._x2) // 2
        start_y = (self._y1 + self._y2) // 2
        end_x = (to_cell._x1 + to_cell._x2) // 2
        end_y = (to_cell._y1 + to_cell._y2) // 2
        self._win.draw_line(Line(Point(start_x, start_y), Point(end_x, end_y)), fill_color=color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("My Window")
        
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        
        self.__running = False
        
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False
        self.__root.destroy()
    
    def draw_line(self, line: Line, fill_color: str = 'black'):
        line.draw(self.__canvas, fill_color)