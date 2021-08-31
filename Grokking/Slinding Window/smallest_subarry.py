# smallest contiguous subarray whose sum is greater than or equal to ‘S’
# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2]

# arr=[2, 1, 5, 2, 3, 2]
# s=7
# N = len(arr)


def smallest_subarray_with_given_sum(s, arr):
    shortestLen = 999
    currentLen = 0
    windowStart = 0
    window_sum = 0
    for windowend in range(0,len(arr)):
        window_sum += arr[windowend]
        print("Window SUm",window_sum)
        print("Window End",windowend)
        while window_sum >= s:
            shortestLen = min(shortestLen, windowend - windowStart + 1)
            window_sum -= arr[windowStart]
            windowStart += 1    
    return  shortestLen


def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
#   print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
#   print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
