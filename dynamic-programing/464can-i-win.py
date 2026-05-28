# i want to kill myself

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        if desiredTotal < maxChoosableInteger:
            return True

        i = 0
        j = 0
        player = 1

        while j < desiredTotal:
            i +=1
            j += maxChoosableInteger
            player = (player+1)%2
            print(i , j, player)

        print(player)
        if player == 0 :
            return True
        # jesli to zalerzne od kroku too

        # i ty będzie nie ladnie

        #dla daqnego i , gracza 0 karzy i+j darcza 1 , finalnym wynikiem bedzei i

        memo =

        def rekur(i , player):
            if i >= desiredTotal:
                return player == 1


            if player == 1 :

                all_zeros = True

                for j in range(1,maxChoosableInteger+1):
                    v = rekur(i+j ,(player+1)%2 )
                    if not v :
                        all_zeros = False

                #print("1-0" , all_zeros , i)
                return all_zeros

            if player == 0:
                for j in range(1,maxChoosableInteger+1):
                    v = rekur(i+j ,(player+1)%2 )
                    #print("0-1" ,v ,i, "->" ,j+i)
                    if v :
                        return True

                return False



        return rekur(0 ,0)









s = Solution()
print(s.canIWin(5,10))
