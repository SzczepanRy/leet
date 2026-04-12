# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """



        def reverse(root ):
            curr = root
            prev = None

            while curr != None:
                next_node = curr.next
                curr.next = prev

                prev = curr
                curr = next_node

            return prev




        c = head

        length = 0
        while c != None:
            c=c.next
            length+=1


        przedzialy = length//k

        curr = head
        count = 0

        final_head = None
        prev_gr_end = None

        while przedzialy > 0:

            lasthead= curr

            #curr can be none
            while count < k-1 :
                curr = curr.next
                count+=1

            tail = curr.next
            curr.next = None

            revhead = reverse(lasthead)

            ## head after first switch
            if final_head is None:
                final_head= revhead

            ## byk łączenia 2134 by nienbyło 2134 i 2143
            if prev_gr_end is not None:
                prev_gr_end.next = revhead


            lasthead.next = tail

            """
            p = revhead
            while p != None:
                p = p.next
            p.next = curr
            """


            curr = tail

            prev_gr_end = lasthead
            count = 0
            przedzialy-=1

        return final_head




def fill(root , arr):
    c = root
    for num in arr:
        n = ListNode(num)
        c.next = n
        c = n

def p(root ,test="print"):
    print(test)
    c = root
    while c != None:
        print(c.val)
        c = c.next




root = ListNode(1)
head = [2,3,4,5]
k = 2

fill(root, head)
p(root , "init")
s=Solution()
s.reverseKGroup(root,k)
