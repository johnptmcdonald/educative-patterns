from heapq import heappush, heappop

class MedianOfAStream:
    """Make a minheap and a maxheap
    if the num to add is small, put it on the max heap.
    If the number is large, put it on the min heap.
    Then rebalance so the size of the heaps is the same.
    If there are an odd number of elements, put the extra on eon the maxheap

    Visually, it works like this. Just ignore the negative signs (heapq only makes minheaps)

    minHeap:        10      15
                        9
        median ---->
                        -8
    maxHeap:        -6      -7

    As you add numbers, the tip of the minheap moves over to the maxheap or vice versa. 
    """
    def __init__(self):
        self.minheap = []
        self.maxheap = []


    def insert_num(self, num):
        # largest = maxheap[0]
        # smallest = minheap[0]
        if not self.maxheap or -self.maxheap[0] >= num:
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)

        # rebalance
        if len(self.maxheap) > len(self.minheap) + 1:
            heappush(self.minheap, -heappop(self.maxheap))
        elif len(self.maxheap) < len(self.minheap):
            heappush(self.maxheap, -heappop(self.minheap))

    def get_median(self):
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap)/2

        return -self.maxheap[0]

