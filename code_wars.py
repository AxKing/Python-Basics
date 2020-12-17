"""
Your task is to construct a building which will be a pile of n cubes. 
The cube at the bottom will have a volume of n^3, 
the cube above will have volume of (n-1)^3 and so on until the top 
which will have a volume of 1^3.

You are given the total volume m of the building. 
Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) 
will be an integer m and you have to return the integer n such as 
n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if
 there is no such n.
"""

# code Wars uses this function to determine if something is true or not.
assert_equals(A, B):
    if A != B:
        print("Wrong")
    return A == B

def find_nb(m):
    #m = 1071225
    return_val = -1
    n = 1
    sum_of_cubes = 0
    while m < sum_of_cubes:
        sum_of_cubes += n ** 3
        if m == sum_of_cubes:
            return_val = n
            print("they're equal")
            break
        else:
            n += 1
    return return_val

assert_equals(find_nb(4183059834009), 2022)
assert_equals(find_nb(24723578342962), -1)
assert_equals(find_nb(135440716410000), 4824)
assert_equals(find_nb(40539911473216), 3568)
assert_equals(find_nb(26825883955641), 3218)