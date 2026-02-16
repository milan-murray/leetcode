# Median of Two Sorted Arrays - Analysis

## Problem Summary
Find the median value of the combined sorted array formed by merging two sorted input arrays with O(log(m+n)) time complexity.

## Key Points
- Two sorted arrays: nums1 (size m), nums2 (size n)
- Median definition depends on whether the combined array has odd or even length
- Must achieve O(log(m+n)) time complexity
- Constraints: m, n up to 1000, total up to 2000 elements

## Approach: Binary Search on Smaller Array

### Core Idea
Instead of merging arrays (O(m+n)), we can use binary search to find the correct partition point in the smaller array, allowing us to determine the median without fully merging.

### Algorithm Steps
1. Ensure nums1 is the smaller array for optimal binary search range
2. Perform binary search on nums1 to find partition point i (0 to m)
3. Calculate corresponding partition point j = (m + n + 1) / 2 - i
4. Validate partition:
   - If max_left <= min_right, partition is correct
   - If i > 0 and j < n and nums1[i-1] > nums2[j], move binary search left
   - If j > 0 and i < m and nums2[j-1] > nums1[i], move binary search right
5. Calculate median based on partition positions

### Edge Cases
- One array empty
- Arrays of different sizes
- Odd/even total element count
- All elements in one array

## Complexity Analysis
- **Time**: O(log(min(m, n))) - binary search on smaller array
- **Space**: O(1) - only using constant extra space

## Potential Pitfalls
- Incorrect boundary calculations for odd/even lengths
- Not handling empty array cases
- Off-by-one errors in partition comparisons