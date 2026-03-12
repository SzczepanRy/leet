class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """

        def merge(l, r):
            res =[]
            i=j=0
            while i < len(l) and j< len(r):
                if l[i][0] < r[j][0]:
                    res.append(l[i])
                    i+=1
                else:
                    res.append(r[j])
                    j+=1

            res.extend(l[i:])
            res.extend(r[j:])
            return res


        def sor(arr):
            n = len(arr)
            if n <= 1:
                return arr
            mi= n//2
            r = arr[mi:]
            l = arr[:mi]

            sr= sor(r)
            sl= sor(l)

            return merge(sl,sr)



        pairs = sor(pairs)
        print(pairs)

        n = len(pairs)
        dp1 = [1] *n


        for i in range(1,n):
            for j in range(i):
                if pairs[i][0] >pairs[j][0] and pairs[i][0] >pairs[j][1]:
                    dp1[i] = max(dp1[i], dp1[j] + 1)

        print(dp1)
        return max(dp1)

pairs1 = [[1,2],[7,8],[4,5]]
pairs = [[1,2],[2,3],[2,3],[3,4]]
s = Solution()
s.findLongestChain(pairs)
