class Solution(object):

    def check(self, arr):
        isGood = True
        d = {
            ".":0,
            "0":0,
            "1" :0,
            "2" :0,
            "3" :0,
            "4" :0,
            "5" :0,
            "6" :0,
            "7" :0,
            "8" :0,
            "9" :0,
        }
        for el in arr:
            print (el)
            d[el] +=1

        for i in range(len(arr)+1):

            print( "num of ", i ,d[str(i)])
            if(d[str(i)] > 1 ):
                isGood= False
        print("end row")
        return isGood

    def vertical(self, board):
        isGood = True
        for rowI in range(len(board)):
            d = {
                ".":0,
                "0":0,
                "1" :0,
                "2" :0,
                "3" :0,
                "4" :0,
                "5" :0,
                "6" :0,
                "7" :0,
                "8" :0,
                "9" :0,
            }
            for i in range(len(board) ):
                d[board[i][rowI]] +=1

            for i in range(len(board) +1 ):
                print( "num of ", i ,d[str(i)])
                if(d[str(i)] > 1 ):
                    isGood= False
            print("end vert")
        return isGood


    def checkSquare(self, i , j , board):
        isGood= True
        d = {
                ".":0,
                "0":0,
                "1" :0,
                "2" :0,
                "3" :0,
                "4" :0,
                "5" :0,
                "6" :0,
                "7" :0,
                "8" :0,
                "9" :0,
            }

        for m in range(-1, 2):
            for n in range(-1, 2):
                d[board[i+m][j+n]]+=1


        for i in range(len(board)+1):
            print( "num of ", i ,d[str(i)])
            if(d[str(i)]>1):
                return False
        print("endsquare")
        return isGood


    def checkSquares(self, board):
        isGood= True
        for i in range( 1 ,len(board), 3 ):
            for j in range( 1 ,len(board), 3 ):
                isGood = self.checkSquare(i , j , board)
                if(not isGood):
                    return False

        return isGood


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for row in board:
            if(not self.check(row)):
                print("faled row")
                return False

        if(not self.vertical(board)):
                print("faled verwtical")
                return False

        if(not self.checkSquares(board)):
                print("faled square")
                return False


        return True

        #

        print("all good")





s = Solution()
s.isValidSudoku([[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".","9",".",".",".",".",".",".","1"],["8",".",".",".",".",".",".",".","."],[".","9","9","3","5","7",".",".","."],[".",".",".",".",".",".",".","4","."],[".",".",".","8",".",".",".",".","."],[".","1",".",".",".",".","4",".","9"],[".",".",".","5",".","4",".",".","."]])
