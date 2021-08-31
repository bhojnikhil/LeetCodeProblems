# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
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
            len_cycle= calculate_length(slow)
    cur1 = head
    cur2= head
    while len_cycle>0:
        cur2=cur2.next   
        len_cycle-=1 
    while cur1!=cur2:
        cur1 = cur1.next
        cur2=cur2.next
    return cur1
    
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
