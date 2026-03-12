class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        envelopes[i] = [wi, hi]
        """



        def merge(l,r):

            result=[]
            i=j=0

            while i<len(l) and j<len(r):

                if l[i][0] > r[j][0]:
                    result.append(r[j])
                    j+=1
                elif l[i][0] < r[j][0]:
                    result.append(l[i])
                    i += 1
                # 2. Widths are EQUAL! Tie-breaker: sort by height DESCENDING
                else:
                    if l[i][1] > r[j][1]:
                        result.append(l[i])
                        i += 1
                    else:
                        result.append(r[j])
                        j += 1
            result.extend(l[i:])
            result.extend(r[j:])
            return result

        def mergeSort(arr):
            if len(arr)<=1:
                return arr

            n= len(arr)

            mid = n //2

            l =arr[:mid]
            r=arr[mid:]
            leftS = mergeSort(l)
            rightS= mergeSort(r)

            return merge(leftS, rightS)



        print(envelopes)
        envelopes=mergeSort(envelopes)
        print(envelopes)


        n = len(envelopes)
        dp =[1]*n

        """
        moje za wolne
        for i in range(1,n):
            for j in range(i):

                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i]= max(dp[i] ,dp[j]+1 )

        print(dp)

        print(max(dp))
        return max(dp)
        """

        def binary_search(tails, target):
            low = 0
            high = len(tails) - 1
            while low <= high:
                mid = (low + high) // 2
                if tails[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        # 1. Sortujemy koperty
        envelopes = mergeSort(envelopes)

        # 2. Algorytm LIS z ręcznym wyszukiwaniem binarnym
        tails = []
        for _, h in envelopes:
            # Szukamy miejsca dla wysokości h w tablicy tails
            idx = binary_search(tails, h)

            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h

        return len(tails)

envelopes = [[5,4],[6,4],[6,7],[2,3]]
s=Solution()
s.maxEnvelopes(envelopes)
