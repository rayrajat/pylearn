"""public class LongestSubstringWithoutRepeatingCharacters {
    public static int lengthof longestsubstring(String s){
        int n = s.length();
        HashSet<character> seen = new HashSet<>();
        int maxlength = 0;
        int left = 0;

        for(int right=0;right<n;right++){
            while(seen.contains(s.charAt(right))){
                seen.remove(s.charAt(left));
                left++;
            
            }
            seen.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left+1);
        }
        return maxLength;
    }"""




#python code!
def length_of_longest_substring(s: str) -> int:
    n = len(s)
    seen = set()
    max_length = 0
    left = 0

    for right in range(n):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
