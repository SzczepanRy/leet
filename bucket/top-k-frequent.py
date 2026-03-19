
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if len(nums) <2:
            return [len(nums)]
        # buckets , as a length

        #size,count
        n = len(nums)
        B =[0]*n

        used = []

        for num in nums:
            if num not in used :
                used.append(num)


        C = [0]* len(used)

        for num in nums:
            C[used[]]






        #countsort




        """
        for num in nums:
            if num not in used :
                buckets.append([num,0])
                used.append(num)



            target_idx = -1
            for idx, pair in enumerate(buckets):
                if pair[0] == num:

                    target_idx = idx
                    break

            curr_pair = buckets.pop(target_idx) # This is cleaner than slicing
            curr_pair[1] += 1


            left = 0
            right = len(buckets)


            while left < right:
                mid = (left + right) //2
                if buckets[mid][1] < curr_pair[1]:
                    left= mid +1
                else:
                    right = mid

            buckets.insert(left, curr_pair)



        """

        result = []

        for i in range(k):
            result.append(buckets[len(buckets)-1-i][0])

        print(result)

        return result




nums = [1,2,1,2,1,2,3,1,3,2]
k = 2

s =Solution()
s.topKFrequent(nums, k)
