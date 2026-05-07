# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """


        maxS = -float("inf")
        def rekur(node):
            nonlocal maxS

            if node == None or node.val == None:
                return 0

            left = max( rekur(node.left) , 0)
            right = max( rekur(node.right) , 0)

            maxPath = left + right + node.val
            maxS =max(maxPath, maxS)

            #ZWRÓĆ DO RODZICA: Rodzic może wybrać tylko jedną nogę (lewą LUB prawą)
            # aby zachować ciągłość ścieżki
            return node.val + max(left, right)

        rekur(root)
        return maxS










arr = [-10,9,20,None,None,15,7]

def makeTree(root , i , n):

    root.left = None
    root.right=  None

    li = i*2 +1
    if li < n :
        root.left = TreeNode(arr[li])

    ri = i*2 +2
    if ri < n :
        root.right = TreeNode(arr[ri])

    if root.left != None:
        makeTree(root.left , li , n)

    if root.right != None:
        makeTree(root.right , ri , n)

def p(root):
    print(root.val)

    if root.left != None:
        p(root.left)

    if root.right != None:
        p(root.right )


root = TreeNode(arr[0])
makeTree(root , 0 , len(arr))
p(root)

s=Solution()
print(s.maxPathSum(root))
