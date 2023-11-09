my_list = [9, 1 ,3, 5, 4, 5, 3, 8]

def bubble_sort(list):
    stop = len(list) - 1
    for run in range(stop):
        for i in range(stop-run):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

print(bubble_sort(my_list))