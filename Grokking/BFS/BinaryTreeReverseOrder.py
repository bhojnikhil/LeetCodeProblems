from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):

    queue = deque()
    queue.append(root)
    result=deque()
    while queue:
        currentlevel=[]
        currentlength=len(queue)

        for _ in range(currentlength):
            currentnode=queue.popleft()
            currentlevel.append(currentnode.val)
            if currentnode.left:
                queue.append(currentnode.left)
            if currentnode.right:
                queue.append(currentnode.right)
        result.appendleft(currentlevel)

    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
