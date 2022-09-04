from itertools import zip_longest

class Solution:
    def mergeAlternately(word1: str, word2: str) -> str:
        # merged = ''
        # for i in range(max(len(word1), len(word2))):
        #     try:
        #         merged += word1[i]
        #         merged += word2[i]
        #     except:
        #         if len(word1) > len(word2):
        #             pass
        #         else:
        #             merged += word2[i]
        # return merged
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))

print(Solution.mergeAlternately(word1 = "abc", word2 = "pqr"))