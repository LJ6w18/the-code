
import math

num_list = [10, -13, 50, 5, 7, 65, -40, 44, 30]

def get_extremes(num_list):
    smallest = math.inf
    largest = -math.inf

    for item in num_list:
        if item < smallest:
            smallest = item
        if item > largest:
            largest = item

    return smallest, largest

smallest, largest = get_extremes(num_list)
print("smallest =", smallest)
print("largest =", largest)
