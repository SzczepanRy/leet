class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """


        if len(words) < 2:
            return words

        used=[]
        buckets =[]

        i = 0
        for word in words:
            if word not in used:
                buckets.append([i,word,0])
                used.append(word)
                i+=1

        ## lkoczem jest index słów w used i buckets
        print(buckets)


        for bucket in buckets:
            for word in words:
                if word == bucket[1]:
                    bucket[2]+=1


        sorted = []
        for bucket in buckets:

            l = 0
            r = len(sorted)

            while l < r:
                mid = (l+r)//2

                if sorted[mid][2] > bucket[2]:
                    l = mid+1
                else:
                    r = mid

            sorted.insert(l ,bucket)


        letters={
                "a":1,
                "b":2,
                "c":3,
                "d":4,
                "e":5,
                "f":6,
                "g":7,
                "h":8,
                "i":9,
                "j":10,
                "k":11,
                "l":12,
                "m":13,
                "n":14,
                "o":15,
                "p":16,
                "r":17,
                "s":18,
                "t":19,
                "u":20,
                "w":21,
                "x":22,
                "y":23,
                "z":24
                }

        def compare(w1,w2):
            #l1> l2 1
            #l1== l2 0
            #l1<  l2 -1

            l1 = len(w1)
            l2 = len(w2)
            for i in range(min(l1,l2)):
                if w1[i] > w2[i]:
                    return 1
                elif w1[i] < w2[i]:
                    return -1

            if l1 < l2:
                return -1
            if l1 > l2:
                return 1


            return 0




        result = []


        for i in range(len(sorted)):
            for j in range(i,len(sorted)):
                if i != j and sorted[i][2] == sorted[j][2]:
                    if compare(sorted[i][1],sorted[j][1] ) > 0:
                        sorted[i] , sorted[j] =sorted[j],sorted[i]



        for i in range(k):
            result.append(sorted[i][1])



        print(result)
        return result


words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4


words = ["a","aa","aaa"]
k = 1
s = Solution()
s.topKFrequent(words, k)
