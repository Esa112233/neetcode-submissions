# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodeList = list()

        while head:
            nodeList.append(head)
            head = head.next
        
        L, R = 0, len(nodeList) - 1

        orderedList = list()
        while L <= R:
            if L == R:
                orderedList.append(nodeList[L])
                break
            orderedList.append(nodeList[L])
            orderedList.append(nodeList[R])
            L+=1
            R-=1
        
        if len(nodeList) % 2 != 0: orderedList.append(nodeList[R])

        orderedLen = len(orderedList)
       
        for i, node in enumerate(orderedList):
            if i == orderedLen - 1:
                break
            node.next = orderedList[i+1]

        orderedList[-1].next = None



            

        