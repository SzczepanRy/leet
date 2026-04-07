class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        ##add length
        intervals = [(pair[0], pair[1] , abs(pair[1] - pair[0])) for pair in intervals ]

        def merge(arr , B , p , q, r):
            i = p
            j = q
            k = p

            while i < q and j < r:
                if arr[i][1] < arr[j][1]:
                    B[k] = arr[i]
                    i+=1
                elif arr[i][1] > arr[j][1]:
                    B[k] = arr[j]
                    j+=1
                else:
                    #arr[i][0] == arr[j][0]:
                    if arr[i][2] > arr[j][2]:
                        B[k] = arr[i]
                        i+=1
                    else:
                        B[k] = arr[j]
                        j+=1



                k+=1

            #dla końcówki to chynba nie ma znaczenia ?
            while i <q:
                B[k] = arr[i]
                i+=1
                k+=1

            while j <r:
                B[k] = arr[j]
                j+=1
                k+=1

            arr[p:r] = B[p:r]

        def msor(arr , B , p ,r):
            if r-p <=1:
                return

            mid= (p+r)//2
            msor(arr, B , p , mid)
            msor(arr, B , mid, r)
            merge(arr, B , p , mid , r)

        n = len(intervals)
        B = [[0] for _ in range(n)]
        msor( intervals , B , 0 , n)



        # morze priorytet do usunięcia mają większe ale zaczynające sie od tej samej liczny
        #KURWA WSZYSTKO CO PISZE TO ZACHŁANY KMS
        count = 0

        # Koniec ostatniego przedziału, który ZOSTAWIAMY
        last_end = intervals[0][1]

        # Startujemy od drugiego przedziału
        for i in range(1, len(intervals)):
            if intervals[i][0] < last_end:
                # Nachodzą na siebie! Usuwamy ten aktualny (bo ma późniejszy koniec)
                count += 1
            else:
                # Nie nachodzą na siebie. To jest nasz nowy "ostatni dobry"
                last_end = intervals[i][1]

        print("count" , count)
        return count









intervals = [[1,2],[2,3]]
s = Solution()
s.eraseOverlapIntervals(intervals)
