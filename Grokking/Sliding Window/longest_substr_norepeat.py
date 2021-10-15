# Given a string, find the length of the longest substring, which has no repeating characters.
# Example 1:
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".

def longest_substr(s):
    mapper = {}
    left = 0
    max_str_len = 0
    for right in range(len(s)):
        if s[right] not in mapper:
            mapper[s[right]] = 1
        else:
            mapper[s[right]]  += 1
        
        if mapper[s[right]] > 1:
            max_str_len = max(max_str_len, len(mapper))
            # left += 1
            mapper[s[right]] -= 1

    return max_str_len



print(longest_substr("aabccbb"))
    
    



    