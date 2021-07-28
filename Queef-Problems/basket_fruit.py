# Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
# You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both baskets.
# Example 1:
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

def fruits_into_baskets(fruits):
    left = 0 
    right = 0
    mapper = {}
    answer = 0
    for right in range(len(fruits)): 
        if fruits[right] not in mapper.keys(): 
            mapper[fruits[right]] = 1 
        else : 
            mapper[fruits[right]]+=1 
        while len(mapper.keys()) > 2 :
            mapper[fruits[left]]-=1
            if mapper[fruits[left]] == 0 :
                   del mapper[fruits[left]]
            left+=1
        answer = max(answer, right - left + 1)
    return answer


print(fruits_into_baskets([3,3,3,1,2,1,1,2,3,3,4]))