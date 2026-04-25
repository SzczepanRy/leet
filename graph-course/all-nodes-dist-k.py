# Definition for a binary tree node.

from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        # find the note from withcz i sfould search
        # element , len form root
        # 1. Zbuduj mapę rodziców (zamiana drzewa na graf)
        parent_map = {}
        def find_parents(node, par=None):
            if node:
                parent_map[node] = par
                find_parents(node.left, node)
                find_parents(node.right, node)

        find_parents(root)

        # 2. BFS startujący od obiektu target
        queue = deque([(target, 0)])
        visited = {target}
        res = []

        while queue:
            curr, dist = queue.popleft()

            if dist == k:
                res.append(curr.val)
            elif dist < k:
                # Sprawdź wszystkie 3 kierunki
                for neighbor in [curr.left, curr.right, parent_map[curr]]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
        return res

arr = [3,5,1,6,2,0,8,None,None,7,4]


head = TreeNode(3)
def make(root , arr , i ):
    c = root
    n = len(arr)
    if i <= n :
        li = i*2 +1
        ri= i*2 +2

        if li < n :
            l = TreeNode(arr[li])
            c.left = l
            make(l , arr , li)

        if ri < n :
            r = TreeNode(arr[ri])
            c.right = r

            make(r , arr , ri)

make(head , arr, 0 )
s = Solution()
target_node = head.left # W Twoim drzewie head to 3, a head.left to 5

print(s.distanceK(head, target_node, 2))
