class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        min_length = min(len(word1),len(word2))

        for i in range(min_length):
            res.append(word1[i])
            res.append(word2[i])
        
        res.append(word1[min_length:])
        res.append(word2[min_length:])

        return "".join(res)
