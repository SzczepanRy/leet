class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr = candidates
        arr.sort()
        result=[]
        if(len(arr) ==1 ):
            if(arr[0] == target):

                ar=[]
                ar.append(arr[0])
                result.append(ar)



        for l in range(1,len(candidates)):
            ##lenght
            for i in range(len(candidates)):
                if(arr[i] == target):

                    ar=[]
                    ar.append(arr[i])
                    if(ar not in result):
                        result.append(ar)

                for j in range(len(candidates) ):
                    print( j ,i , l, i+l)
                    print("d " ,arr[i : i+l] , arr[j])
                    if(j > i+l or j < i):

                        print(arr[i : i+l] , arr[j])
                        #print(arr[j : j+l] ,arr[j] )

                        ar =[]
                        ar.append(arr[j])
                        ar.extend(arr[i:i+l])
                        sum =0
                        for el in ar:
                            sum += el
                        print("sum" , sum)
                        if(sum == target):
                            ar.sort()
                            if(ar not in result):
                                result.append(ar)
                                print("nigga ",ar)
        print(result)
        return result

s =Solution()
s.combinationSum2([4,1,1,4,4,4,4,2,3,5] , 10)
