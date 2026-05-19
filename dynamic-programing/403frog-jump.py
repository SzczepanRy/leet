class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        # pozycja (stany morzliwr)
        memo = {}
        for i in stones:
            memo[i] = []

        memo[0].append(0)

        moves = set()

        n = stones[-1]

        ## curr stone
        def rekur(i):
            if i > n or i < 0 :
                return False

            if i == n:
                return True

            if i in memo:
                # istnieje ścierzka do i

                arr = memo[i]
                # wszystkie k
                print(i , arr)

                for k in arr:
                    a = i + k - 1
                    b = i + k
                    c = i + k + 1

                    for r in range(-1 , 2 , 1):
                        v = i + k +r
                        if v in memo and (i , v) not in moves :
                            memo[v].append(k+r)


                    for jump in [a , b, c]:
                        if (i , jump) not in moves :
                            moves.add((i,jump))

                            if rekur(jump):
                                return True

            return False


        v = rekur(0)

        print(moves)
        print(memo)

        return v

stones = [0,1,2,3,4,8,9,11]
s = Solution()
print(s.canCross(stones))
