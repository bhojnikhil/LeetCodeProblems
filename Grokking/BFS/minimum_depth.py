from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  if root is None:
    return 0

  queue = deque()
  queue.append(root)
  minimumTreeDepth = 0
  while queue:
    minimumTreeDepth+=1
    levelsize=len(queue)
    for _ in range(levelsize):
        currrentnode=queue.popleft()
        if not currrentnode.left and not currrentnode.right:
            return minimumTreeDepth
        if currrentnode.left:
            queue.append(currrentnode.left)
        if currrentnode.right:
            queue.append(currrentnode.right)
            


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
