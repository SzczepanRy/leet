class Solution(object):


    def recur(self , obj):
        if( len(obj) ==1 ):
            return obj
        newObj ={}
        maxPre = []
        start = obj[0]
        for i in range(1 ,len(obj)):
            curr=obj[i]

            if(len(start) > len(curr)):
                for a in range(1,len(curr)+1):
                    for b in range(len(curr)):

         #               print(a,b,curr[b:a+b])
                        windowC = curr[b:a+b]
                        for c in range( len(start) - len(curr)+1):#+1?
                            windowS = start[c+b: c+a+b]

         #                   print( windowC , windowS)

                            if(windowC== windowS):
                                if(len(windowC) > len(maxPre) ):
                                    maxPre = windowC


            if(len(start) <= len(curr)):
                for a in range(1,len(start)+1):
                    for b in range(len(start)):

        #                print(a,b,start[b:a+b])
                        windowS = start[b:a+b]
                        for c in range( len(curr) - len(start)+1):#+1?
                            windowC = curr[c+b: c+a+b]

        #                    print( windowC , windowS)

                            if(windowC== windowS):
                                if(len(windowS) > len(maxPre) ):
                                    maxPre = windowS

            newObj[len(newObj)]= maxPre
            maxPre= []
            start= curr

        print(newObj)
        val = self.recur(newObj)
        return val

    def longestCommonPrefix(self, strs):
        obj={}
        for i in range(len(strs)):
            obj[len(obj)] = list(strs[i])

        final = self.recur( obj)
        return "".join(final[0])

s = Solution()

s.longestCommonPrefix(["cid","car"])
