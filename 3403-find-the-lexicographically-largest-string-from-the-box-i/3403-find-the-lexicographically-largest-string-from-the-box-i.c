char *lastSubstring(char *s) {
    int i = 0, j = 1, n = strlen(s);
    while (j < n) {
        int k = 0;
        while (j + k < n && s[i + k] == s[j + k]) {
            k++;
        }
        if (j + k < n && s[i + k] < s[j + k]) {
            int t = i;
            i = j;
            j = fmax(j + 1, t + k + 1);
        } else {
            j = j + k + 1;
        }
    }
    return s + i;
}

char *answerString(char *word, int numFriends) {
    if (numFriends == 1) {
        return word;
    }
    char *last = lastSubstring(word);
    int n = strlen(word);
    int m = strlen(last);
    int len = fmin(m, n - numFriends + 1);
    last[len] = '\0';
    return last;
}