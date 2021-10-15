from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse(head):
    # TODO: Write your code here
    return head

# 1 -> 2 -> 3
  
def reverse_ashwin(head):
    # TODO: Write your code here
    cur = head
    temp_back = None
    temp_front = cur
    while temp_front != None:
        temp_front = cur.next
        cur.next = temp_back
        temp_back = cur
        cur = temp_front
    return temp_back

def reverse2(head):
    prev = None
    while head:
        curr=head
        head=head.next
        curr.next=prev
        prev=curr
    return prev

def reverse_batman(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_ashwin(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
    

def main2():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    print("Aarons shit")
    result = reverse_batman(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
    
def main3():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse2(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()
main2()
main3()