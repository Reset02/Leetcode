# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        # 初始化：把每個 linked list 的第一個節點加入 heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node)) # (值, 編號, 節點)
        
        dummy = ListNode(0)
        tail = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next