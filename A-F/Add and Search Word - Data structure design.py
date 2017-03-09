# coding=utf-8
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = dict()
        self.height = 0

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for x in word:
            cur = cur.setdefault(x, {})
        cur.setdefault('_end')
        self.height = max(self .height, len(word))
        #print self.root
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character ' .' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) > self.height:
            return False
        return self.dfs(self.root, word)
    
    def dfs(self, root, word):
        if root == None:
            return False
        if '_end' in root:
            if len(word) == 0:
                return True
        if len(word) == 0:
            return False
        cur = root
        #for i in xrange(len(word)):
        if word[0] == '.':
            for y in cur:
                if self.dfs(cur[y], word[1:]):
                    return True
            return False
        else:
            if word[0] in cur:
                #print cur, word, word[0], cur[word[0]]
                return self.dfs (cur[word[0]], word[1:])
            return False
        
        
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")

