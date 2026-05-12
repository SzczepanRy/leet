class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """

        def oper(a ,b,c):
            if "-" == b:
                return (a - c)
            if "+" == b:
                return (a + c)
            if "*" == b:
                return (a * c)

# 1. PARSOWANIE: Zamieniamy string na listę liczb (int) i znaków
        # Przykład: "11-2*3" -> [11, "-", 2, "*", 3]
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                j = i
                while j < len(expression) and expression[j].isdigit():
                    j += 1
                tokens.append(int(expression[i:j]))
                i = j
            else:
                tokens.append(expression[i])
                i += 1

        def rekur(st ):

            if len(st) == 1:
                return [st[0]]

            res = []

            for i in range(1, len(st), 2):
                char = st[i]

                if char in "+-*":

                    left = rekur(st[:i])
                    right= rekur(st[i+1:])

                    for l in left:
                        for r in right:
                            res.append(oper(l ,char , r))

            return res


        return rekur( tokens )
expression = "2*3-4*5"
s= Solution()
print(s.diffWaysToCompute(expression))
