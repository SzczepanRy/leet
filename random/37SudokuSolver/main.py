class Solution(object):

    def IsBoardClear(self, board):
        count = 0
        for arr in board :
            for el in arr:
                if(el == "."):
                    count+=1
        if count > 0:
            return False
        return True

    def findMaxInColumns(self, board , visited):
        maxArr = []
        maxIndex = -1
        for i in range(len(board)):
            arr = []
            if(not self.inVisited(visited,"x", i)):
                for j in range(len(board)):
                    if(board[j][i] != "." ):
                        arr.append(board[j][i])

            if(len(arr) > len(maxArr)):
                maxArr = arr
                maxIndex = i
        return maxIndex , maxArr


    def findMaxInRow(self, board, visited):
        maxArr = []
        maxIndex = -1
        for i in range(len(board)):
            arr = []
            if(not self.inVisited(visited,"y", i)):
                for j in range(len(board)):
                    if(board[i][j] != "."  ):
                        arr.append(board[i][j])

            if(len(arr) > len(maxArr)):
                maxArr = arr
                maxIndex = i
        return maxIndex , maxArr


    def findMaxInSquareCenterCoords(self , x , y, board):
        for i in range( 1 ,len(board), 3 ):
            for j in range( 1 ,len(board), 3 ):

                for m in range(-1, 2):
                    for n in range(-1, 2):
                        if( y == i+m and x == j+n ):
                            return j , i

    def numbersInSquares(self, x , y , board):
        arr = []
        for m in range(-1, 2):
            for n in range(-1, 2):
                if(board[y+m][n+x] != "."):
                    arr.append(board[y+m][n+x])

        return arr

    def possibleNumbers(self, arr):
        d = {
        '1':1,
        '2':1,
        '3':1,
        '4':1,
        '5':1,
        '6':1,
        '7':1,
        '8':1,
        '9':1,
        }
        for i in arr:
            d[i] -=1
        result = []
        for i in d:
            if(d[i]==1):
                result.append(i)
        return result


    def repeatingNumbers(self,arr1 , arr2 , arr3):
        d = {
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0,
        }

        for i in arr1:
            d[i] +=1
        for i in arr2:
            d[i] +=1
        for i in arr3:
            d[i] +=1

        result = []
        for i in d:
            if(d[i]==3):
                result.append(i)
        return result

    def inVisited(self, visited, t , num):
        for val in visited[t]:
            if(num == val):
                return True
        return False

    def printBoard(self, board):
        for arr in board:
            print(arr)

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        visited ={
            "x":[],
            "y":[]

        }
        while not self.IsBoardClear(board):
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            self.printBoard(board)
            print(visited)
            maxX , numsInCol = self.findMaxInColumns(board , visited)
            maxY , numsInRow = self.findMaxInRow(board, visited)
            if(board[maxY][maxX] != "."):
                visited["x"].append(maxX)
                if(len(visited["x"]) == 9 ):
                    visited["y"].append(maxY)
                    visited["x"] =[]

            else:
                centerX , centerY = self.findMaxInSquareCenterCoords(maxX, maxY , board)
                numsInCenter = self.numbersInSquares( centerX , centerY , board)

                pNumsCol = self.possibleNumbers(numsInCol)
                pNumsRow = self.possibleNumbers(numsInRow)
                pNumsSqu = self.possibleNumbers(numsInCenter)

                pNumbers= self.repeatingNumbers(pNumsCol, pNumsRow, pNumsSqu)


                print(numsInCol , numsInRow , numsInCenter)
                print(pNumsCol, pNumsRow, pNumsSqu)
                print(pNumbers)
                if(len(pNumbers) > 0  ):

                    board[maxY][maxX] = pNumbers[0]
                else:
                    visited["x"].append(maxX)
                    if(len(visited["x"]) == 9 ):
                        visited["y"].append(maxY)
                        visited["x"] =[]


                    print("u fucked up" ,maxY , maxX)

s =Solution()
s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
