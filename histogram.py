def ArrayChallenge(arr):
  res = 0
  stack = []
  arr.append(0)
  for i, k in enumerate(arr):
    while stack and k <=arr[stack[-1]]:
      heightBar = stack.pop()
      begin = stack[-1] + 1 if stack else 0
      end = i - 1
      dist = end - begin + 1
      res = max(res, dist * arr[heightBar])
    stack.append(i)
  return res

# keep this function call here 
print(ArrayChallenge(input()))