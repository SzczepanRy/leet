class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        #recur will be the death of me bad time

        def merge( l , r):
            res = []
            i = j = 0
            while len(l) > i and len(r) > j:
                if l[i] > r[j]:
                    res.append(r[j])
                    j+=1
                else:
                    res.append(l[i])
                    i+=1

            res.extend(l[i:])
            res.extend(r[j:])
            return res


        n = len(matrix)

        i = 1

        while len(matrix) != 1:

            li = (i-1)%(len(matrix)-1)
            ri = (i)%(len(matrix)-1)

            ls = matrix.pop(li)
            rs = matrix.pop(ri)

            result = merge(ls ,rs)
            matrix.append(result)
            i+=2

        return matrix[0][k-1]


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8



matrix = [[-5]]
k = 1
s= Solution()
s.kthSmallest(matrix, k)
