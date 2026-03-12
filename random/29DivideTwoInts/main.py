class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if(divident == -1 and divisor == 1):
            return -1
        floatVal = dividend/divisor
        intVal = dividend//divisor
        if(floatVal < 0 and intVal < 0):
            if( intVal < floatVal):
                return intVal +1
            return intVal

        return intVal

s =Solution()

print(s.divide(7,-3))
