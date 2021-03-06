# -*- coding: utf-8 -*-
'''
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
'''

import random


class ReRandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.set_list = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.dict.get(val) is not None:
            return False
        else:
            self.set_list.append(val)
            self.dict[val] = len(self.set_list) - 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        index = self.dict.get(val)
        if index is not None:
            last_num = self.set_list[-1]
            self.set_list[index] = last_num
            self.dict[last_num] = index
            self.set_list.pop()
            del self.dict[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.set_list[random.randint(0, len(self.set_list) - 1)]


obj = ReRandomizedSet()
print obj.insert(1)
print obj.remove(2)
print obj.insert(2)
print obj.remove(1)
print obj.set_list
print obj.insert(2)
print obj.set_list


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.pos = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.array.append(val)
            self.pos[val] = len(self.array) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            idx, lastNum = self.pos[val], self.array[-1]
            self.array[idx] = lastNum
            self.pos[lastNum] = idx
            del self.pos[val]
            self.array.pop()
            return True
        return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        length = len(self.array)
        return self.array[random.randint(0, length - 1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# print obj.insert(1)
# print obj.remove(2)
# print obj.insert(2)
# print obj.remove(1)
# print obj.pos
# print obj.insert(2)