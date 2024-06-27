class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first_edges = edges[0]
        second_edges = edges[1]

        return first_edges[0] if first_edges[0] in second_edges else first_edges[1]