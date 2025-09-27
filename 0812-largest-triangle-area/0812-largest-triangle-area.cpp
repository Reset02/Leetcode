class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        int n = points.size();
        double max_area = 0.0;

        // 三層迴圈取所有點的組合
        for (int i = 0; i < n; i++){
            for (int j = i + 1; j < n; j++){
                for (int k = j + 1; k < n; k++){
                    double area = triangleArea(points[i], points[j], points[k]);
                    max_area = max(max_area, area);
                }
            }
        }
        return max_area;
    }

private:
    // 計算三角形面積 (Shoelace formula)
    double triangleArea(vector<int>& p1, vector<int>& p2, vector<int>& p3){
        return fabs(
            p1[0] * (p2[1] - p3[1]) +
            p2[0] * (p3[1] - p1[1]) +
            p3[0] * (p1[1] - p2[1])
        ) / 2.0;
    }
};