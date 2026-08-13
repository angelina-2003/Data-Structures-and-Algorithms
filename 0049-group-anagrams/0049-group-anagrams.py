class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sorted_words = sorted(word)
            key = "".join(sorted_words)

            if key not in groups:           # If didn't start a sub-list for this key then start one
                groups[key] = []

            groups[key].append(word)        # If sub-list exist, then add it into it

        return list(groups.values())



