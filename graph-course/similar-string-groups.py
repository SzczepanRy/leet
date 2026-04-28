class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """


        parents = {strs[i] :strs[i] for i in range(len(strs))}


        def is_similar(s1,s2):

            diff = 0

            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff+=1
                    if diff>2:
                        return False

            return diff==2 or diff == 0


        def find(s):
            if s == parents[s]:
                return parents[s]
            parents[s] = find(parents[s])
            return parents[s]

        def union(s1,s2):
            rs1 = find(s1)
            rs2 = find(s2)

            if rs1 != rs2:
                if rs1 >rs2:
                    parents[rs1] = rs2
                else:
                    parents[rs2] = rs1

        for i in range(len(strs)):
            for j in range(i , len(strs)):
                if is_similar(strs[i] , strs[j]):
                    union(strs[i] , strs[j])

        s = set()
        for key in parents:
            s.add(find(key))


        return len(s)

strs = ["tars","rats","arts","star"]
s=Solution()
s.numSimilarGroups(strs)
