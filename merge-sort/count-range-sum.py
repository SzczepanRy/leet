#tablica , z summami , merge , s(i,j) = p[j] - p[i-1]
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """


        # part sum is a o(n) operation
        """

        n = len(nums)
        sums = [0]*n
        sums[0] =nums[0]

        for i in range(1,n):
            sums[i]= sums[i-1]+nums[i]

        result = 0
        for i in range(n):
            for j in range(n-i):
                if i+j == i:
                    if sums[i]>= lower and sums[i] <= upper:
                        result+=1
                else:
                    delta = sums[i+j] - sums[i]
                    if delta>= lower and delta <= upper:
                        result+=1

        print(result)
        return result
        """

        n = len(nums)
        #addind zero by pojedyńcze liczby wyłu ok , bo 2+0 =2
        sums = [0]

        for i in range(n):
            sums.append(sums[-1]+nums[i])

        def mergeSums( p,r) :

            if r-p <=1:
                return 0

            mid = (p+r)//2

            count = mergeSums(p,mid) + mergeSums(mid,r)

            j = k = mid

            for i in range(p,mid):

                # szumkamu , największą wartość < od lower  i  infinum k
                while j < r and sums[j]- sums[i] < lower:
                    j+=1

                while k < r  and sums[k]- sums[i] <=upper:
                    k+=1


                count += (k-j)



            merged = []
            left_idx, right_idx = p, mid

            while left_idx < mid and right_idx < r:
                if sums[left_idx] <= sums[right_idx]:
                    merged.append(sums[left_idx])
                    left_idx += 1
                else:
                    merged.append(sums[right_idx])
                    right_idx += 1

            # Dodanie reszty elementów, które zostały
            merged.extend(sums[left_idx:mid])
            merged.extend(sums[right_idx:r])

            # Podmiana w oryginalnej tablicy
            sums[p:r] = merged

            return count





        res = mergeSums(0, len(sums))
        return res










nums = [-2,5,-1]
lower = -2
upper = 2

s = Solution()
s.countRangeSum(nums , lower, upper)
