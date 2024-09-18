from typing import List

# * Anagram Groups

# * Difficult: Medium

# Given an array of strings strs, group all anagrams together 
# into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters 
# as another string, but the order of the characters can be different.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list = []
        for string in strs:
            word_to_sort = list(string)
            word_to_sort.sort()
            sorted_string = "".join(word_to_sort)
            new_list.append(sorted_string)
            if sorted_string not in new_list[new_list.index(sorted_string) + 1:]:
                strs.pop(new_list.index(sorted_string))
        return strs
    
test = Solution()
print(test.groupAnagrams(['hat', 'pop', 'david', 'divad', 'cat', 'tac', 'hat', 'hair']))