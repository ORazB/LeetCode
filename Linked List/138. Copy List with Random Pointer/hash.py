"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Time Complexity: O(n)
# Space Complexity: O(n) | Can be optimized to O(1) just by changing the nodes and disconnecting the old one


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        # Hash Method
        temp = {}
        curr = head

        # Copy the Values
        while curr:
            temp[curr] = Node(curr.val)
            curr = curr.next

        # Copy the Random Pointers
        curr = head
        while curr:
            temp[curr].next = temp.get(curr.next)
            temp[curr].random = temp.get(curr.random)
            curr = curr.next
        return temp[head]
