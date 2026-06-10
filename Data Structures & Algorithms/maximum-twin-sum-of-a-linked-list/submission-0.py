# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        sums = []
        prev = None
        #Split the list, point at the end of first half and start of second. compare and store in an array. return the max of the array

        while fast.next.next: 
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        #Reverse selcond half
        second = slow.next
        while second: 
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        while prev and head: 
            sums.append((prev.val + head.val))
            prev = prev.next
            head = head.next
        return max(sums)
            