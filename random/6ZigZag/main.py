class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows ==1 ):
            return s

        print("#######")
        arr = list(s)

        board={}

        for i in range(numRows):
            board[i] = {}

        print(arr)
        print(board)
        print("#######")

        col =0
        row =0
        temp =0
        for i in range(0 ,len(arr)):
            if(row ==0 ):
                temp =0
            if(i == 0):
                print("begin")
                board[row][col] = arr[0]
                continue
            if(temp==0 and  row  < numRows):
                if(row ==0):
                    row +=1
                print (row ,col)
                board[row][col] = arr[i]
                row +=1
            else:
                if( temp ==0 ):
                    row -=1
                row -=1
                col+=1
                print (row,col)
                board[row][col] = arr[i]
                temp =1
        print(board)
        result = ""

        for s in board:
            keys = list(board[s].keys())
            keys.sort()
            for q in keys:
                print(board[s][q])
                result += board[s][q]
        print(result)
        return result

s = Solution()
s.convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.", 5)

