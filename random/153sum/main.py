class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if( len(nums) <3):
            return[]
        s ={}
        cleanArr = []

        for i in range(len(nums)):
            try:
                if(s[nums[i]]<3):
                    cleanArr.append(nums[i])
                    s[nums[i]]+=1
            except:
                s[nums[i]]=1
                cleanArr.append(nums[i])

#        print(len(nums))
        nums= cleanArr
#        print(len(nums))
        obj= {}
        index = 0
        for i in range(len(nums)):
            first = nums[i]
            for j in range(i+1, len(nums)  ):
                second = nums[j]
                for a in range(j+1, len(nums) ):
                    third = nums[a]
                    if( (first + second + third) == 0):
                        add = 0
                        rra= [first,second,third]
                        rra.sort()
                        for b in obj:
                            if(obj[b] == rra):
        #                        print("hit " , obj[b])
                                add+=1
                        if(add ==0 ):
                            obj[len(obj)] = rra

        print(obj)
        result=[]
        if len(obj) == 0:
            return result
        for i in obj:
            result.append(obj[i])

        return result


s = Solution()
s.threeSum([-1,0,1,2,-1,-4])

