#define MAX_LEN 1001  // \U0001f7e2 定義 MAX_LEN 放在最上面
// 初始化並查集
int parent[26];

// Find：尋找代表元素，並做 path compression
int find(int x) {
    if (parent[x] != x) {
        parent[x] = find(parent[x]);
    }
    return parent[x];
}

// Union：合併兩個集合，讓字典序小的成為代表
void unionSet(int x, int y) {
    int px = find(x);
    int py = find(y);
    if (px == py) return;
    if (px < py) {
        parent[py] = px;
    } else {
        parent[px] = py;
    }
}

// 主函式
char* smallestEquivalentString(char* s1, char* s2, char* baseStr) {
    // 初始化 parent 陣列
    for (int i = 0; i < 26; ++i) {
        parent[i] = i;
    }

    int len = strlen(s1);
    for (int i = 0; i < len; ++i) {
        unionSet(s1[i] - 'a', s2[i] - 'a');
    }

    static char result[MAX_LEN];
    int baseLen = strlen(baseStr);

    for (int i = 0; i < baseLen; ++i) {
        int rep = find(baseStr[i] - 'a');
        result[i] = rep + 'a';
    }
    result[baseLen] = '\0'; // 結尾補上 null 字元

    return result;
}
