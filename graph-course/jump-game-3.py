from collections import deque
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """

        if 0 not in arr:
            return False

        queue = deque([(arr[start] , start)])

        visited = [False] *len(arr)


        while queue:
            curr , ind = queue.popleft()

            # left
            if curr == 0 :
                print("found")
                return True

            lind = ind - curr
            if lind >= 0 and lind < len(arr):
                if not visited[lind] :
                    lval = arr[lind]
                    visited[lind] = True

                    queue.append((lval, lind))


            rind = ind + curr
            if rind < len(arr) and rind >= 0:
                if not visited[rind] :
                    rval = arr[rind]
                    visited[rind] = True
                    queue.append((rval, rind))

        return False
arr = [3,0,2,1,2]
start = 2
s = Solution()
s.canReach(arr, start)
