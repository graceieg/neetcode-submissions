# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Could create a dictionary that stores index and value
        #Visited []
        #Cycle if node.next is in visited set
        #Could create a dictionary that stores index and value

        curr = head
        visited = set()
        count = 0
        while curr: 
            if curr.next in visited:
                return True
            else:
                visited.add(curr)
            curr = curr.next
        return False
        

        