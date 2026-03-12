# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def p(root , s=""):
            print("list : " ,s,"  ")
            c = root
            while c != None:
                print(c.val)
                c = c.next


        def merge(root1 , root2):
            dummy = ListNode(0)
            tail = dummy
            curr1 = root1
            curr2 = root2

            while curr1 != None and curr2 != None:

                if curr1.val <= curr2.val:
                    tail.next  = curr1
                    curr1 = curr1.next
                else:
                    tail.next  = curr2
                    curr2 = curr2.next

                tail = tail.next

            if curr1 == None:
                tail.next = curr2
            else:
                tail.next = curr1

            return dummy.next

        def leng(root):
            if not root: return 0
            n = 0
            c = root
            while c != None:
                n+=1
                c = c.next
            return n



        def devide(root):
            n =leng(root)

            mid = n //2
            x = 0
            c = root
            while x != mid:
                x+=1
                c = c.next

            right = c.next
            c.next = None
            return right




        def splitl(root):


            if not root:
                return None
            if not root.next:
                return root



            r = devide(root)
            l = root

            ls = splitl(l)
            rs = splitl(r)

            return merge(ls ,rs)

        root = splitl(head)
        p(root, " root ")
        return root

"""
    modelowe rozwianie
    def sortList(self, head):
    if not head or not head.next:
        return head

    # 1. Znajdź środek i rozetnij listę
    def get_mid(node):
        slow, fast = node, node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right_start = slow.next
        slow.next = None  # To jest KLUCZOWE rozcięcie!
        return right_start

    def merge(l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    # Rekurencyjny podział
    mid = get_mid(head)
    left = self.sortList(head)
    right = self.sortList(mid)

    return merge(left, right)
"""





def create(root, arr):
    c = root
    for i in arr:
        n = ListNode(i)
        c.next = n
        c = n


root = ListNode(-1)
create(root,[5,3,4,0])
s = Solution()
s.sortList(root)
