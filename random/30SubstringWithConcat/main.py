class Solution(object):
    def checkIfSubstr(self , s , words):
        resultArr = []
        for i in range(len(s)):
            for j in words:
                isGood = True
                for p in range(len(j)):
                    try:
                        if(s[i+p] != j[p]):
                            isGood = False
                    except:
                        print("to far")
                if(isGood):
                    resultArr.append(j)
                #print(isGood)
        resultArr.sort()
        words.sort()


        print(" zabij sie prosze: ", resultArr , words,  "".join(resultArr) == "".join(words) )
        if( "".join(resultArr) != "".join(words)):
            return False
        else:
            if len(s) == len("".join(resultArr)):
                print("allgood")
                return True
            else:
                return False



    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        for i in range(0,len(s),len(words[0])):
            st = s[i :i+len("".join(words))]

            print(st, i , i + len("".join(words)), "".join(words))
            if(i + len("".join(words)) <= len(s) ):
                if(self.checkIfSubstr(st, words)):
                    result.append(i)
        print(result)
        return result







s = Solution()
s.findSubstring("barfoothefoobarman" , ["foo" , "bar"])

