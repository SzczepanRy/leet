class Solution(object):

    def strToInt(self,s):
        d = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            }
        sArr = list(s)

        result = 0
        index = 1
        while len(sArr) > 0 :
            dVal = sArr.pop()
            result += index * d[dVal]

            index = index*10

        return result

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = self.strToInt(num1)*self.strToInt(num2)
        return str(res)


s = Solution()
s.multiply("123","456")
