# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# You can assume that K is less than or equal to the length of the given string.
# Example 1
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# ARAACI 
# {A:1}
# {A:1, R:1}
# {A:2, R:1}
# {A:3, R:1} -> ARAA
# RAACI
# {A:2, R:1, C:1}
# {A:2, R:0, C:1, I:1}
       
def substr1(arr,k):
    start_char = 0
    end_char = 0
    longest = 0
    window_start = 0
    char_freq = {}

    for window_end in range(len(arr)):
        end_char = arr[window_end]
        if end_char not in char_freq:
            char_freq[end_char] = 1
        else:
            char_freq[end_char] += 1
        while(len(char_freq) > k):
            start_char = arr[window_start]
            char_freq[start_char] -= 1
            window_start += 1
            if char_freq[start_char] == 0:
                del char_freq[start_char]
        longest = max(longest, window_end - window_start + 1)
        print("Longest", longest)
        print("Countmap", char_freq)
    print(longest)

substr1("araaci", 2)