from bisect import bisect_left, bisect_right


arr = [11, 12, 13, 14, 15, 17, 18, 19, 20]

print(bisect_left(arr, 16))  # 5
print(bisect_right(arr, 16))  # 5

print(bisect_left(arr, 15))  # 4
print(bisect_right(arr, 15))  # 5


people = [
    ("Sam", 12),
    ("David", 15),
    ("John", 20),
    ("Mike", 25),
    ("Tom", 30),
    ("Alice", 35),
    ("Bob", 40),
    ("Cathy", 45),
    ("Eve", 50),
    ("Frank", 55),
]

# print(bisect_left(people, 25, key=lambda x: x[1]))  # 3


def binary_search(arr, target):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def binary_search_lower_bound(arr, target):
    lo = 0
    hi = len(arr) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    return lo


print(binary_search_lower_bound(arr, 15))
print(binary_search_lower_bound(arr, 16))
print(binary_search_lower_bound(arr, 17))
