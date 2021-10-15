from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
    queue = deque()
    queue.append(root)
    result=[]
    while queue:
        lev_sum = 0.0
        currentlength=len(queue)

        for _ in range(currentlength):
            currentnode=queue.popleft()
            lev_sum+=currentnode.val
            if currentnode.left:
                queue.append(currentnode.left)
            if currentnode.right:
                queue.append(currentnode.right)
        result.append(lev_sum/currentlength)

    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()
