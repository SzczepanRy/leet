class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Warunek bazowy: dla n = 0 mamy tylko liczbę 0
        if n == 0:
            return 1

        # Dla n = 1 mamy 10 liczb (0-9)
        res = 10

        # unikalne_dla_dlugosci reprezentuje ile jest unikalnych kombinacji
        # dla aktualnie badanej długości liczby. Zaczynamy od 9 (dla pierwszej cyfry)
        unikalne_dla_dlugosci = 9

        # Ile cyfr mamy do wyboru dla kolejnych pozycji (zaczynamy od 9, bo jedna już odpadła)
        dostepne_cyfry = 9

        # Pętla liczy unikalne liczby dla długości od 2 do n
        for i in range(2, min(n + 1, 11)):
            unikalne_dla_dlugosci *= dostepne_cyfry
            res += unikalne_dla_dlugosci
            dostepne_cyfry -= 1  # Z każdym krokiem mamy o jedną cyfrę mniej do wyboru

        return res
