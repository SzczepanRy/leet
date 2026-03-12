class Solution(object):

    def sumArr(arr):
        sum = 0
        for i in arr:
            sum += i
        return sum


    def threeSumClosest(self, nums , target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       # gap = len(nums) //4
       # if(len(nums) < 25):
            #normal fors
        minVal = 999999
        sum = 0
        for i in range(len(nums)):
            for j in range(i+1 ,len(nums)):
                for k in range(j+1,len(nums)):
                    su = nums[i] + nums[j] + nums[k]

                    if(su< 0 and target> 0 ):
                        su-=1
                    if(su == target):
                        print("found exact match", target)
                        return target

                    ddsu = abs(su)

                    leng = 0
                    if target > su :

                        leng = (( (target - su )**2)**(1/2)).real
                    else:

                        leng = (( ( su -target )**2)**(1/2)).real

                    print(i,j,k ,su,target, leng)
                    if(leng < minVal ):
                            minVal = leng
                            sum = su




        print(minVal , sum)

        return sum





s = Solution()
s.threeSumClosest([1,1,1,0],-100 )
    # check left

