class Solution:
    def findNumberOfLIS(self, nums) :

        n = len(nums)
        if n == 0:
            return 0

        # Każda liczba na start ma długość 1 i 1 sposób jej ułożenia
        length = [1] * n
        count = [1] * n

        for i in range(n): # Idziemy przez każdą liczbę (nasze "B")
            for j in range(i): # Sprawdzamy wszystkie liczby przed nią (nasze "A")

                if nums[i] > nums[j]: # Czy B może stać na A?

                    # Czy to najdłuższy ciąg jaki dotąd widzieliśmy dla liczby B?
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j] # "Przejmujemy" liczbę sposobów od A

                    # Czy to kolejna droga dająca tę samą maksymalną długość?
                    elif length[j] + 1 == length[i]:
                        count[i] = count[i] + count[j] # Dodajemy nowe sposoby

        # Na koniec szukamy, jaka była rekordowa długość w całej tablicy
        max_l = 0
        for l in length:
            if l > max_l:
                max_l = l

        # Sumujemy sposoby tylko dla tych liczb, które osiągnęły rekordową długość
        wynik = 0
        for i in range(n):
            if length[i] == max_l:
                wynik = wynik + count[i]

        print(length)
        print(count)

        print(wynik)
        return wynik

s=Solution()
s.findNumberOfLIS([1,3,5,4])

