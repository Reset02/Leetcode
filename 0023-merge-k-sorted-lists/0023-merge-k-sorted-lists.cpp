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
struct Compare {
    bool operator()(ListNode* a, ListNode* b) {
        return a->val > b->val;  // 小根堆：值小的優先
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, Compare> pq;
        
        // 初始化：將每條 linked list 的頭節點加入 heap
        for (ListNode* node: lists){
            if (node) pq.push(node);
        }

        ListNode dummy(0);
        ListNode* tail = &dummy;

        while(!pq.empty()){
            ListNode* curr = pq.top();
            pq.pop();

            tail->next = curr;
            tail = tail->next;

            if (curr->next) pq.push(curr->next);   
        }
        return dummy.next;
    }
};