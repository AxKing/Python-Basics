"""
Your task is to construct a building which will be a pile of n cubes. \
The cube at the bottom will have a volume of n^3, \
the cube above will have volume of (n-1)^3 and so on until the top \
which will have a volume of 1^3.

You are given the total volume m of the building. \
Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) \
will be an integer m and you have to return the integer n such as \
n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if \
 there is no such n.
"""

# code Wars uses this function to determine if something is true or not.


def assert_equals(A, B):
    print(A == B)
    return A == B


def find_nb(m):
    n = 1
    sum_of_cubes = 0
    while m > sum_of_cubes:
        sum_of_cubes += n ** 3
        if m == sum_of_cubes:
            return_val = n
            break
        elif m < sum_of_cubes:
            return_val = -1
            break
        else:
            n += 1
    return return_val


print("Sum of Cubes")
assert_equals(find_nb(4183059834009), 2022)
assert_equals(find_nb(24723578342962), -1)
assert_equals(find_nb(135440716410000), 4824)
assert_equals(find_nb(40539911473216), 3568)
assert_equals(find_nb(26825883955641), 3218)

"""
You live in the city of Cartesia where all roads \
    are laid out in a perfect grid. \
    You arrived ten minutes too early to an appointment, \
    so you decided to take the opportunity to go for a short walk. \
    The city provides its citizens with a Walk Generating App on \
    their phones -- everytime you press the button \
    it sends you an array of one-letter strings representing \
    directions to walk (eg. ['n', 's', 'w', 'e']). \
    You always walk only a single block for each letter (direction) \
    and you know it takes you one minute to traverse one city block, \
    so create a function that will return true if the walk the app \
    gives you will take you exactly ten minutes (you don't want \
    to be early or late!) and will, of course, return you to \
    your starting point. Return false otherwise.
"""


def is_valid_walk(walk):
    if len(walk) != 10 or len(walk) % 2 == 1:
        return False
    directions = {
        "n": 0,
        "s": 0,
        "e": 0,
        "w": 0
        }
    for direction in walk:
        directions[direction] += 1
    if (
        directions["n"] == directions["s"]
        and directions["e"] == directions["w"]
    ):
        return True
    else:
        return False


print("Is this a valid walk?")
assert_equals(is_valid_walk(
    ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']
    ), True)
assert_equals(is_valid_walk(
    ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']
    ), False)
assert_equals(is_valid_walk(['w']), False)
assert_equals(is_valid_walk(
    ['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']
    ), False)
