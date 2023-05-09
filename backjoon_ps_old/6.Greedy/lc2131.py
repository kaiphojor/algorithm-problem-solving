from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_dict = dict()
        # li = []
        isSolidCountOdd = False
        palindrome_count = 0
        for word in words:
            if word not in word_dict:
                word_dict[word] = 0
            word_dict[word] += 1
        for key in word_dict.keys():
            if word_dict[key] == 0:
                continue
            elif key[0] == key[1]:
                palindrome_count += (word_dict[key] // 2) * 2 * 2
                if not isSolidCountOdd and word_dict[key] % 2 == 1:
                    isSolidCountOdd = True
            elif key[::-1] in word_dict:
                palindrome_count += 2 * min(word_dict[key],word_dict[key[::-1]])
                
        return palindrome_count + (2 if isSolidCountOdd else 0)