from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList:
            return 0

        # n = len(wordList)
        wordSet= set(wordList)

        """
        visited = {word: False for word in wordList}
        """
        queue = deque([(beginWord, 1)])

        while queue:
            curr , dist = queue.popleft()

            if endWord == curr:
                    print(dist)
                    return dist

            for i in range(len(curr)):
                for char_code in range(ord('a') , ord('z')+1):
                    next_word = curr[:i] + chr(char_code) + curr[i+1:]
                    if next_word in wordSet:
                        queue.append((next_word,dist+1))
                        wordSet.remove(next_word)



                    """
                    this is normal and slow

            for word in wordList:
                if not visited[word]:

                    diff = 0
                    for i in range(len(word)):
                        if word[i] != curr[i]:
                            diff += 1

                    if diff == 1:
                        queue.append((word,dist+1))
                        visited[word] = True
                    """
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
s = Solution()
s.ladderLength(beginWord, endWord, wordList)
