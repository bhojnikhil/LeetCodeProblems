# Problem Statement #
# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of 
# the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.
# The flag of the Netherlands consists of three colors: red, white and blue; and since our input array 
# also consists of three different numbers that is why it is called Dutch National Flag problem.
# Example 1:
# Input: [1, 0, 2, 1, 0]
# Output: [0 0 1 1 2]


def dutch_flag_1(arr):
    end = len(arr) - 1
    start = 0
    while start < end:
        if arr[start] == 2:
            # swap
            print("first", start, end, arr[start], arr[end])
            arr[end], arr[start] = arr[start], arr[end]
            end -= 1
        else:
            start += 1
        

    start = 0
    while start < end:
        if arr[start] == 1:
            # swap
            print("second", start, end, arr[start], arr[end]) 
            arr[end], arr[start] = arr[start], arr[end]
            end -= 1
        else:
            start += 1
        

    return arr
print(dutch_flag_1([2, 2, 0, 1, 2, 0]))

def dutch_flag_bestest_solution(arr):
    left = 0
    count_zero = 0
    count_one = 0 
    count_two = 0 

    right = len(arr)-1

    for ele in arr:
        if ele == 0 : 
            count_zero +=1
        elif ele == 1 : 
            count_one +=1
        else: 
            count_two +=1
     
    #pass_1
    while left < count_zero :
        if arr[left]==0:
              left+=1
        if arr[right]==0: 
              arr[left], arr[right] = arr[right], arr[left]
              left+=1

    #pass 2
    right = len(arr) - 1 
    while left < count_zero+count_one :
        if arr[left]==1:
               left+=1
        if arr[right] == 1:
               arr[left], arr[right] = arr[right], arr[left]
    return arr 
    
print("aaswins crap")
print(dutch_flag_bestest_solution([2, 2, 0, 1, 2, 0]))

    