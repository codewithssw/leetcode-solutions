# LeetCode 3760: Maximum Substrings With Distinct Start
# Time Complexity: O(n) - Single pass loop through the string elements
# Space Complexity: O(1) - Constant space because the set holds at most 26 lowercase English characters

def max_distinct(s):
    include = set()  # Set data structure to filter out duplicate characters
    
    for char in s:
        # Check if the character is unique before adding it
        if char not in include:
            include.add(char)
            
    # The maximum unique starting characters equals the number of distinct items in our set
    return len(include)     

# --- Test Case Execution ---
s = "abab"
output = max_distinct(s)
print("Output: ", output)  # Expected Output: 2