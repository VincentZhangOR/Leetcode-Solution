# coding=utf-8
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d={}
        self.l=[]

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            self.d[val]={len(self.l )}
            self.l.append(val)
            return True
        else:
            self.d[val].add(len(self .l))
            self.l.append(val)
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            return False
        else:
            last=self.l.pop()
            self.d[last].remove(len (self.l))
            if val!=last:
                index=self.d[val] .pop()
                self.d[last].add (index)
                self.l[index]=last
            if not self.d[val]:
                del self.d[val]
            return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        r=random.randint(0,len(self .l)-1)
        return self.l[r]


# Your RandomizedCollection object will be instantiated and called 
