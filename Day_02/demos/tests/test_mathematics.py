from d4_mathematics import divide, hypotenuse, multiply, round_up


def test_multiply():
    assert multiply(4, 5) == 20
    # assert multiply(1, 1) == 1 # We could use many lines to tests different results, but it's good practice to make a test for each case, in that example by creating a new function test_multiply_by_one with assert in it


def test_divide(): # Make a test before creating the function
    assert divide(4, 5) == 0.8


def test_round_up():
    assert round_up(2.4) == 3

def test_hypotenuse():
    """Returns the longest side of a right-angled triangle.

    Pythagorean Theorem: a² + b² = c²
    3² + 4² = 5²
    9  + 16 = 25
    """
    assert hypotenuse(3, 4) == 5
