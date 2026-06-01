# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        root = Node(node.val)

        dic = {}
        dic[node] = root

        def dfs(r, curr):
            for n in r.neighbors:
                if n not in dic:
                    nn = Node(n.val)
                    dic[n]=nn
                    curr.neighbors.append(nn)
                    dfs(n , nn)
                else:
                    # jeśli byliśmy to i tak dodajemy bo chcemy zamknąć
                    curr.neighbors.append(dic[n])


        for v in node.neighbors:
            if v not in dic:
                c = Node(v.val)

                dic[v] = c

                dfs(v , c)
                root.neighbors.append(c)
            else:
                root.neighbors.append(dic[v])

        return root






