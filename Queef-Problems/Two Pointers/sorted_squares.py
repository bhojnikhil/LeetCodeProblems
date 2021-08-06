# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.
# Example 1:
# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Input: [-3, -1, 0, 1, 2]
# Output: [0, 1, 1, 4, 9]
-2,-1,0 ,2 ,3
[0,1,4,4,9]
def sorted_shit(arr):
    end = len(arr)-1
    sex = [0 for i in range(len(arr))]
    start = 0
    highest_index = end
    while start <=end:
        if arr[start]==0:
            sex[start] = 0
        if (arr[start]*arr[start]) > (arr[end]*arr[end]):
            sex[highest_index] = arr[start]*arr[start]
            start+=1
        else:
            sex[highest_index] = arr[end]*arr[end]
            end-=1    
        highest_index -= 1
    return sex


def sorted_shit2(arr):
    squares = [0 for i in range(len(arr))]
    start = 0
    end = len(arr)-1
    highest_index = end

    while start <= end:
        if abs(arr[start]) >= abs(arr[end]):
            squares[highest_index] = arr[start]*arr[start]
            start+=1
        else:
            squares[highest_index] = arr[end]*arr[end]
            end-=1
        highest_index-=1
    
    return squares
    

def sorted_squares_3(arr):
    left = 0 
    right = len(arr) - 1
    count = len(arr) - 1
    newArray = arr.copy()
    while (left <= right) : 
        if (abs(arr[left]) > abs(arr[right])) :    
            newArray[count] = arr[left]*arr[left]
            left+=1
        else:  
            newArray[count] = arr[right]*arr[right]
            right -= 1
        count-=1
    return newArray



print(sorted_squares_3([-3, -1, 1, 1, 2]))