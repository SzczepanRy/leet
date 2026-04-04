class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        # Tablica liczników dla sum od -n do n.
        # Dodajemy offset 'n', żeby indeksy były dodatnie.
        counts = [0] * (2 * n + 1)

        # Startujemy na wysokości 0 przed pierwszym elementem
        curr_height = 0
        counts[curr_height + n] = 1

        total_subarrays = 0
        smaller_sums_count = 0

        for num in nums:
            if num == target:
                # KROK W GÓRĘ:
                # Wszystko, co było na 'starej' wysokości, jest teraz mniejsze od nas.
                smaller_sums_count += counts[curr_height + n]
                curr_height += 1
            else:
                # KROK W DÓŁ:
                # Nowa wysokość, na którą właśnie spadliśmy, przestaje być "mniejsza".
                curr_height -= 1
                smaller_sums_count -= counts[curr_height + n]

            # Dodajemy do wyniku liczbę wszystkich mniejszych sum z przeszłości
            total_subarrays += smaller_sums_count

            # Zapisujemy obecną wysokość w liczniku
            counts[curr_height + n] += 1
            print(counts)

        return total_subarrays

nums = [1,2,2,3]
target = 2
s = Solution()
s.countMajoritySubarrays(nums , target)
