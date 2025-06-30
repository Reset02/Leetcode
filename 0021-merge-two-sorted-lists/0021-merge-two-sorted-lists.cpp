/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy(0);// 建立虛擬頭節點
        ListNode* tail = &dummy; // 尾指標指向 dummy

        while(list1 && list2){
            if (list1->val < list2->val){
                tail->next = list1;
                list1 = list1->next;
        } else{
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }

    // 接上剩餘節點
    tail->next = list1 ? list1: list2;
    return dummy.next; // 回傳虛擬頭節點的下一個節點，也就是合併後串列的頭
    }
};
