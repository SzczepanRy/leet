class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        offset = ord("a")

        st = set()
        li = list(s)
        n = 0
        maxn = 0
        for char in li:
            if char not in st:
                st.add(char)
                n += 1
                if maxn < ord(char) - offset:
                    maxn = ord(char) - offset

        freq = [0] * (maxn+1)
        instack = [0] * (maxn+1)

        for char in li:
            freq[ord(char) - offset] += 1

        for char in li:

            freq[ord(char) - offset] -= 1

            if instack[ord(char)-offset]  == 1 :
                continue

            while len(stack)!= 0 and  ord(stack[-1]) >= ord(char) and freq[ord(stack[-1]) - offset] > 0 :
                    ch = stack.pop()
                    instack[ord(ch) - offset] = 0

            stack.append(char)
            instack[ord(char) - offset] = 1


                # morzyemy usunac wsyskie ze stacku

        return "".join(stack)





s = Solution()
print(s.removeDuplicateLetters("cbacdcbc"))
