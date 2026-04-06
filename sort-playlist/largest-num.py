class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """


        if len(nums) == 1:
            return str(nums[0])


        n = len(nums)
        s_nums = [str(x) for x in nums]

        def merge(arr , B, p, q , r):

            i = p
            j = q
            k= p
            while i < q and j < r:
                if arr[j] + arr[i] <= arr[i] + arr[j]:
                    B[k] = arr[i]
                    k+=1
                    i+=1
                else:
                    B[k] = arr[j]
                    k+=1
                    j+=1

            while i < q:
                B[k] = arr[i]
                k+=1
                i+=1

            while j < r:
                B[k] = arr[j]
                k+=1
                j+=1


            arr[p:r] = B[p:r]

        def msor(arr , B , p , r):
            if r-p <=1:
                return

            mid = (p+r)//2
            msor(arr, B , p , mid)
            msor(arr, B , mid , r)
            merge(arr ,B , p , mid , r)




        B=["0"] *(len(s_nums))
        msor(s_nums , B , 0 , len(s_nums))


        result = "".join(B)

        if result[0] == "0":
            return "0"

        return result




nums = [3,30,34,5,9]
s = Solution()
s.largestNumber(nums)
