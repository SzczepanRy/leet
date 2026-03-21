class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """


        #find unique


        """
        nie potymalne

        A = nums
        k = k-1
        r = len(nums)-1

        p = 0

        while r -p >0:


            fi , li , mi = p , r , (p+r)//2
            f , l , mid = A[fi] , A[li] , A[mi]

            pi = -1

            if (f<= mid<= l) or(l<= mid<= f):
                pi = mi
            elif (f<= l <= mid) or(mid<= l<= f):
                pi = li
            else:
                pi = fi

            x = A[pi]
            A[pi] , A[r] =  A[r] ,A[pi]

            i = p-1
            for j in range(p,r):
                if A[j] >= x:
                    i+=1
                    if i!= j:
                        A[i] , A[j] =  A[j] , A[i]

            A[i+1] , A[r] =  A[r] , A[i+1]

            q = i+1

            if q == k:
                print(k)
                return A[k]

            elif q > k :
                r = q -1
            else:
                p = q+1

        return A[p]

        """

        target = k - 1
        p, r = 0, len(nums) - 1

        while p <= r:
            if p == r:
                return nums[p]

            # 1. Wybór pivota (Median-of-three)
            mid = (p + r) // 2
            # Sortujemy skrajne punkty, by wybrać medianę
            if nums[p] > nums[mid]: nums[p], nums[mid] = nums[mid], nums[p]
            if nums[p] > nums[r]: nums[p], nums[r] = nums[r], nums[p]
            if nums[mid] > nums[r]: nums[mid], nums[r] = nums[r], nums[mid]

            pivot = nums[mid]

            # 2. Partycja Hoare'a (Dwa wskaźniki zbieżne)
            i = p - 1
            j = r + 1

            while True:
                # Szukamy elementu po lewej, który powinien być po prawej
                while True:
                    i += 1
                    if nums[i] <= pivot: break # Dla k-max (malejąco) zmieniamy znak

                # Szukamy elementu po prawej, który powinien być po lewej
                while True:
                    j -= 1
                    if nums[j] >= pivot: break

                if i >= j:
                    break

                # Zamiana "niepasujących" elementów
                nums[i], nums[j] = nums[j], nums[i]

            # 3. Logika Quickselect dla partycji Hoare'a
            # Uwaga: Hoare zwraca punkt podziału 'j', a nie stałą pozycję pivota
            if target <= j:
                r = j
            else:
                p = j + 1

        return nums[target]








nums = [3,2,1,5,6,4]
k = 2

s = Solution()
print(s.findKthLargest(nums,k))
