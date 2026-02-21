# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# New Topic: Linked List
# What is Linked List?
# A linked list is a linear data structure where each element is a separate object.
# Each element (node) contains two parts: data and a reference (pointer) to the next node in the sequence.
# The last node points to None, indicating the end of the list.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
      # Initialize prev as None for holding the reversed list
      prev = None
      
      # How does this work?
      while head:
        # Store the next node in a temporary variable
        temp = head.next
        
        # Reverse the link by pointing the current node's next to the previous node
        head.next = prev
        
        # Move prev and head pointers one step forward
        prev = head
        
        # Move head pointer one step forward
        head = temp
      return prev