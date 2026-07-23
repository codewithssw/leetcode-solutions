# LeetCode 1512: Number of Good Pairs
# Time Complexity: O(n) - Single pass loop through the input list
# Space Complexity: O(n) - Linear space used to store element frequencies in the dictionary

def num_of_good_pairs(nums):
    count = {}       # Hash map to track the frequency of each number
    good_pairs = 0   # Total accumulator for identical matching pairs
    
    for num in nums:
        # If the number has been seen before, it forms new pairs
        if num in count:
            # Trick: It creates new pairs with ALL previous copies of itself
            good_pairs += count[num]
            count[num] += 1
            
        else:
            # First time seeing this number, assign a baseline frequency of 1
            count[num] = 1     
            
    return good_pairs

# --- Test Case Execution ---
nums = [1, 2, 3, 1, 1, 3]
pairs = num_of_good_pairs(nums)
print("Output: ", pairs)  # Expected Output: 4