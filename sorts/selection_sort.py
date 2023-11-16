# Временная сложность (в худшем, среднем и лучшем случае) 
# алгоритма сортировки выбором составляет O(n^2)

array = [9, 7, 4, 1, -1, -2, 3]

lens = len(array)

for i in range(lens - 1):
    m = array[i]
    p = i
    for j in range(i+1, lens):
        if m > array[j]:
            m = array[j]
            p = j
        
    if p != i:
        t = array[i]
        array[i] = array[p]
        array[p] = t

print(array)