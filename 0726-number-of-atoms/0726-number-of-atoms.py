class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # 為每個索引儲存有效的乘數
        muls = [] # 一個列表，用於儲存每個索引位置對應的有效乘數。
        running_mul = 1

        # 用堆疊來處理嵌套的化學式
        stack = [1]

        # 預處理化學式並提取所有乘數
        index = len(formula) - 1
        curr_number = ""
        while index >= 0:
            if formula[index].isdigit(): # 當遇到數字時，累加到curr_number。
                curr_number += formula[index]

            elif formula[index].isalpha(): # 當遇到字母時，將curr_number清空（因為這個數字是原子的數量，不是乘數）
                curr_number = ""

            elif formula[index] == ")": # 當遇到右括號)時，表示這裡有一個嵌套的乘數，將這個乘數乘到running_mul上並儲存到stack中。
                curr_multiplier = int(curr_number[::-1]) if curr_number else 1
                running_mul *= curr_multiplier
                stack.append(curr_multiplier)
                curr_number = ""

            elif formula[index] == "(": # 當遇到左括號(時，表示一個嵌套結束，從stack中取出最近的乘數，並將running_mul除以這個乘數。
                running_mul //= stack.pop()
                curr_number = ""

            muls.append(running_mul) # 每個索引位置的有效乘數儲存在muls中。
            index -= 1

        # 反轉muls # 最後反轉muls列表，因為掃描是從右到左進行的，而我們需要從左到右的順序。
        muls = muls[::-1]

        # 儲存元素數量的字典
        final_map = defaultdict(int)

        # 從左到右遍歷化學式
        index = 0
        while index < len(formula):
            if formula[index].isupper(): # 當遇到大寫字母時，開始提取整個原子名稱，可能包括後續的小寫字母
                curr_atom = formula[index]
                curr_count = ""
                index += 1
                while index < len(formula) and formula[index].islower():
                    curr_atom += formula[index]
                    index += 1

                while index < len(formula) and formula[index].isdigit():
                    curr_count += formula[index]
                    index += 1

                if curr_count:
                    final_map[curr_atom] += int(curr_count) * muls[index - 1]
                else:
                    final_map[curr_atom] += 1 * muls[index - 1]
            else:
                index += 1
        
        # 將final_map排序
        final_map = dict(sorted(final_map.items()))

        # 生成結果字串
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans

        