class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        # Zamiast dp = [0]*n, tworzymy listę słowników.
        # dp[i] będzie przechowywać: { roznica: ilosc_ciagow_dlugosci_2_lub_wiecej }
        dp = [{} for _ in range(n)]
        total_count = 0

        # Musimy sprawdzić każdą parę (j, i), bo elementy mogą być daleko od siebie
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]

                # Sprawdzamy, czy na indeksie 'j' kończyły się już jakieś ciągi o tej samej różnicy
                # To jest odpowiednik Twojego "dp[i-1] + count"
                count_at_j = dp[j].get(diff, 0)

                # Wszystkie ciągi z indeksu 'j' przedłużają się o nums[i],
                # stając się ciągami o długości >= 3. Dodajemy je do globalnego wyniku.
                total_count += count_at_j

                # Aktualizujemy stan dla indeksu 'i'.
                # Zapisujemy dotychczasowe ciągi (count_at_j) + 1 (nowa para [nums[j], nums[i]])
                dp[i][diff] = dp[i].get(diff, 0) + count_at_j + 1


        return total_count


nums = [2, 4, 6, 8, 10]

s = Solution()
s.numberOfArithmeticSlices(nums)
