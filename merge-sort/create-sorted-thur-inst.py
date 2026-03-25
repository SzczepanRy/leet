class Solution(object):
    def createSortedArray(self, instructions):
        print(instructions)
        #LEARN FEnwic asshole!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        MOD = 10**9 + 7
        max_val = max(instructions)
        # tree[i] will store the cumulative frequencies
        bit = [0] * (max_val + 1)

        def update(i, delta):
            while i <= max_val:
                bit[i] += delta
                i += i & (-i) # Move to the next responsible index

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i) # Move to the parent index
            return s

        total_cost = 0
        for i, val in enumerate(instructions):
            # Number of elements strictly less than val
            less_than = query(val - 1)
            # Number of elements strictly greater than val
            # i is the total elements currently in the 'nums' container
            # query(val) gives us elements <= val
            greater_than = i - query(val)

            total_cost += min(less_than, greater_than)
            update(val, 1)

        return total_cost % MOD
        """
        count = 0

        nums=[0]*(max(instructions)+1)

        # nlogn


        for i in range(len(instructions)):
            num = instructions[i]

            countL= 0
            for ind in range(num):
                countL += nums[ind]

            countR= 0
            for ind in range(num+1, len(nums)):
                countR += nums[ind]

            print(nums)
            print("countl",countL)
            print("countR" ,countR)
            count += min(countL, countR)

            nums[num]+=1

        print(count)
        return count


        """

        """
        :type instructions: List[int]
        :rtype: int

        # binserach , min of index -1 +1

        # counting if good

        count = 0
        nums = []

        nums.append(instructions[0])
        # nlogn

        for i in range(1,len(instructions)):
            num = instructions[i]

            left = 0
            right = len(nums)


            while left < right:

                mid = (left + right)//2
                if nums[mid] < num:
                    left = mid+1
                else:
                    right =mid

            lg = left -1
            rg = left

            while lg >0 and  nums[lg] == num:
                lg-=1

            while rg < len(nums) and nums[rg] == num:

                rg+=1




        """
        print(instructions)
        repe=[0]*(max(instructions)+1)

        for i in range(len(instructions)):
            num = instructions[i]
            repe[num] +=1

        temp = 0
        for num in range(1,len(repe)):
            if repe[num]!=0:
                repe[num] = temp+repe[num]
                temp = repe[num]

        print(repe)

        count = 0

        nums=[0]*(max(instructions)+1)

        # nlogn


        for i in range(len(instructions)):
            num = instructions[i]

            countL= 0
            for ind in range(num):
                countL += nums[ind]

            countR= 0
            for ind in range(num+1, len(nums)):
                countR += nums[ind]

            print(nums)
            print("countl",countL)
            print("countR" ,countR)
            count += min(countL, countR)

            nums[num]+=1
            repe[num]-=1


        print(count)
        return count

        """



            print(repe[left])
            #print(nums ,"number " , lg+1  , len(nums) -rg )
            count += min(lg+1  , len(nums) -rg)

            nums.insert(left , num)

        print(count)

        """





s= Solution()
instructions = [1,5,6,2]

s.createSortedArray(instructions )
instructions = [1,2,3,6,5,4]

s.createSortedArray(instructions )
instructions = [1,3,3,3,2,4,2,1,2]


s.createSortedArray(instructions )
