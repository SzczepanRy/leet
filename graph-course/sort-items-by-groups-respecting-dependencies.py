from collections import deque
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """

        # buduje grupy
        groups = [ [] for _ in range(m)]

        for i , g in enumerate(group):
            if g!=-1:
                groups[g].append(i)
            else:
                groups.append([i])
                #tu modd smartt
                group[i] = len(groups) -1

        indegg=[0]*len(groups)

        # ZMIANA 1 NAPRAWIONA: Teraz to faktycznie jest set()
        adj = [set() for _ in range(len(groups))]

        item_indegg = [0] * n
        item_adj = [[] for _ in range(n)]

        for i , arr in enumerate(beforeItems):
            for u in arr:
                # ZMIANA 2 NAPRAWIONA: Używamy tablic dla itemów!
                item_indegg[i] += 1
                item_adj[u].append(i)

                # Logika Grup: grupa u musi być przed grupą i
                gu = group[u]
                gi = group[i]
                if gu != gi:
                    if gi not in adj[gu]:
                        adj[gu].add(gi)
                        indegg[gi] += 1 # i czeka na u, więc indegree 'i' rośnie

        #################################
        # DODATEK: Szybkie sortowanie samych itemów
        item_q = deque([i for i in range(n) if item_indegg[i] == 0])
        item_topo = []
        while item_q:
            curr = item_q.popleft()
            item_topo.append(curr)
            for nxt in item_adj[curr]:
                item_indegg[nxt] -= 1
                if item_indegg[nxt] == 0:
                    item_q.append(nxt)

        if len(item_topo) != n:
            return [] # Jeśli jest cykl w przedmiotach, od razu zwracamy []

        # Aktualizujemy zawartość grup: teraz wrzucamy do nich itemy w JUŻ POSORTOWANEJ kolejności
        groups_sorted = [[] for _ in range(len(groups))]
        for item in item_topo:
            groups_sorted[group[item]].append(item)
        ######################################

        # ZMIANA 3 NAPRAWIONA: Inicjalizujemy kolejkę posortowanymi grupami (groups_sorted)
        queue = deque([ (i , groups_sorted[i]) for i in range(len(groups)) if 0 == indegg[i] ])

        topo = []
        while queue:
            gind , currgroup = queue.popleft()
            topo.append(currgroup)

            for ngind in adj[gind]:
                indegg[ngind] -= 1

                if indegg[ngind] <= 0:
                    # Tutaj też dopinamy posortowaną wersję grupy
                    queue.append( ( ngind , groups_sorted[ngind] ))

        res = []

        for arr in topo:
            res.extend(arr)

        if len(res) != n :
            return []

        print(res)
        return res
n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]

s = Solution()
s.sortItems(n,m,group,beforeItems)
