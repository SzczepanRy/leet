# i want to kill myself


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        # i ty będzie nie ladnie

        # dla daqnego i , gracza 0 karzy i+j darcza 1 , finalnym wynikiem bedzei i
        suma_wszystkich = (1 + maxChoosableInteger) * maxChoosableInteger // 2
        if suma_wszystkich < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True

        # 2. Tworzymy ręczną tablicę na cache (None oznacza nieobliczony stan)
        # Rozmiar to 2 do potęgi (maxChoosableInteger + 1)
        cache_size = 1 << (maxChoosableInteger + 1)
        memo = [None] * cache_size

        def rekur(current_total, used_mask):
            # Jeśli ten stan był już kiedyś obliczony, zwróć go natychmiast!
            if memo[used_mask] is not None:
                return memo[used_mask]

            for move in range(1, maxChoosableInteger + 1):
                # Sprawdzenie, czy liczba jest wolna
                if not (used_mask & (1 << move)):
                    # Jeśli ten ruch wygrywa grę
                    if current_total + move >= desiredTotal:
                        memo[used_mask] = True  # Zapisz w tablicy przed powrotem
                        return True

                    # Jeśli przeciwnik po tym ruchu przegra
                    if not rekur(current_total + move, used_mask | (1 << move)):
                        memo[used_mask] = True  # Zapisz w tablicy przed powrotem
                        return True

            # Jeśli żaden ruch nie dał wygranej
            memo[used_mask] = False  # Zapisz w tablicy przed powrotem
            return False

        return rekur(0, 0)


s = Solution()
print(s.canIWin(4, 6))
