"""leetcode.com Task 3. Longest Substring Without Repeating Characters.

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
# import typing as t


class Solution:
    """Class for defining the lengthl of the longest substring."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        """Define the length of the longest substring."""
        left = 0
        right = 0
        length_max = 1
        s_len = len(s)
        if s_len <= 1:
            return s_len
        for i in range(1, s_len):
            right = i

            try:
                a = s[left:right:1].index(s[i])
                left += a + 1
            except ValueError:
                a = -1
                if right + 1 - left > length_max:
                    length_max = right + 1 - left
        return length_max


s = "abcabcbb"
d = Solution.lengthOfLongestSubstring(Solution.lengthOfLongestSubstring, s)
print(d)
