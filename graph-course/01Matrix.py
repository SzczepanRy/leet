from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if not mat or not mat[0]:
            return mat

        m, n = len(mat), len(mat[0])
        queue = deque()

        # 1. Przygotowanie macierzy i kolejki
        # Zamiast visited, zmieniamy 1 na coś, co oznacza "jeszcze nie odwiedzone" (np. -1)
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r, c)) # Zera są punktami startowymi
                else:
                    mat[r][c] = -1 # Oznaczamy jedynki do przetworzenia

        # 2. BFS - rozchodzenie się fali
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Jeśli sąsiad jest wewnątrz macierzy i jest oznaczony jako -1
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1 # Dystans to dystans rodzica + 1
                    queue.append((nr, nc))

        return mat
