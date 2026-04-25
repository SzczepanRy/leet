from collections import deque


class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        male_litery = {chr(i) for i in range(97, 123)}
        duze_litery = {chr(i) for i in range(65, 91)}
        ## bst , tzrzymający w kolejce , pozycje dystsans i klucze
        n = len(grid)
        m = len(grid[0])

        dist = [[float("inf")] * m for _ in range(n)]

        sx = -1
        sy = -1

        key_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@":
                    sx = j
                    sy = i
                if grid[i][j] in male_litery:
                    key_count += 1

        visited = set([(sx, sy, "")])

        if sx == -1:
            return -1

        dist[sy][sx] = 0

        queue = deque([(sx, sy, 0, "")])

        while queue:
            cx, cy, cd, keysA = queue.popleft()

            for xd, yd in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx = cx + xd
                ny = cy + yd

                nd = cd + 1

                if 0 <= nx < m and 0 <= ny < n:
                    char = grid[ny][nx]
                    if char == "#":
                        continue

                    nkeys = keysA

                    if char in male_litery and char not in keysA:
                        nkeys = "".join(sorted(keysA + char))
                        if len(nkeys) == key_count:
                            print(nd)
                            return nd

                    if char in duze_litery and char.lower()not in keysA:
                        continue

                    if (nx, ny, nkeys) not in visited:
                        visited.add((nx, ny, nkeys))
                        queue.append((nx, ny, nd, nkeys))
        return -1


grid = ["@..aA", "..B#.", "....b"]
grid = ["@.a..", "###.#", "b.A.B"]
grid = ["@...a", ".###A", "b.BCc"]
s = Solution()
s.shortestPathAllKeys(grid)
