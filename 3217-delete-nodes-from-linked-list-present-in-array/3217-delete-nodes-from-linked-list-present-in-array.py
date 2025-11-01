# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums) # 轉成集合以加快查找速度
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next:
            if cur.next.val in nums_set:
                cur.next = cur.next.next # 刪除節點
            else:
                cur = cur.next # 移動到下一個節點
        
        return dummy.next