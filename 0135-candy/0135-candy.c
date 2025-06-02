// 計算最少需要多少糖果
int candy(int* ratings, int ratingsSize) {
    if (ratingsSize == 0) return 0;

    // 動態配置一個陣列來記錄每個孩子的糖果數，初始化為 1
    int* candies = (int*)malloc(sizeof(int) * ratingsSize);
    for (int i = 0; i < ratingsSize; i++) {
        candies[i] = 1;
    }

    // 從左到右掃描
    for (int i = 1; i < ratingsSize; i++) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        }
    }

    // 從右到左掃描
    for (int i = ratingsSize - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1]) {
            if (candies[i] < candies[i + 1] + 1) {
                candies[i] = candies[i + 1] + 1;
            }
        }
    }

    // 計算總和
    int total = 0;
    for (int i = 0; i < ratingsSize; i++) {
        total += candies[i];
    }

    free(candies);  // 記得釋放記憶體
    return total;
}