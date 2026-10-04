# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        grp_prev=dummy
        while True:
            kth=grp_prev
            for i in range(k):
                kth=kth.next
                if not kth:
                    return dummy.next
            grp_next=kth.next
            prev=grp_next
            curr=grp_prev.next
            while curr!=grp_next:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=grp_prev.next
            grp_prev.next=kth
            grp_prev=temp



        