def minSwaps(nums):
    n = len(nums)
    k = nums.count(1)  # Total number of 1's in the array
    
    if k == 0:
        return 0  # No 1's to group
    
    # Initial count of 1's in the first window of size k
    current_ones = sum(nums[:k])
    max_ones = current_ones
    
    # Use sliding window technique to find the maximum number of 1's in any window of size k
    for i in range(1, n):
        # Slide the window: subtract the element going out of the window and add the element coming into the window
        current_ones = current_ones - nums[i-1] + nums[(i+k-1) % n]
        max_ones = max(max_ones, current_ones)
    
    # Minimum swaps needed to group all 1's together
    return k - max_ones


