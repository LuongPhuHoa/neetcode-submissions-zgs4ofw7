class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for item in strs:
            freq = {}
            freq = [0]* 26
            for char in item:
                index = ord(char)- ord('a')
                freq[index] += 1
            signature = tuple(freq)
            result[signature].append(item)
        return list(result.values())
