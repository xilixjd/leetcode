# -*- coding: utf-8 -*-
'''
Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements.
The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
'''

import random
class RandomizedCollectionBad(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.pos = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.array:
            self.array.append(val)
            return False
        else:
            self.array.append(val)
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.array:
            self.array.remove(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        length = len(self.array)
        return self.array[random.randint(0, length - 1)]

class RandomizedCollectionReWrite(object):
    def __init__(self):
        self.array = []
        self.arrDict = {}

    def insert(self, val):
        self.array.append(val)
        arr_length = len(self.array) - 1
        if self.arrDict.get(val) is None:
            self.arrDict[val] = set([arr_length])
            return True
        else:
            self.arrDict[val].add(arr_length)
            return False

    def remove(self, val):
        if self.arrDict.get(val) is None or self.arrDict.get(val) == set([]):
            return False
        else:
            remove_pos = self.arrDict[val].pop()
            self.array[remove_pos] = self.array[-1]
            if len(self.arrDict[self.array[remove_pos]]) != 0:
                # 先 add 再 pop()
                self.arrDict[self.array[remove_pos]].add(remove_pos)
                self.arrDict[self.array[remove_pos]].discard(len(self.array) - 1)
            self.array.pop()
            return True

    def getRandom(self):
        return random.choice(self.array)

a = RandomizedCollectionReWrite()
print a.insert(1)
# print a.arrDict
print a.remove(1)

print a.array

import collections
class RandomizedCollectionFast(object):

    def __init__(self):
        self.vals, self.idxs = [], collections.defaultdict(set)

    def insert(self, val):
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)
        return len(self.idxs[val]) == 1

    def remove(self, val):
        if self.idxs[val]:
            out, ins = self.idxs[val].pop(), self.vals[-1]
            self.vals[out] = ins
            if self.idxs[ins]:
                self.idxs[ins].add(out)
                self.idxs[ins].discard(len(self.vals) - 1)
            self.vals.pop()
            return True
        return False

    def getRandom(self):
        return random.choice(self.vals)



        # Your RandomizedCollection object will be instantiated and called as such:
        # obj = RandomizedCollection()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()