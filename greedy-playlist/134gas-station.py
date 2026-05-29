class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)

        # 1. Szybkie sprawdzenie: jeśli w ogóle brakuje paliwa w całym układzie, to się nie da.
        if sum(gas) < sum(cost):
            return -1

        # Inicjalizujemy zmienne podobnie jak u Ciebie
        bag = 0
        start = 0
        pos = 0

        # Przechodzimy przez stacje tylko RAZ (stąd O(n))
        while pos < n:
            bag += gas[pos] - cost[pos]

            # Jeśli bag spadnie poniżej zera, to znaczy, że nie dojedziemy do pos + 1
            if bag < 0:
                # Kluczowa modyfikacja O(n): zamiast start += 1, skaczemy od razu za stację, na której polegliśmy
                start = pos + 1
                bag = 0  # zerujemy bak na nowy start

            pos += 1

        return start
gas = [2,3,4]
cost = [3,4,3]


gas= [1,2,3,4,5]
cost = [3,4,5,1,2]

gas = [4]
cost= [5]

s=Solution()
s.canCompleteCircuit(gas , cost)
