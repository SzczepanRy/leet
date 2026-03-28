class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        """
        mój kod bez setów nie przechodzi
        res=0

        ## minimize by deleting , duplicates ?

        ## minimalizuje permutacje
        def binSearch(arr,val):
            if len(arr) == 0 :
                arr.append(val)
                return True

            l = 0
            r = len(arr)-1

            while l<= r:
                mid = (r+l)//2

                if arr[mid] <= val:
                    if arr[mid] == val:
                        return False

                    l = mid+1
                else:
                    r = mid-1


            arr.insert(l , val)
            return True


        xt = []

        for iii in range(len(nums1)):
            x = nums1[iii]

            yt = []

            if not binSearch(xt, x):
                continue

            for ii in range(iii+1 , len(nums1) ):

                y = nums1[ii]

                zt = []
                if not binSearch(yt, y):
                    continue

                for i in range(ii+1 , len(nums1) ):
                    z =  nums1[i]
                    if not binSearch(zt, z):
                        continue

                    idx = 0
                    n2_len = len(nums2)

                    while idx < n2_len and nums2[idx] != x:
                        idx += 1
                    if idx == n2_len:
                        continue
                    idx += 1

                    while idx < n2_len and nums2[idx] != y:
                        idx += 1
                    if idx == n2_len:
                        continue
                    idx += 1

                    while idx < n2_len and nums2[idx] != z:
                        idx += 1
                    if idx == n2_len:
                        continue

                    res += 1

        print(res)

        return res
        """
        n = len(nums1)

        pos_in_nums2 = [0] * n
        for i, v in enumerate(nums2):
            pos_in_nums2[v] = i

        # Tablica indeksów z nums1 przemapowana na nums2
        A = [pos_in_nums2[v] for v in nums1]

        smaller_left = [0] * n
        arr = [[A[i], i] for i in range(n)]
        print(arr)

        def merge_sort(items):
            if len(items) <= 1:
                return items

            mid = len(items) // 2
            left = merge_sort(items[:mid])
            right = merge_sort(items[mid:])

            return merge(left, right)

        def merge(left, right):
            merged = []
            i = j = 0

            # Kluczowy moment:
            # Przechodzimy przez prawą tablicę. Dla każdego elementu z prawej
            # sprawdzamy, ile elementów z lewej jest od niego mniejszych.
            while i < len(left) and j < len(right):
                if left[i][0] < right[j][0]:
                    merged.append(left[i])
                    i += 1
                else:
                    # Element z prawej (right[j]) jest większy od wszystkich
                    # dotychczasowych elementów z lewej (od 0 do i-1)
                    smaller_left[right[j][1]] += i
                    merged.append(right[j])
                    j += 1

            # Dopisujemy resztę z prawej (jeśli lewa się skończyła)
            while j < len(right):
                smaller_left[right[j][1]] += i
                merged.append(right[j])
                j += 1

            # Dopisujemy resztę z lewej
            while i < len(left):
                merged.append(left[i])
                i += 1

            return merged

        merge_sort(arr)

        # Krok 3: Obliczenie wyniku końcowego
        ans = 0
        for j in range(n):
            # Ile mniejszych po lewej (mamy to z merge sorta)
            s_l = smaller_left[j]

            # Ile mniejszych po prawej (matematycznie)
            s_r = A[j] - s_l

            # Ile większych po prawej
            g_r = (n - 1 - j) - s_r

            ans += s_l * g_r

        return ans

nums1 = [2,0,1,3]
nums2 = [0,1,2,3]
s = Solution()
s.goodTriplets(nums1,nums2)








