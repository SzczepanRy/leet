class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        """
        BRAK STABLINOSCI < NIE POMIENTANIE OSTATNIEJ RNDY RADIX
        letters={
                "0":0,
                "1":1,
                "2":2,
                "3":3,
                "4":4,
                "5":5,
                "6":6,
                "7":7,
                "8":8,
                "9":9
                }

        results = []
        # len nums but max string
        sor= [[]for _ in range(len(nums[0]))]

        for pair in queries:
            arr=nums[:]

            buckets = [[] for _ in range(10)]
            x = 0

            ## or arr longest str
            while len(arr[0]) > x:

                if len(sor[x]) !=0:
                    sor[x] = []


                for sti in range(len(arr)):
                    st = arr[sti]
                    let= st[len(st)-1-x]
                    digit = letters[let]
                    buckets[digit].append((st[len(st)-1-x:], sti ) )


                for a in buckets:
                    sor[x].extend(a)

                x+=1


                buckets = [[] for _ in range(10)]


        for i in sor:
            print(i)



        for pair in queries:
            results.append(sor[pair[1]-1][pair[0]-1][1] )



        print(results)
        return results
        """
        letters={
                "0":0,
                "1":1,
                "2":2,
                "3":3,
                "4":4,
                "5":5,
                "6":6,
                "7":7,
                "8":8,
                "9":9
                }



        # len nums but max string
        results = []
        # sor przechowuje stan po każdym kroku 'x' (trymowaniu)
        sor = [[] for _ in range(len(nums[0]))]

        # ZACZYNAMY OD ORYGINALNEJ LISTY Z INDEKSAMI
        # format: [("102", 0), ("473", 1), ...]
        current_order = []
        for i in range(len(nums)):
            current_order.append((nums[i], i))

        x = 0
        max_len = len(nums[0])

        while x < max_len:
            buckets = [[] for _ in range(10)]

            for item in current_order:
                s_val = item[0]  # string (np. "102")
                original_idx = item[1] # int (np. 0)

                # Wyciągamy znak od końca
                char = s_val[max_len - 1 - x]
                digit = letters[char]

                # Dodajemy całą krotkę do kubełka
                buckets[digit].append(item)

            # CZYŚCIMY current_order i układamy na nowo z kubełków (to daje STABILNOŚĆ)
            current_order = []
            for b in buckets:
                for element in b:
                    current_order.append(element)
                    # Zapisujemy kopię do sor[x], żeby potem wyciągnąć wynik dla query
                    sor[x].append(element)

            x += 1

        for pair in queries:
            k = pair[0]     # k-ty element
            trim = pair[1]  # ile cyfr od końca (nasze x + 1)

            # pair[1]-1 to indeks w sor, pair[0]-1 to k-ty najmniejszy
            results.append(sor[trim-1][k-1][1])

        return results


nums = ["102","473","251","814"]
queries = [[1,1],[2,3],[4,2],[1,2]]

nums = ["9415","5908","1840","5307"]
queries = [[3,2],[2,2],[3,3],[1,3]]

s = Solution()
s.smallestTrimmedNumbers(nums , queries)
