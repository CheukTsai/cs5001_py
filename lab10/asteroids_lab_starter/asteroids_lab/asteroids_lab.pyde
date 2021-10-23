SIZE = (600, 600)
thrust_factor = 0
spaceship_x = 300
spaceship_y = 300
x_vel = 0
y_vel = 0
rotation = 0


def setup():
    size(*SIZE)
    colorMode(RGB, 1)


def draw():
    global rotation
    background(0)
    draw_spaceship()


def keyPressed():
    global rotation
    global thrust_factor
    if (key == CODED):
        if keyCode == UP:
            thrust_factor = 0.5
        if keyCode == RIGHT:
            rotation += 3
        if keyCode == LEFT:
            rotation -= 3
            
def draw_spaceship():
    global spaceship_x
    global spaceship_y
    global x_vel
    global y_vel
    global thrust_factor
    x_vel = (x_vel + sin(radians(rotation))) * thrust_factor
    y_vel = (y_vel - cos(radians(rotation))) * thrust_factor
    
    spaceship_x = spaceship_x + x_vel
    spaceship_y = spaceship_y + y_vel
    translate(spaceship_x, spaceship_y)
    rotate(radians(rotation))
    fill(0)
    stroke(1)
    strokeWeight(3)
    triangle(-16, 10,  0, -30, 16, 10)
