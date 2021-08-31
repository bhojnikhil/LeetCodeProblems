# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.
# Example 1:
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

def remove_dupes(arr):
    result=0
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            result+=1
        else:
            continue
    return len(arr) - result

print(remove_dupes([2, 2, 2, 11]))
