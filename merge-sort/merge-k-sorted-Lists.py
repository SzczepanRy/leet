# Definition for singly-linked list.

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0] if lists[0] else None


        def p(root , s=""):
            print("list : " ,s,"  ")
            c = root
            while c != None:
                print(c.val)
                c = c.next



        def merge(root1 , root2):
            # root 1 , and root 2 are already sorted

            dummy = ListNode(0)
            tail = dummy

            curr1 = root1
            curr2 = root2


            while curr1 != None and curr2 != None:

                if curr1.val >= curr2.val:
                    tail.next = curr2
                    curr2 = curr2.next

                else:
                    tail.next = curr1
                    curr1 = curr1.next

                tail = tail.next

                p(tail , "curr1")


            if curr1 == None:
                tail.next = curr2
            else:
                tail.next = curr1

            return dummy.next


        def sor(lists):

            n = len(lists)
            if n == 0:
                return None

            if n ==1:
                return lists[0]
            mid = n//2

            l = lists[:mid]
            r = lists[mid:]

            ls = sor(l)
            rs = sor(r)
            return merge(ls , rs)


        r1 = sor(lists)
        p(r1 , "result : ")

        return r1



def create(root, arr):
    c = root
    for i in arr:
        n = ListNode(i)
        c.next = n
        c = n

def p(root):
    print("test")
    c = root
    while c != None:
        print(c.val)
        c = c.next

r1 = ListNode(1)
r2 = ListNode(2)
r3 = ListNode(2)

create(r1 , [3,5,8])
create(r2 , [3,9,12])
create(r3 , [3,6,32])
p(r1)
p(r2)
p(r3)

lis = [r1,r2,r3]
s = Solution()
s.mergeKLists(lis)
