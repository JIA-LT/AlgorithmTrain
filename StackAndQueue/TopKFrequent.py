from typing import List
import heapq

class solution:
    def topKFrequent(self, nums:List[int], k)->List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
        print(map)
        priority_queue = []
        for key,freq in map.items():
            heapq.heappush(priority_queue,(freq,key))
            if len(priority_queue) > k:
                heapq.heappop(priority_queue)

        result = [0]*k
        print(result)
        for i in range(k - 1, -1, -1):
            result[i]=heapq.heappop(priority_queue)[1]
        return result

if __name__ == "__main__":
    s = solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(s.topKFrequent(nums, k))