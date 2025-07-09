def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
"""
print(sequential_search([10,20,30,40],30))
"""
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
"""
print(binary_search([10,20,30,40],30))
"""
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
"""
print(interpolation_search([10,20,30,40],30))
"""
def linear_probing_insert(table, key, value):
    index = hash(key) % len(table)
    while table[index] is not None:
        index = (index + 1) % len(table)  # 다음 칸으로 이동
    table[index] = value

table=[None]*10

linear_probing_insert(table,10,'A')
linear_probing_insert(table,10,'B')
linear_probing_insert(table,20,'C')
linear_probing_insert(table,10,'B')
print(table)

s=set()
s.add(5)
s.add(3)
s.add(2)
print(s)



