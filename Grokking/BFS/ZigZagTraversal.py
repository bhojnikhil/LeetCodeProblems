from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):

    queue = deque()
    queue.append(root)
    result=[]
    reverse_order=True
    while queue:
        currentlevel=deque()
        currentlength=len(queue)

        for _ in range(currentlength):
            currentnode=queue.popleft()
            if reverse_order:
                currentlevel.append(currentnode.val)
            else:
                currentlevel.appendleft(currentnode.val)
            if currentnode.left:
                queue.append(currentnode.left)
            if currentnode.right:
                queue.append(currentnode.right)
        result.append(list(currentlevel))
        reverse_order = not reverse_order
    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))

main()
