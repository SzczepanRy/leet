class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        """
        n =len(nums)
        count = 0
        for i in range(n):
            for j in range(i,n):
                if nums[i]> 2*nums[j]:
                    print(i , j)
                    count +=1

        """


        #nic nie zmieniamy w arr tylko zliczamy
        def merge(p,r):
            i = 0
            mid = (p+r)//2
            count =0
            j = mid

            for i in range(p ,mid):
                while j <r and nums[i] > 2 *nums[j] :
                    j+=1
                count += j-mid

            nums[p:r] = sorted(nums[p:r])
            return count

        def div( p,r):
            if r-p <=1:
                return 0

            mid = (p+r) //2
            count = div(p,mid)+ div(mid,r)
            count += merge( p,r )
            return count


        return div( 0 ,len(nums))





nums=[1,3,2,3,1]
s = Solution()
s.reversePairs(nums)

