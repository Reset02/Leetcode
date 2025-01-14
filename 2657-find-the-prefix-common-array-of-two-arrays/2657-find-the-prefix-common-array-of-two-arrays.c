/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findThePrefixCommonArray(int* A, int ASize, int* B, int BSize, int* returnSize) {
    // 分配結果陣列的記憶體
    
    int* prefixCommonArray = (int*)malloc(ASize * sizeof(int));
    int* frequency = (int*)calloc(ASize + 1, sizeof(int)); // 初始化為 0
    int commonCount = 0;

    *returnSize = ASize; // 設定結果陣列大小

    // 遍歷 A 和 B 的每個索引
    for (int currentIndex = 0; currentIndex < ASize; currentIndex++){
        // 更新 A[currentIndex] 的出現次數，並檢查是否已經出現過
        if (++frequency[A[currentIndex]] == 2){
            commonCount++;
        }
        // 更新 B[currentIndex] 的出現次數，並檢查是否已經出現過
        if (++frequency[B[currentIndex]] == 2){
            commonCount++;
        }
        // 存儲當前前綴的共同元素數量
        prefixCommonArray[currentIndex] = commonCount;
    }
    // 釋放 frequency 陣列的記憶體
    free(frequency);
    return prefixCommonArray;
}