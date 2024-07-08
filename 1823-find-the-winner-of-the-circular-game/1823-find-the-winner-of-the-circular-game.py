class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Initialize deque with n friends
        circle = deque(range(1, n + 1))

        # Perform eliminations while more than 1 player remains
        while len(circle) > 1:
            # Process the first k-1 friends without eliminating them
            for _ in range(k - 1):
                # 這個 for 迴圈將前 k-1 個人從隊列的前端移到後端，模擬這些人繞過一圈回到隊列的末尾。popleft() 用來從隊列前端移除元素，append() 用來在隊列末端添加元素。
                circle.append(circle.popleft())
            # Eliminate the k-th friend
            circle.popleft()
        return circle[0]
        