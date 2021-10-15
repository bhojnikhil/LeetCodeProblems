from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root,key):
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    minimumTreeDepth = 0
    while queue:

        levelsize=len(queue)
        for _ in range(levelsize):
            currrentnode=queue.popleft()
            if currrentnode.left:
                queue.append(currrentnode.left)
            if currrentnode.right:
                queue.append(currrentnode.right)
            if currrentnode.val==key:
                return queue[0]
    return None

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)


main()
