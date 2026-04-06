class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """



        numst = len(students)
        numse = len(seats)
        # if numst != numse coś źle
        reslen = max( max(seats) , max(students))+1
        res=[0]*reslen

        indseats = 0
        indstudents = 0

        height= 0
        for i in range(numse):
            res[seats[i]] -= 1

        for i in range(numst):
            res[students[i]] += 1


        count = 0
        height = 0
        for i in range(reslen):
            height += res[i]
            count +=abs(height)

        return count


s= Solution()
students = [19,2,17,20,7]
seats = [12,14,19,19,12]

s.minMovesToSeat(seats ,students)
