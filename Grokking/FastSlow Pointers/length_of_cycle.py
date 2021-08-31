# Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def find_cycle_length(head):
    slow,fast = head,head
    while fast is not None and fast.next is not None:
        fast=fast.next.next
        slow=slow.next
        if slow == fast:
            return calculate_length(slow)
    return 

def calculate_length(slow):
    len = 0
    cur = slow
    while True:
        len +=1
        cur = cur.next
        if cur == slow:
            break
    return len

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()
