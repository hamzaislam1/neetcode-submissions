class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for str in strs:
            counts = [0] * 26
            for letter in str:
                index = ord(letter) - ord('a')
                counts[index] += 1
            key = tuple(counts)
            if key not in groups:
                groups[key] = []
            groups[key].append(str)
        return list(groups.values())