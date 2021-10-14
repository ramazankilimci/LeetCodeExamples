class Solution:
    def romanToInt(self, s: str) -> int:
        temp_num = 0
        temp_str = s
        while True:   
            # print(temp_str)
            if len(temp_str) == 0:
                break
            if 'CD' in s:
                temp_num += 400
                temp_str = s.replace('CD', '')
            if 'CM' in temp_str:
                temp_num += 900
                temp_str = temp_str.replace('CM', '')
            if 'XL' in temp_str:
                temp_num += 40
                temp_str = temp_str.replace('XL', '')
            if 'XC' in temp_str:
                temp_num += 90
                temp_str = temp_str.replace('XC', '')
            if 'IV' in temp_str:
                temp_num += 4
                temp_str = temp_str.replace('IV', '')
            if 'IX' in temp_str:
                temp_num += 9
                temp_str = temp_str.replace('IX', '')
            if 'I' in temp_str:
                temp_num += temp_str.count('I')
                temp_str = temp_str.replace('I', '')
            if 'V' in temp_str:
                temp_num += temp_str.count('V') * 5
                temp_str = temp_str.replace('V', '')
            if 'X' in temp_str:
                temp_num += temp_str.count('X') * 10
                temp_str = temp_str.replace('X', '')
            if 'L' in temp_str:
                temp_num += temp_str.count('L') * 50
                temp_str = temp_str.replace('L', '')
            if 'C' in temp_str:
                temp_num += temp_str.count('C') * 100
                temp_str = temp_str.replace('C', '')
            if 'D' in temp_str:
                temp_num += temp_str.count('D') * 500
                temp_str = temp_str.replace('D', '')
            if 'M' in temp_str:
                temp_num += temp_str.count('M') * 1000
                temp_str = temp_str.replace('M', '')
        return temp_num

roman_number = 'MCCMCDIVIII'
obj1 = Solution()
print(obj1.romanToInt(roman_number))

