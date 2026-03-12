class Solution(object):


    def recur(self, arr,result , number):
        if(len(result) >= number ):
            return;
        """
        temp2 = arr.copy()
        last = temp2.pop()
        temp2.insert(0,last)
 #       print(temp2 , result ,temp2 not in result  )
        if( temp2 not in result ):
            result.append(temp2)
            self.recur(temp2 ,result, number)
        """
        for i in range(1, len(arr) ):
            temp = arr.copy()
            last = temp.pop()
            temp.insert(len(temp)-i, last)

#        print(temp, result ,temp not in result  )
            if( temp not in result ):
                result.append(temp)
                self.recur(temp,result, number)





    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if(len(nums)< 2):
            return [nums]

        result = []
        expNum =1
        for i in range(1, len(nums)+1):
            expNum = expNum *i
        print(expNum)

        result.append(nums)
        if(len(nums) > 2):
            self.recur(nums,result, expNum)

        else:
            temp = nums.copy()
            temp.reverse()
            result.append(temp)



        print(result ,len(result))
        return(result)


s = Solution();
s.permute([1,2,3])
