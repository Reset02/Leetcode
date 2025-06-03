class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        have_keys = set()
        visited = set()
        boxes = set(initialBoxes)
        queue = deque(initialBoxes)
        total_candies = 0

        while queue:
            size = len(queue)
            opened_this_round = False

            for _ in range(size):
                box = queue.popleft()

                if box in visited:
                    continue

                # 可以打開箱子：本身開著或擁有鑰匙
                if status[box] == 1 or box in have_keys:
                    visited.add(box)
                    total_candies += candies[box]
                    opened_this_round = True

                    # 拿鑰匙
                    for key in keys[box]:
                        if key not in have_keys:
                            have_keys.add(key)
                            # 如果鑰匙能打開某個箱子，且我們擁有這個箱子但還沒打開
                            if key in boxes and key not in visited:
                                queue.append(key)

                    # 拿子箱子
                    for new_box in containedBoxes[box]:
                        boxes.add(new_box)
                        if status[new_box] == 1 or new_box in have_keys:
                            queue.append(new_box)
                        else:
                            # 等未來有鑰匙再開
                            queue.append(new_box)
                else:
                    # 放回去之後再處理
                    queue.append(box)

            # 若這輪完全沒開新箱子，避免無限循環
            if not opened_this_round:
                break

        return total_candies