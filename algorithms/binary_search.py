my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def binarysearch(list, item, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if item == list[mid]:
            return mid
        elif item < list[mid]:
            return binarysearch(list, item, start, mid - 1)
        else:
            return binarysearch(list, item, mid + 1, stop)

look = 20
start = 0
stop = len(my_list)

x = binarysearch(my_list, look, start, stop)

if x is False:
    print(f"The {look} wasn't found")
else:
    print(f"The index of {look} is {x}")
