from laserbeam import LaserBeam
from asteroid import Asteroid
from spaceship import Spaceship
import copy


""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class GameController:
    """
    Maintains the state of the game
    and manages interactions of game elements.
    """

    def __init__(self, SPACE, fadeout):
        """Initialize the game controller"""
        self.SPACE = SPACE
        self.fadeout = fadeout

        self.spaceship_hit = False
        self.asteroid_destroyed = False
        self.asteroids = [Asteroid(self.SPACE)]
        self.laser_beams = []
        self.spaceship = Spaceship(self.SPACE)
        self.lifespan = []

    def update(self):
        TEXT_COLOR = 1
        TEXT_SIZE = 30
        HALF = 2
        TEXT_X_LEFT_1 = 165
        TEXT_X_LEFT_2 = 250
        """Updates game state on every frame"""
        self.do_intersections()

        for asteroid in self.asteroids:
            asteroid.display()

        # ======================================================
        # TODO: Problem 3, Part 2: Laser beam handler
        # Your code will replace (or augment) the next several
        # lines. Laser beam objects should remain in the scene
        # as many frames as their lifespan allows.
        # Begin problem 3 code changes

        """  """

        for i in range(len(self.laser_beams)):
            if self.laser_beams[i].lifespan > 0:
                self.laser_beams[i].lifespan -= 1
                self.laser_beams[i].display()

        # End problem 3, part 2 code changes
        # =======================================================

        self.spaceship.display()

        # Carries out necessary actions if game over
        if self.spaceship_hit:
            if self.fadeout <= 0:
                fill(TEXT_COLOR)
                textSize(TEXT_SIZE)
                text("YOU HIT AN ASTEROID",
                     self.SPACE['w']/HALF - TEXT_X_LEFT_1,
                     self.SPACE['h']/HALF)
            else:
                self.fadeout -= 1

        if self.asteroid_destroyed:
            fill(TEXT_COLOR)
            textSize(TEXT_SIZE)
            text("YOU DESTROYED THE ASTEROIDS!!!",
                 self.SPACE['w']/HALF - TEXT_X_LEFT_2,
                 self.SPACE['h']/HALF)

    def fire_laser(self, x, y, rot):
        """Add a laser beam to the game"""
        x_vel = sin(radians(rot))
        y_vel = -cos(radians(rot))
        self.laser_beams.append(
            LaserBeam(self.SPACE, x, y, x_vel, y_vel)
        )

    def handle_keypress(self, key, keycode=None):
        if (key == ' '):
            if self.spaceship.intact:
                self.spaceship.control(' ', self)
        if (keycode):
            if self.spaceship.intact:
                self.spaceship.control(keycode)

    def handle_keyup(self):
        if self.spaceship.intact:
            self.spaceship.control('keyup')

    def do_intersections(self):
        """ Intersections both hit by spaceship and
        laser beams """
        # ======================================================
        # TODO: Problem 4, Part 1: Intersections
        # Here's where you'll probably want to check for intersections
        # between asteroids and laser beams. Laser beams should be removed
        # from the scene if they hit an asteroid, and the asteroid should
        # blow up (the blow_up_asteroid method also must be written. It's
        # been started for you below).
        #
        # The intersection logic below between the spaceship
        # and asteroids should give a hint as to how this will work.
        # Begin code changes for Problem 4, Part 1: Intersections
        if self.spaceship.intact:
            # Check each asteroid for intersection
            for i in range(len(self.asteroids)):
                for j in range(len(self.laser_beams)):
                    if (
                        abs(self.laser_beams[j].x - self.asteroids[i].x)
                        < max(self.asteroids[i].radius,
                              self.laser_beams[j].radius)
                        and
                        abs(self.laser_beams[j].y - self.asteroids[i].y)
                            < max(
                                self.asteroids[i].radius,
                                self.laser_beams[j].radius)):
                        # We've intersected an asteroid
                        self.blow_up_asteroid(
                            self.asteroids[i], self.laser_beams[j])

        pass

        # End of code changes for Problem 4, Part 1: Intersections
        # ======================================================

        # If the space ship still hasn't been blown up
        if self.spaceship.intact:
            # Check each asteroid for intersection
            for i in range(len(self.asteroids)):
                if (
                    abs(self.spaceship.x - self.asteroids[i].x)
                    < max(self.asteroids[i].radius, self.spaceship.radius)
                    and
                    abs(self.spaceship.y - self.asteroids[i].y)
                        < max(
                            self.asteroids[i].radius, self.spaceship.radius)):
                    # We've intersected an asteroid
                    self.spaceship.blow_up(self.fadeout)
                    self.spaceship_hit = True

    def blow_up_asteroid(self, i, j):
        """ Blow up asteroid after hit """
        # ======================================================
        # TODO: Problem 4, Part 2: Asteroid blow-up

        # Here you'll write the code to blow up an asteroid.
        # The parameters represent the indexes for the list of
        # asteroids and the list of laser beams, indicating
        # which asteroid is hit by which laser beam.

        # You'll need to:
        # A) Remove the hit asteroid from the scene
        # B) Add appropriate smaller asteroids to the scene
        # C) Make sure that the smaller asteroids are positioned
        #    correctly and flying off in the correct directions

        # Specifically. If the large asteroid is hit, it should
        # break into two medium asteroids, which should fly off
        # perpendicularly to the direction of the laser beam.

        # If a medium asteroid is hit, it should break into three
        # small asteroids, two of which should fly off perpendicularly
        # to the direction of the laser beam, and the third
        # should fly off in the same direction that the laser
        # beam had been traveling.

        # If a small asteroid is hit, it disappears.

        # Begin code changes for Problem 4, Part 2: Asteroid blow-up

        if i.asize == "Large":

            med_1 = copy.deepcopy(i)
            med_1.x_vel = -j.y_vel
            med_1.y_vel = j.x_vel
            med_1.asize = "Med"

            med_2 = copy.deepcopy(i)
            med_2.x_vel = j.y_vel
            med_2.y_vel = -j.x_vel
            med_2.asize = "Med"

            self.asteroids.append(med_1)
            self.asteroids.append(med_2)

        elif i.asize == "Med":
            small_1 = copy.deepcopy(i)
            small_1.x_vel = -j.y_vel
            small_1.y_vel = j.x_vel
            small_1.asize = "Small"

            small_2 = copy.deepcopy(i)
            small_2.x_vel = j.y_vel
            small_2.y_vel = -j.x_vel
            small_2.asize = "Small"

            small_3 = copy.deepcopy(i)
            small_3.x_vel = j.x_vel
            small_3.y_vel = j.y_vel
            small_3.asize = "Small"

            self.asteroids.append(small_1)
            self.asteroids.append(small_2)
            self.asteroids.append(small_3)

        self.asteroids.remove(i)
        self.laser_beams.remove(j)

        pass
