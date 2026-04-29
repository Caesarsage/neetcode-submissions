class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()

        # {1:1, 2:2, 3:3}
        # use min heap = []
        # heap keeps the smallest frequency at the top.
        # iterating through the keys
        # first iteration : 1
        # [(1,1)]
        # check if the length of heap is greater than the min k
        # len(heap) > k, not yet, let's proceed
        # second iteration : 2
        # [(1,1),(2,2)] (heap algo: 1 < 2)good
        # similar check
        # third iteratio
        # [(1,1),(2,2),(3,3)] (heap algo: 1 < 2) goor
        # remeber heap keeps the smallest frequecy at root.

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # heap
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        print(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
        