class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):

            if indexDiff <= 0: return False
        n = len(nums)

        # 1. Kompresja współrzędnych (Coordinate Compression)
        # Musimy wiedzieć, jakie wartości występują, żeby nadać im rangi
        # Używamy własnego merge_sort zamiast .sort()
        def my_sort(arr):
            if len(arr) <= 1: return arr
            mid = len(arr) // 2
            left = my_sort(arr[:mid])
            right = my_sort(arr[mid:])
            res = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]: res.append(left[i]); i += 1
                else: res.append(right[j]); j += 1
            res.extend(left[i:]); res.extend(right[j:])
            return res

        sorted_unique = []
        temp_sorted = my_sort(nums)
        if n > 0:
            sorted_unique.append(temp_sorted[0])
            for i in range(1, n):
                if temp_sorted[i] != temp_sorted[i-1]:
                    sorted_unique.append(temp_sorted[i])

        # Funkcja do szukania rangi (nasz własny Binary Search)
        def get_rank(val):
            low, high = 0, len(sorted_unique) - 1
            while low <= high:
                mid = (low + high) // 2
                if sorted_unique[mid] == val: return mid + 1
                if sorted_unique[mid] < val: low = mid + 1
                else: high = mid - 1
            return low # Zwraca miejsce, gdzie "powinna" być wartość

        # 2. Drzewo Fenwicka na liście (Binary Indexed Tree)
        bit = [0] * (len(sorted_unique) + 1)

        def update(idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)

        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        # 3. Przesuwne okno + Zapytania o zakres
        for i in range(n):
            # Szukamy zakresu rang, które mieszczą się w valueDiff
            left_rank = get_rank(nums[i] - valueDiff) + 1
            right_rank = get_rank(nums[i] + valueDiff + 1) # +1 dla domknięcia zakresu

            # Jeśli w drzewie są już liczby w tym zakresie wartości -> mamy to!
            if query(right_rank - 1) - query(left_rank - 1) > 0:
                return True

            # Dodajemy obecną liczbę do drzewa
            update(get_rank(nums[i]), 1)

            # Usuwamy liczbę, która wypadła z okna indexDiff
            if i >= indexDiff:
                update(get_rank(nums[i - indexDiff]), -1)

        return False







nums = [1,2,3,1]
indexDiff = 3
valueDiff = 0
nums = [1,5,9,1,5,9]
indexDiff = 2
valueDiff = 3
s = Solution()
print(s.containsNearbyAlmostDuplicate(nums , indexDiff , valueDiff))
