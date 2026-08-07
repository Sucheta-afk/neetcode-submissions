# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        len_nums=0
        #computing lenght of LL
        while curr.next!=None:
            curr=curr.next
            len_nums+=1
        len_nums+=2
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        rang=len_nums-n
        rang=rang-1
        for i in range(rang):
            curr=curr.next
            prev=prev.next
        

        #code to delete node
        print("deleting...")
        nxt=curr.next
        curr=curr.next
        prev.next=nxt

        return dummy.next
            
            