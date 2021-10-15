from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    prev=cur=None
    while queue:
        prev=cur 
        for _ in range(len(queue)):
            cur=queue.popleft()
            if prev:
                prev.next=cur
            prev=cur
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
    return        

    return


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()
