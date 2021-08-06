# Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.
# Example 1:
# Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
# Output: 4
# Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

def remove_keys(arr, key):
    start = 0
    end = len(arr)-1
    while(start <= end):
        if arr[start] == key:
            arr[start], arr[end] = arr[end], arr[start]
            end -= 1
        else:
            start += 1
    return end + 1


def remove_keys_rev(arr, key):
    id = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[id] = arr[i]
            id += 1
    return id


print(remove_keys([3, 2, 3, 6, 3, 10, 9, 3], 3))
print(remove_keys_rev([3, 2, 3, 6, 3, 10, 9, 3], 3))
    
        