
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        arr=[]
        for i in range(len(l1)):
            arr.append(0)
        for i in range(len(l1)):
            print(len(l1) , i)
            arr[i] = str(l1[len(l1)-i-1].val)

        arr1=[]
        for i in range(len(l2)):
            arr1.append(0)
        for i in range(len(l2)):
            print(len(l2) , i)
            arr1[i] = str(l2[len(l2)-i-1].val)

        num1 = int( "".join(arr))
        num2 = int( "".join(arr1))

        sum = num1 + num2

        numArr = []

        tempSum= sum
        while tempSum >0 :
            r= tempSum%10
            tempSum = tempSum//10
            numArr.append(r)

        return numArr
#        print(arr1, arr, numArr)

arr=[2,4,3]
arr1 = [5,6,4]
l1=[]
l2=[]
lastNode=None
for i in arr:
    node = ListNode(i , lastNode)
    l1.append(node)
    lastNode = node

lastNode2=None
for i in arr1:
    node = ListNode(i , lastNode2)
    l2.append(node)
    lastNode2 = node

sol = Solution()
print(sol.addTwoNumbers(l1,l2))
