class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        letters= {
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

        res = []



        #3RADIX IN RAX QUERISE
        def countsort(strarr , off ):
            counts = [0]*10

            for st in strarr:
                counts[letters[st[0][len(st[0])-1 -off]]]+=1

            ind =0
            for i , count in enumerate(counts):
                counts[i] = ind
                ind += count


            sorted= [[] for _ in range(len(strarr))]

            for st in strarr:
                sorted[counts[letters[st[0][len(st[0])-1-off]]]] = st
                counts[letters[st[0][len(st[0])-1-off]]] += 1


            return sorted

        maxq = 1
        for q in queries:
            maxq = max(maxq , q[1])



        cp =[[num, i ] for i , num in enumerate(nums)]
        for i in range(maxq):
            cp = countsort(cp, i )
            res.append(cp)


        print(nums)
        for a in res:
            print(a)

        result=[]
        for q in queries:
            arr = res[q[1]-1]
            result.append(arr[q[0]-1][1])
        print(result)
        return result






nums = ["102","473","251","814"]
queries = [[1,1],[2,3],[4,2],[1,2]]
nums = ["24","37","96","04"]
queries = [[2,1],[2,2]]
nums = ["64333639502","65953866768","17845691654","87148775908","58954177897","70439926174","48059986638","47548857440","18418180516","06364956881","01866627626","36824890579","14672385151","71207752868"]
queries = [[9,4],[6,1],[3,8],[12,9],[11,4],[4,9],[2,7],[10,3],[13,1],[13,1],[6,1],[5,10]]
s=Solution()
s.smallestTrimmedNumbers(nums , queries)

