size_x = 600
size_y = 600
circle_x = 300
circle_rad = 75


def setup():
    size(size_x, size_y)
    strokeWeight(3)
    colorMode(RGB, 1)


def draw():
    global circle_x
    background(0)
    circle_x = circle_x + 1
    
    if circle_x > size_x + circle_rad:
        circle_x = circle_x - size_x
    elif circle_x > size_x - circle_rad:
        draw_circle_1(circle_x - size_x)
        draw_circle_2(circle_x - size_x)
        draw_circle_3(circle_x - size_x)
    draw_circle_1(circle_x)
    draw_circle_2(circle_x)
    draw_circle_3(circle_x)



def draw_circle_1(x):
    fill(0.5, 0.5, 0.5)
    stroke(1.0, 1.0, 1.0)
    ellipse(x, 100, circle_rad*2, circle_rad*2)


def draw_circle_2(x):
    fill(0.8, 0.9, 1.0)
    stroke(1.0, 1.0, 1.0)
    ellipse(x, 300, circle_rad*2, circle_rad*2)


def draw_circle_3(x):
    fill(0.5, 0.5, 0.5)
    stroke(1.0, 1.0, 1.0)
    ellipse(x, 500, circle_rad*2, circle_rad*2)
