from collections import deque


class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """

        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        visited = set()
        visited.add(startGene)

        while queue:
            current_word, dist = queue.popleft()

            if current_word == endGene:
                return dist

            for banked in bank:
                if banked not in visited:
                    diff = 0
                    for i in range(len(current_word)):
                        if current_word[i] != banked[i]:
                            diff += 1

                    if diff == 1:
                        visited.add(banked)
                        queue.append((banked, dist + 1))

        return -1


startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
s = Solution()
s.minMutation(startGene, endGene, bank)
