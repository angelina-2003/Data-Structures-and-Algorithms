from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = Counter(nums)
            top_k = count.most_common(k)   # returns [(num, count), ...] already sorted, top k only!
            
            result = []
            for pair in top_k:
                result.append(pair[0])
            return result


