class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """

        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}

        def find(char):
            if parent[char] == char:
                return char

            parent[char] = find(parent[char])

            return parent[char]

        def union(char1 ,char2 ):

            r1=find(char1)
            r2=find(char2)

            if r1 != r2:
                if r1 > r2:
                    parent[r1]= r2
                else:
                    parent[r2]= r1



        for i  in range(len(s1)):
            char1 = s1[i]
            char2 = s2[i]
            union(char1,char2)

        res = ""
        for i  in range(len(baseStr)):
            rep = find(baseStr[i])
            res+= rep

        return res

s1 = "parker"
s2 = "morris"
baseStr = "parser"

s=Solution()
s.smallestEquivalentString(s1,s2,baseStr)
