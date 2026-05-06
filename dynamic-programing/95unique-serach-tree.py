# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """

        if n == 0 :
            return []


        def build(start , end):
            if start > end:
                return [None]


            allT=[]

            for i in range(start, end+1):

                leftSubtrees = build(start, i-1)
                rightSubtrees = build(i+1, end)
                print(leftSubtrees ,rightSubtrees  )

                for left in leftSubtrees:
                    for right in rightSubtrees:
                        root = TreeNode(i) # Tworzymy korzeń
                        root.left = left   # Podpinamy lewe poddrzewo
                        root.right = right # Podpinamy prawe poddrzewo
                        allT.append(root) # Dodajemy gotowe drzewo do listy

            return allT

        return build(1, n)


