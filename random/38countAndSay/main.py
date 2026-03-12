class Solution(object):

    def recur(self, s,  numOfLoops):
        print("intake" , s)
        if(numOfLoops==0):
            return s

        d ={
                "1":0,
                "2":0,
                "3":0,
                "4":0,
                "5":0,
                "6":0,
                "7":0,
                "8":0,
                "9":0
        }
        lastItem= list(s)[0]
        result=[]
        print(list(s))
        for i in list(s):
            if(lastItem != i):
                print("not last" , d[i] , i)
                result.append(str(d[lastItem]))
                result.append(lastItem)


                d={
                "1":0,
                "2":0,
                "3":0,
                "4":0,
                "5":0,
                "6":0,
                "7":0,
                "8":0,
                "9":0
                }
                lastItem = i
                d[i]+=1
                print(i , d[i])
            else:
                print(i)
                d[i]+=1

        result.append(str(d[lastItem]))
        result.append(lastItem)
        print(result)

        numOfLoops -=1
        return self.recur("".join(result) , numOfLoops)




    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.recur("1" , n-1 )




s = Solution()

s.countAndSay(4)
