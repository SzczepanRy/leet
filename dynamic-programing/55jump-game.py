class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        # To jest nasze "DP" skompresowane do jednej zmiennej
        # max_reach mówi: jaki jest najdalszy indeks, który możemy "odblokować"
        max_reach = 0

        for i, v in enumerate(nums):
            # Jeśli obecny indeks i jest większy niż nasz zasięg,
            # to znaczy, że nigdy tu nie dotrzemy
            if i > max_reach:
                return False

            # Aktualizujemy zasięg: obecny rekord vs to, co daje skok z i
            max_reach = max(max_reach, i + v)

            # Optymalizacja: jeśli już sięgamy do końca, nie ma co dalej liczyć
            if max_reach >= n - 1:
                return True

        return max_reach >= n - 1

s= Solution()
print(s.canJump([0,2,1,1,4]))
