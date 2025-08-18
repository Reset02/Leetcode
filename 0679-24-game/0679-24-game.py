class Solution:
    def value(self, n1, op, n2):
        if op == '+': return n1 + n2
        if op == '-': return n1 - n2
        if op == '*': return n1 * n2
        if op == '/':
            if abs(n2) < 1e-6:
                return 1e9
            return n1 / n2
        return 1e9

    def isValid(self, ans):
        return abs(ans - 24.0) < 1e-6

    def evaluate(self, op1, op2, op3, cards):
        # ((_ _)_)_
        ans = self.value(self.value(self.value(cards[0], op1, cards[1]), op2, cards[2]), op3, cards[3])
        if self.isValid(ans): return True

        # (_ _) (_ _)
        ans = self.value(self.value(cards[0], op1, cards[1]), op2, self.value(cards[2], op3, cards[3]))
        if self.isValid(ans): return True

        # (_(_ _))_
        ans = self.value(self.value(cards[0], op1, self.value(cards[1], op2, cards[2])), op3, cards[3])
        if self.isValid(ans): return True

        # _(_(_ _))
        ans = self.value(cards[0], op1, self.value(self.value(cards[1], op2, cards[2]), op3, cards[3]))
        if self.isValid(ans): return True

        # _(_(_ _))
        ans = self.value(cards[0], op1, self.value(cards[1], op2, self.value(cards[2], op3, cards[3])))
        if self.isValid(ans): return True

        return False

    def judgePoint24(self, cards):
        ops = ['+', '-', '*', '/']
        for perm in itertools.permutations(cards):
            for op1 in ops:
                for op2 in ops:
                    for op3 in ops:
                        if self.evaluate(op1, op2, op3, perm):
                            return True
        return False