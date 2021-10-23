from asteroid import Asteroid

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

SPACE_WIDTH = 100
SPACE_HEIGHT = 100


def test_constructor():
    SPACE = {'w': SPACE_WIDTH, 'h': SPACE_HEIGHT}

    # Test minimal required constructor args
    a = Asteroid(SPACE)
    assert a.SPACE['w'] == SPACE_WIDTH and \
        a.SPACE['h'] == SPACE_HEIGHT and \
        hasattr(a, "x") and \
        hasattr(a, "y") and \
        hasattr(a, "x_vel") and \
        hasattr(a, "y_vel") and \
        hasattr(a, "rotation") and \
        hasattr(a, "rot_vel") and \
        a.asize == 'Large'

    # Test with optional size value
    b = Asteroid(SPACE, 'Small')
    assert b.asize == 'Small'

    # Test with insufficient arguments
    try:
        c = Asteroid()
    except TypeError:
        failedWithTypeError = True
    assert failedWithTypeError
