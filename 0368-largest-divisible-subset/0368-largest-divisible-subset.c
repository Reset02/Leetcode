/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 // 比較函數給 qsort 用
int cmp(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int* largestDivisibleSubset(int* nums, int numsSize, int* returnSize) {
    if (numsSize == 0){
        *returnSize = 0;
        return NULL;
    }
    
    qsort(nums, numsSize, sizeof(int), cmp);

    int* dp = (int*)malloc(sizeof(int) * numsSize);
    int* prev = (int*)malloc(sizeof(int) * numsSize);
    for (int i = 0; i < numsSize; i++){
        dp[i] = 1;
        prev[i] = -1;
    }

    int max_len = 1;
    int max_idx = 0;

    for (int i = 1; i < numsSize; i++){
        for (int j = 0; j < i; j++){
            if (nums[i] % nums[j] == 0){
                if (dp[j] + 1 > dp[i]){
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
        }
        if (dp[i] > max_len){
            max_len = dp[i];
            max_idx = i;
        }
    }

    // 回溯構建答案
    *returnSize = max_len;
    int* result = (int*)malloc(sizeof(int) * max_len);
    int idx = max_len - 1;
    while (max_idx != -1){
        result[idx--] = nums[max_idx];
        max_idx = prev[max_idx];
    } 
    // 清理記憶體
    free(dp);
    free(prev);
    return result;
}