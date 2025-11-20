// 自訂 Sort 的比較函式
// 排序規則：end 升序、start 降序
int cmp (const void* a, const void* b){
    int *x = *(int**)a;
    int *y = *(int**)b;

    if (x[1] != y[1])
        return x[1] - y[1];  // end asc
    return y[0] - x[0]; // start desc
}
int intersectionSizeTwo(int** intervals, int intervalsSize, int* intervalsColSize) {
    qsort(intervals, intervalsSize, sizeof(int*), cmp);

    int p1 = -1; // 最大的點
    int p2 = -1; // 第二大的點
    int ans = 0; 

    for (int i = 0; i < intervalsSize; i++){
        int s = intervals[i][0];
        int e = intervals[i][1];

        // Case 1: 已經至少兩個點落在 interval
        if (p2 >= s){
            continue;
        }
        // Case 2: 目前只有 1 個點落在 interval
        if (p1 >= s){
            ans += 1;
            p2 = p1;
            p1 = e;
        }
        else{
            // Case 3: 一個點都沒有，要補兩個
            ans += 2;
            p2 = e - 1;
            p1 = e;
        }
    }

    return ans;
}