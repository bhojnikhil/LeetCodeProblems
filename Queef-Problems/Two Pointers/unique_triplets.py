# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
# Example 1:
# Input: [-3, 0, 1, 2, -1, 1, -2]
# Sorted: [-3, -2, -1, 0, 1, 1, 2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero. 

def unique_trips_ash(arr):
    arr = sorted(arr)
    i = 0
    finalArray = []
    for i in range(len(arr)-2):
       k = len(arr)-1
       j = i + 1
       while (j<k):
           if (arr[i]+arr[j]+arr[k]==0): 
               finalArray.append([arr[i],arr[j],arr[k]])
               j+=1
               k-=1
           elif (arr[j]+arr[k]+arr[i]<0) :
               j+=1
           else:
               k-=1
    return finalArray 


def triple_sum_target(arr,target):
    arr = sorted(arr)
    i = 0
    finalArray = []
    mapper = {}
    min_target = min_sum = 99999999999999999
    
    for i in range(len(arr)-2):
       k = len(arr)-1
       j = i + 1
       while (j<k):
           if (arr[i]+arr[j]+arr[k]-target<=min_target): 
               min_target = min(min_target ,abs(arr[i]+arr[j]+arr[k]-target))
               curr_sum = arr[i]+arr[j]+arr[k]
               if  curr_sum < min_sum:
                   finalArray = [curr_sum] 
               elif curr_sum == min_sum:
                   finalArray.append(curr_sum)
               j+=1
               k-=1
           elif (-arr[i] > arr[j]+arr[k]) :
               j+=1
           else:
               k-=1
    return min(finalArray)

 

print(unique_trips_ash([-3, 0, 1, 2, -1, 1, -2]))
print(triple_sum_target([-2, 0, 1, 2],2))

    