class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def atMost(k):
            if k < 0:
                return 0
            
            vowels = {'a','e','i','o','u'}
            last = {v:-1 for v in vowels}
            
            left = 0
            consonants = 0
            res = 0
            
            for right, c in enumerate(word):
                
                if c in vowels:
                    last[c] = right
                else:
                    consonants += 1
                
                while consonants > k:
                    if word[left] not in vowels:
                        consonants -= 1
                    left += 1
                
                min_vowel = min(last.values())
                
                if min_vowel >= left:
                    res += min_vowel - left + 1
            
            return res
        
        return atMost(k) - atMost(k-1)