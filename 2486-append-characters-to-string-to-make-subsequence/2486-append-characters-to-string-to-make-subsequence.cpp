class Solution {
public:
    int appendCharacters(string s, string t) {
        int first = 0, longest_prefix = 0;

        while (first < s.length() && longest_prefix < t.length()){
            if (s[first] == t[longest_prefix]){
                longest_prefix++;
            }
            first++;
        }
        return t.length() - longest_prefix;
    }
};