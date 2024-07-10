class Solution {
public:
    int minOperations(vector<string>& logs) {
        int folder_depth = 0;

        // Iterate through each log operation
        for (const auto& current_operation: logs){
            // Go up one directory if "../" is encountered, but don't go above
            // the root
            if (current_operation == "../"){
                folder_depth = max(0, folder_depth - 1);
            }
            // Increase depth if the log is not 'stay in the current directory
            else if (current_operation != "./"){
                folder_depth++;
            } // Ignore "./" operations as they don't change the current folder
        }
        return folder_depth;
    }
};