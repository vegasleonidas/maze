from window_class import Window, Point, Line

def main():
    win = Window(800, 600)

    # Create points
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(200, 100)
    p4 = Point(300, 200)
    
    # Create lines
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    
    # Draw lines
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")

    win.wait_for_close()

if __name__ == "__main__":
    main()