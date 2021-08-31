# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
([1,2,3,4,6],6) 
def target_pair(arr, target):
    start = 0
    end = len(arr)-1

    while end > start:
        if arr[start] + arr[end] == target:
            return [arr[start], arr[end]]
        elif arr[start] + arr[end] > target:
            end -= 1
        elif arr[start] + arr[end] < target:
            start += 1
    
    return -1

print(target_pair([1,2,3,4,6],6))
            