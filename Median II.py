"""
Numbers keep coming, return the median of numbers at every time a new number added.

Example
For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3]

For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3]

For numbers coming list: [2, 20, 100], return [2, 2, 20]

Challenge
O(nlogn) time

Clarification
What's the definition of Median?

Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is
A[(n-1)/2].
For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.
"""
__author__ = 'Danyang'
import heapq
class Solution:
    def __init__(self):
        self.heap_min = []
        self.heap_max = []

    def insert(self, num):
        if not self.heap_min or num>self.heap_min[0]:
            heapq.heappush(self.heap_min, num)
        else:
            heapq.heappush(self.heap_max, -num)
        self.balance()

    def balance(self):
        l1 = len(self.heap_min)
        l2 = len(self.heap_max)
        if l1-l2>1:
            heapq.heappush(self.heap_max, -heapq.heappop(self.heap_min))
            self.balance()
        elif l2-l1>1:
            heapq.heappush(self.heap_min, -heapq.heappop(self.heap_max))
            self.balance()
        return

    def get_median(self):
        l1 = len(self.heap_min)
        l2 = len(self.heap_max)
        m = (l1+l2-1)/2
        if m==l2-1:
            return -self.heap_max[0]
        elif m==l2:
            return self.heap_min[0]
        raise Exception("not balanced")


    def medianII(self, nums):
        """

        :param nums: A list of integers.
        :return: The median of numbers
        """
        ret = []
        for num in nums:
            self.insert(num)
            ret.append(self.get_median())
        return ret

if __name__=="__main__":
    assert Solution().medianII([4, 5, 1, 3, 2, 6, 0])==[4, 4, 4, 3, 3, 3, 3]


