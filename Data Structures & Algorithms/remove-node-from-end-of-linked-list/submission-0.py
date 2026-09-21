# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        diff = 0
        curr = head
        dummy = head

        while curr:
            diff += 1
            curr = curr.next
        
        move = diff - n
        counter = 0
        dummy = prev = ListNode(0, head)
        curr = head

        while curr:
            if diff == n:
                prev.next = curr.next
                break
            if counter == move:
                prev.next = curr.next
                break
            counter+=1    
            prev = curr
            curr = curr.next

        return dummy.next





            

