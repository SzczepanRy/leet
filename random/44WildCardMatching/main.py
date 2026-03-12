class Solution(object):

    def checkStrInTemp(self, tArr ):
        beginIndex=[]
        strArr = []

        leterLast = False
        lastIndex = -1
        for i in range(len(tArr)):
            if(  tArr[i] != "*" and i > lastIndex):
                index = i
                valArr= []
                lastJ=0
                for j in range(i, len(tArr)):
                    lastJ= j
                    if(tArr[j] != "*" ):
                        valArr.append(tArr[j])
                    else:
                        lastIndex = j-1
                        break
                print(lastJ)
                strArr.append(valArr)
                beginIndex.append(index)

                if(lastJ == len(tArr) - 1 ):
                    return strArr , beginIndex
            else:
                continue

        return strArr , beginIndex


    def validateStr(self , strArr , sArr, bIArr ):
        validStr=[]
        """
        for cStrI in range(len(sArr)):
            continous= True
        """
        cI = 0
        lastIndexes= []
        for i in range(len(strArr)):
            if(strArr[i] == sArr[cI][0] or sArr[cI][0] == "?" ):
                isGood = True

                print("good" , strArr[i] ,cI, sArr[cI][0])
                for j in range(1, len(sArr[cI])):
                    if(i+j < len(strArr)):
                        if(strArr[i +j ] == sArr[cI][j] or sArr[cI][j] == "?"):
                            #issGood
                            print("good" , strArr[i+j] ,cI, sArr[cI][j])
                        else:
                            print("not good")
                            isGood = False
                            break
                    if(i+j > len(strArr) -1):
                        return validStr, lastIndexes

                if(isGood):
                    validStr.append(cI)
                    lastIndexes.append(i+len(sArr[cI] ) -1)
                    cI+=1
                    print(cI)
                    if(cI >= len(sArr)):
                        break
        return validStr, lastIndexes


    def checkI(self,arr):
        last = -1
        for val in arr:
            if(val > last):
                last = val
            elif(val < last):
                return False

        return True



    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if(p == "*"):
            return True

        strArr = list(s)
        tempArr = list(p)

        sArr , bIArr = self.checkStrInTemp(tempArr)
        print(sArr , bIArr )
        vStrs , lIndexes  = self.validateStr(strArr, sArr , bIArr)
        #for i in range(len(temparr))

        val = self.checkI(lIndexes)
        if(len(lIndexes) == 0 ):
            return False

        print(vStrs , lIndexes, lIndexes[len(lIndexes) -1 ] , len(strArr) -1)
        if(val and len(vStrs) == len(sArr) and lIndexes[len(lIndexes) -1 ] == len(strArr) -1):
            return True
        return False



s=Solution()
print(s.isMatch("cb" , "?a"))
