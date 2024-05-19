class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head_ref, new_data):
        # Create a new node
        new_node = Node(new_data)
        # Store the head reference in a temporary variable
        last = head_ref
        # Set the next pointer of the new node as None since it will be the last node
        new_node.next = None
        # If the Linked List is empty, make the new node as the head and return
        if head_ref is None:
            return new_node
        # Else traverse till the last node
        while last.next is not None:
            last = last.next
        # Change the next pointer of the last node to point to the new node
        last.next = new_node
        return head_ref


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)