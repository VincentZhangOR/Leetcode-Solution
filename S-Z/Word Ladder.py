# coding=utf-8
class Solution(object):
    def ladderLength(self, beginWord , endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        d = set(wordList)
        if endWord not in d:
            return 0
        n = len(beginWord)
        queue = [beginWord]
        cnt = 1
        while queue:
            
            cnt += 1
            
            frontier = []
            for x in queue:
                for i in xrange(n):
                    for y in 'abcdefghijklmnopq rstuvwxyz':
                        if y == x[i] :
                            continue
                        temp = x[:i] + y + x[i+1:]
                        if temp == endWord:
                            return cnt
                        elif temp in d:
                            frontier .append(temp)
                            d.remove (temp)
            queue = frontier

