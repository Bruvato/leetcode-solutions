# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 == None:
        #     return list2
        # elif list2 == None:
        #     return list1
        

        # if list1.val <= list2.val:
        #     return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        # else:
        #     return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))

        

        head = ListNode()
        curr = head

        while True:
            if not list1:
                curr.next = list2
                break
            elif not list2:
                curr.next = list1
                break
            
            if list1.val <= list2.val:
                curr.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val, None)
                list2 = list2.next
            
            curr = curr.next
        
        return head.next
