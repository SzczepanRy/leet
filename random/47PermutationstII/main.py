class Solution:



    def numOfRes(self , arr):
        num = len(arr)

        unique=[]
        for i in arr:
            if not i in unique:
                unique.append(i)

        res = 1
        for i in range(len(unique)-1):
            res *= num
            num = num -1


        return res

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num= self.numOfRes(nums);

        print(num)

        mapa = {}

        self.recur(nums,mapa,num)



    def recur(self, nums , mapa,num):
        if(len(mapa)  >= num):return

        for i in range(1, len(nums)):
            nums[0] , nums[i] = nums[i] , nums[0]
            temp= nums.copy()
            result = int("".join(map(str, temp)))
            mapa[result] = temp
            self.recur(temp,mapa , num )



Solution().permuteUnique([1,2,3,4,5])
