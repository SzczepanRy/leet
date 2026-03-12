class Solution(object):

    def recur(self ,allNums, currIndex, obj, ob ):
        l = len(obj[allNums[currIndex]])
        print(l)
        for j in range(len(allNums[currIndex]) ):
            #letters
            if(currIndex == 0):
                ob[str(j) ] = []


                for k in range(len(obj[allNums[currIndex]])**(len(allNums))):
                    ob[str(j)].append( [obj[allNums[currIndex]][k//(l)**(len(allNums) -1) ]])
                    if(currIndex == 1):
                        print("#")
            else:
                for k in range(len(obj[allNums[currIndex]])**(len(allNums)) ):
                    """
                    if(k == len(ob[str(j)]) and( allNums[currIndex] == "7" or allNums[currIndex] == "9" )):
                        ob[str(j)].append([])

                    if((int((3)**( len(allNums[currIndex]) - currIndex   ))) != 0):
                        print(len(allNums) -currIndex -1 ,k//(int((3)**( len(allNums[currIndex]) - currIndex   ))  ))
                        if ((3)**( len(allNums) -currIndex -1  ))>0 and k//int((3)**( len(allNums) -currIndex -1  )) < (len(allNums) -1)  :
                            ob[str(j)][k].append(obj[allNums[currIndex]][k//int((3)**( len(allNums) -currIndex -1  ))])
                        else:
                            ob[str(j)][k].append(obj[allNums[currIndex]][k%(3**())])
                    else:

                            ob[str(j)][k].append(obj[allNums[currIndex]][k%3])
                    """

#                    if((int((3)**(abs( len(allNums[currIndex]) - currIndex -1) ))) != 0):
                    #print(len(allNums[currIndex]) -currIndex  -1,k//(int((3)**( abs(len(allNums[currIndex]) - currIndex -1)   ))  ))
                    try:


                        if( int(k//int((l)**( len(allNums) -currIndex -1 )  )) <l )  :

                            print( len(allNums) - currIndex  ,k//int((l)**(  len(allNums) - currIndex -1 )))
                            ob[str(j)][k].append(obj[allNums[currIndex]][int(k//int((l)**( len(allNums) -currIndex -1  ) ))])
                            #else:
                             #   ob[str(j)][k].append(obj[allNums[currIndex]][k//3])
                        else:
                            ob[str(j)][k].append(obj[allNums[currIndex]][int(k//int((l)**( len(allNums) -currIndex -1 ) ))%l])
                    except:
                        print("fuck")


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        obj = {
            "2" : ["a" , "b" ,"c",""],
            "3" : ["d" , "e" ,"f",""],
            "4" : ["g" , "h" ,"i",""],
            "5" : ["j" , "k" ,"l",""],
            "6" : ["m" , "n" ,"o",""],
            "7" : ["p" , "q" ,"r" , "s"],
            "8" : ["t" , "u" ,"v",""],
            "9" : ["w" , "x" ,"y" ,"z"],

                }

        strs = list(digits)
        if(len(strs) == 1):
            print([obj[strs[0]]])
            result = []
            for i in obj[strs[0]]:
                if( i != ""):
                    result.append(i)

            return result

        num = 0
        if(len(strs) == 0 ):
            return []

        result = []
        allLeters= []
        ob={}
        lenofStr = len(strs)

        for i in range(len(strs)):
            self.recur(strs , i , obj , ob)

        for i in ob:
            for j in ob[i]:
                print(j , strs)
                arr = "".join(j)
                rarr = list(arr)
                if(len(rarr) == len(strs) ):
                    result.append("".join(rarr))


        print(result)


        print(ob)
        return result
s= Solution()

s.letterCombinations("2")
