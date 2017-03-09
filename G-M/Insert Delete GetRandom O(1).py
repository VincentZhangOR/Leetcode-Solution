# coding=utf-8
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s={}
        self.l=[]
        self.size=0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.s:

            self.s[val]=self.size
            self.l.append(val)
            self.size+=1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set . Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.s:
            return False
        else:
            index=self.s[val]
            value=self.l[-1]
            self.l[index]=value
            self.s[value]=index
            
            
            self.size-=1
            self.s.pop(val)
            self.l.pop()
            return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        r=random.randint(0,self.size -1)
        return self.l[r]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)

