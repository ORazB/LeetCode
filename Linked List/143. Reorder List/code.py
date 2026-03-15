# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head
        
        # fast & slow pointer
        # use "slow" to find the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # save second half and cut the link
        second = slow.next
        slow.next = None
        
        # Reverse the second so from 4-5 to 5-4 because we want the result to be ex.1-5,2-4
        prev = None
        curr = second
        while curr:
            # save the next node
            temp = curr.next
            # point curr.next to prev
            curr.next = prev
            # update prev to be changed curr
            prev = curr
            # update curr to be the saved next node
            curr = temp
            
        # Re order
        first = head
        second = prev
        
        while second:
            # Save the first and second half next
            temp1 = first.next
            temp2 = second.next
            
            # Change first's next to second
            first.next = second
            # Change second's next to temp1
            second.next = temp1
            
            # Advance first
            first = temp1
            # Advance second
            second = temp2