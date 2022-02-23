"""leetcode.com Task 4. Median of Two Sorted Arrays.

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""
import typing as t


class Solution:
    """Class for defining the median of the two sorted arrays."""

    def findMedianSortedArrays(self,
                               nums1: t.List[int],
                               nums2: t.List[int]) -> float:
        """Return the median of the two sorted arrays."""
        if len(nums1) < len(nums2):
            return Solution.findMedianSortedAB(nums1, nums2)
        else:
            return Solution.findMedianSortedAB(nums2, nums1)

    def findMedianSortedAB(nums1: t.List[int],
                           nums2: t.List[int]) -> float:
        """Return the solution in assumption that length of nums1 < nums2."""
        ln1 = len(nums1)
        ln2 = len(nums2)
        half = (ln1 + ln2) // 2
        left = 0  # initial left position in the first list
        right = ln1 - 1  # initial right position in the first list

        """Binary search through the arrays.
        The conditions of exit are:
        nums1[i]<nums2[j+1]
        nums2[j]<nums1[i+1]
        and i+j = half
        If index exceeds the limits of the array, + or - infinity
        is used instead of array's elements."""
        while True:
            i1 = (left + right)//2  # nums1 index
            i2 = half - i1 - 2  # nums2 index
            """defining medians of nums1"""
            if i1 >= 0:
                num1_left = nums1[i1]
            else:
                num1_left = float('-inf')
            """next element is right if exists """
            if i1+1 <= ln1 - 1:
                num1_right = nums1[i1+1]
            else:
                num1_right = float('inf')

            """defining medians of nums2"""
            if i2 >= 0:
                num2_left = nums2[i2]
            else:
                num2_left = float('-inf')
            """next element is right if exists """
            if i2+1 <= ln2 - 1:
                num2_right = nums2[i2+1]
            else:
                num2_right = float('inf')

            if num1_left <= num2_right and num2_left <= num1_right:
                if (ln1+ln2) % 2 == 1:
                    return min(num1_right, num2_right)
                else:
                    return 0.5*(min(num1_right, num2_right) + max(num1_left, num2_left))
            elif num1_left > num2_right:  # num1 left is too far to the right
                right = i1 - 1
            else:  # num2_left > num1_right; num1_right is too far to the left
                left = i1 + 1


nums1 = [1, 2]

nums2 = [3, 4]

# print(nums1)

a = Solution.findMedianSortedArrays(None, nums1, nums2)
print(a)
# nums1 += nums2
# nums1.sort()
# print(nums1, nums1[len(nums1)//2])



