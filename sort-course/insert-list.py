
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

class Solution(object):
    def insertionSortList(self, head):
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



        if head.val > head.next.val:
            nh = head.next
            tail = nh.next
            nh.next = head
            head.next = tail
            head = nh

        c = head


        while c.next != None:
            grab = c.next
            zagrab = grab.next


            nh = head



            if grab.val < head.val:
                    c.next = zagrab      # Wypinamy
                    grab.next = head     # Wpinamy na start
                    head = grab          # Mamy nowy head

            else:
                while nh.next != grab and nh.next.val <= grab.val:
                    nh = nh.next


                if nh.next != grab:
                    #znaleziony element większy od grab który jest na nh.next
                    # musi znaleść sie przed nh.next


                    c.next = zagrab

                    tail = nh.next# biore tail wraz w większym elementem
                    nh.next = grab# wzamienia wartość większego na mniejszym
                    grab.next = tail # wszystkie elementy po mniejszym zanieniam na te po większym wraz z nim

                else:
                    c = c.next


        return head








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

r1 = ListNode(4)

create(r1 , [2,1,5])
p(r1)


s = Solution()
p(s.insertionSortList(r1))





