from collections import deque


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        stack = [0]

        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)

        for v in visited:
            if not v:
                return False
        return True


s = Solution()
s.canVisitAllRooms()
