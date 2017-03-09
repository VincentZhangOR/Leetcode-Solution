# coding=utf-8
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.childs=dict()
        self.isWord=False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node=self.root
        for x in word:
            child=node.childs.get(x)
            if child==None:
                child=TrieNode()
                node.childs[x]=child
            node=child
        node.isWord=True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node=self.root
        for x in word:
            child=node.childs.get(x)
            if child==None:
                return False
            node=child
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node=self.root
        for x in prefix:
            child=node.childs.get(x)
            if child==None:
                return False
            node=child
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
