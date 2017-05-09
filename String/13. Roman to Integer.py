'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.


'''


class Solution(object):
    def romanToInt(self, s):
        """
        public class Solution {
    public int romanToInt(String s) {
        HashMap<Character,Integer> map = new HashMap<Character,Integer>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        int value = map.get(s.charAt(0));
        for(int i=1;i<s.length();i++){
            if( map.get(s.charAt(i))>map.get(s.charAt(i-1))){
                value = value + map.get(s.charAt(i))- 2*map.get(s.charAt(i-1));
            }
            else{
                value = value + map.get(s.charAt(i));
            }
        }
        return value;
    }
}
        :type s: str
        :rtype: int
        """
        rom_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        value = rom_dict[s[0]]
        for i in range(1, len(s)):
            if rom_dict[s[i]] > rom_dict[s[i - 1]]:
                value += rom_dict[s[i]] - 2 * rom_dict[s[i - 1]]
            else:
                value += rom_dict[s[i]]
        return value

solu = Solution()
print solu.romanToInt('MIVVVVVV')