# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ary = []
        cur_node = head
        while True:
            ary.append(cur_node)
            if cur_node.next is None: break
            cur_node = cur_node.next
        list_len = len(ary)
        if list_len - n == 0:
            return head.next
        else:
            ary[list_len - n - 1].next = ary[list_len - n].next
            return head