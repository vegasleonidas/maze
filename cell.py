from window_class import *

class Cell:
    def __init__(self, x1, y1, x2, y2, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        
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