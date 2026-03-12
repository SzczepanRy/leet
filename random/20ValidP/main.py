class Solution(object):


    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = list(s)
        if(len(arr) %2 ==1):
            print("false")
            return False
       # print(arr)
        stack =[]
        open =[ "{" , "[" , "("]
        close=["}" , "]" , ")"]
        if(arr[len(arr)-1] in open):
            print("false5")
            return False
        if(arr[0] in close):
            print("false5")
            return False

        for i in range(1,len(arr),2 ):
            for j in range(len(arr)):
       #         print( "as  ", i+j)
                for k in range(len(open) ):
                    if(i+j < len(arr)):


                        if( arr[j] == open[k] and arr[i+j] == close[k]):
                            arr[j] = ""
                            arr[i+j] = ""
                            if( i>1):
                                for p in range(i):
                                    if(arr[1+j+p] != ""):
                          #              print(arr[j+p: i+j] , "  asd")
                                        return False


          #              print(arr)


        """
        if(opened != closed):
            print("false6")
            return False
        """

        st = "".join(arr)
        if(st == ""):
            print("true")
            return True

        print("false")
        return False


s =Solution()
s.isValid("[({]})")
