class Solution(object):
    def UsedHeight(self, heights, h):
        for i in heights:
            if(i >= h ):
                return True

        return False


    def isValid(self, arr , height):
        for i in arr:
            if(i >= height):
                return True
        return False


    def flatten(slef , arr ):
        min =0
        isGood = True
        while isGood:
            for i in arr:
                if(min >= i ):
                    isGood= False
            if(isGood):
                min +=1

        print(min)
        for i in range(len(arr)):
            arr[i] = arr[i] - min

        print(arr)
        return arr

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        print(height)
        temp= height.copy()
        temp.sort()
        if( temp == height ):
            print(temp , height)
            return 0


        #index  [0], val[1]
        usedHeights=[]
        """
        if(height[0] > 1 ):
            for i in range(height[0]):
                begin.append(i)

        print(begin)

        begin.extend(height)
        height = begin
        """

        height = self.flatten(height)

        st = ",".join(map(str,height))
        st.strip("0")
        print(st)
        height = st.split(",")
        height =list(map(int, height))
        validZeros= 0
        print(height)
        for cVal in range(1,max(height)+1):
            print("cwel" , cVal)
            for i in range(len(height)-1): # -1 cuss we consider the wfireald in fornt
                cI = i
                #cVal = height[i]



                nI=  i+1
                nVal = height[i+1]

                if(cVal > 0 and not self.UsedHeight(usedHeights, cVal)):
                    usedHeights.append(cVal)
                    print(height[cI:])
                    ##  checksinghle for
                    ## height CVal
                    ## Index CI
                    ## val CVal
                    checkedTo = -1
                    ##
                    isValid=False
                    ## add one to shift check
                    numOfZeros = 0
                    for j in range( cI  ,len(height)):
                        print(j)
                        if(height[j] - (cVal - 1 ) <= 0 and self.isValid(height[j:], cVal)and not checkedTo==-1):
                            # zero
                            numOfZeros+=1

                            print("zoro found at index", j)
                        elif(height[j] >= cVal ):
                            print("checked up to " ,checkedTo,j )
                            checkedTo = j
                            validZeros += numOfZeros
                            numOfZeros = 0


        print("result",validZeros)
        return validZeros

s = Solution()

s.trap([1000,999,998,997,996,995,994,993,992,991,990,989,988,987,986,985,984,983,982,981,980,979,978,977,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966])


