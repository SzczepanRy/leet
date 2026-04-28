from collections import deque
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """


        ## najpierw dodajemy potem sprawdzamy warunki

        sor = []

        for s in equations:
            if s[1]== "=":
                sor.append(s)
        for s in equations:
            if s[1]== "!":
                sor.append(s)

        equations[:]=sor


        ad ={}

        def BFS(u,v):
            n = len(ad)
            visited = {el:False for el in ad}
            visited[u]=True

            queue = deque([u])


            while queue:
                c = queue.popleft()

                if c == v:
                    return True

                for n in ad[c]:
                    if not visited[n]:
                        visited[n] = True
                        queue.append(n)

            return False


        for stri in equations:

            u = stri[0]
            v = stri[3]
            st = stri[1]
            if u == v and st == "!":
                return False

            if st == "=":
                #dodajemy do grafu
                if u not in ad:
                    ad[u] = []
                if v not in ad:
                    ad[v] = []

                if v not in ad[u]:
                    ad[u].append(v)
                if u not in ad[v]:
                    ad[v].append(u)
            else:
                # sprawdzam czy istnieje połączenie

                if u in ad and v in ad:
                    if BFS(u,v):
                        return False

                if u not in ad:
                    ad[u] = []
                if v not in ad:
                    ad[v] = []

        return True




equations = ["a!=b","b!=c","c!=a"]

s = Solution()
print(s.equationsPossible(equations))
