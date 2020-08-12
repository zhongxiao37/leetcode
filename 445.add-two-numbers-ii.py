# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_lst, l2_lst = [], []
        while l1:
            l1_lst.append(l1.val)
            l1 = l1.next
        while l2:
            l2_lst.append(l2.val)
            l2 = l2.next
        l = 0
        ans = None
        while l1_lst or l2_lst or l > 0:
            m = l1_lst.pop() if len(l1_lst) > 0 else 0
            n = l2_lst.pop() if len(l2_lst) > 0 else 0
            cur = (m + n + l)
            k = cur % 10
            l = cur // 10
            curnode = ListNode(k)
            curnode.next = ans
            ans = curnode 
            
        return ans

    
    

l1 = None
l2 = None
for i in reversed([5]):
    t = ListNode(i)
    t.next = l1
    l1 = t

for i in reversed([5]):
    t = ListNode(i)
    t.next = l2
    l2 = t


print(Solution().addTwoNumbers(l1, l2))