class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        # 計算 num2 的 set bits 數量
        k = bin(num2).count('1')
        
        # 初始化結果 x
        x = 0
        
        # 遍歷 num1 的每一位
        for i in range(31, -1, -1):  # 從高位到低位
            if k > 0 and (num1 & (1 << i)):  # 如果 num1 的該位是 1，且還需要 set bits
                x |= (1 << i)  # 將 x 的該位設為 1
                k -= 1  # 減少剩餘 set bits 的需求
        
        # 如果還有剩餘的 set bits
        for i in range(32):  # 從低位到高位填充剩餘的 set bits
            if k > 0 and not (x & (1 << i)):  # 如果 x 的該位是 0
                x |= (1 << i)  # 將 x 的該位設為 1
                k -= 1
        
        return x
        