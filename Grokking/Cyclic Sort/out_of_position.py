# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.
# Example 1:
# t: [4, 0, 3, 1]
# Output: 2

def place(arr):
    i=0
    n=len(arr)
    while i<n:
        j = arr[i]
        if arr[i]<n and arr[i]!=arr[j]:
            arr[i],arr[j] = arr[j], arr[i]
        else:
            i+=1

    for i in range(n):
        if arr[i]!=i:
            return i
    return n



print(place([4, 0, 3, 1]))
