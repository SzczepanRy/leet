class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()  # Niezbędne, by duplikaty były obok siebie
        results = []
        used = [False] * len(nums)

        def backtrack(current_path):
            # Jeśli ścieżka ma długość tablicy, mamy pełną permutację
            if len(current_path) == len(nums):
                print(current_path)
                results.append(list(current_path))
                return

            for i in range(len(nums)):
                # 1. Jeśli element jest już użyty w tej ścieżce - pomiń
                if used[i]:
                    continue

                # 2. Jeśli to duplikat i poprzedni identyczny element NIE był użyty
                # w tym kroku (czyli właśnie skończyliśmy z nim pracować) - pomiń
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                # Wybór (Standardowy Backtracking)
                used[i] = True
                current_path.append(nums[i])

                backtrack(current_path)

                # Cofnięcie (Backtrack)
                used[i] = False
                current_path.pop()

        backtrack([])
        return results



nums = [1,2,1]
s = Solution()
s.permuteUnique(nums)
