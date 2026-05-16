# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def rekur(node):
            if node == None:
                return 0 , 0

            #no take , take
            r2 , r1  = rekur(node.right)
            l2 , l1  = rekur(node.left)

            ## eathe r w can return 0 or val
            ## from right r2 + node.val , r1

            return max(r1,r2) + max(l1,l2) ,r2 + l2 + node.val

        l ,r = rekur(root)

        return max(l,r )
