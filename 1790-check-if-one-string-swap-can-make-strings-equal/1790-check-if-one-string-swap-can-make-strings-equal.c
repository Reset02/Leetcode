bool areAlmostEqual(char* s1, char* s2) {
    // 1. 如果字串已經相等，直接回傳 true
    if (strcmp(s1,s2) == 0){
        return true;
    }
    int diff_indices[2];  // 用來存儲最多兩個不同字母的位置
    int diff_count = 0;   // 記錄不同字母的數量

    // 2. 找出不同字母的位置
    for (int i = 0; i < strlen(s1); i++) {
        if (s1[i] != s2[i]) {
            if (diff_count >= 2) {
                return false;  // 超過兩個不同字母，直接返回 false
            }
            diff_indices[diff_count++] = i;
        }
    }

    // 3. 必須剛好有兩個不同的字母，並且可以互換
    return diff_count == 2 &&
           s1[diff_indices[0]] == s2[diff_indices[1]] &&
           s1[diff_indices[1]] == s2[diff_indices[0]];
}
