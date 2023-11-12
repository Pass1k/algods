import random

def quick_sort(array):
    if len(array) > 1:
        x = array[random.randint(0, len(array)-1)]
        left = [u for u in array if u < x]
        center = [u for u in array if u == x]
        right = [u for u in array if u > x]
        array = quick_sort(left) + center + quick_sort(right)

    return array

print(quick_sort([7, 6, 10, 5, 9, 8, 4, 3]))

