class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}      # dict to store number and occurrence

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # sort the dict's items by count, descending
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result


